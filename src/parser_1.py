from src.token_type import TokenType
from src.expression import Literal, Unary, Binary, Grouping, Variable


class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        expression = self.expression()

        if not self.is_at_end():
            self.error(
                self.peek(),
                "Unexpected token after expression"
            )

        return expression

    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparison()

        while self.match(
            TokenType.EQUAL_EQUAL,
            TokenType.NOT_EQUAL
        ):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self):
        expr = self.term()

        while self.match(
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL
        ):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()

        while self.match(
            TokenType.PLUS,
            TokenType.MINUS
        ):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.match(
            TokenType.STAR,
            TokenType.SLASH,
            TokenType.MODULO
        ):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self):
        if self.match(
            TokenType.MINUS,
            TokenType.NOT
        ):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)

        return self.power()

    def power(self):
        expr = self.primary()

        if self.match(TokenType.POWER):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def primary(self):
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.TRUE):
            return Literal(True)

        if self.match(TokenType.FALSE):
            return Literal(False)

        if self.match(TokenType.NULL):
            return Literal(None)
        
        if self.match(TokenType.IDENTIFIER):
            return Variable(self.previous())

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()

            self.consume(
                TokenType.RIGHT_PAREN,
                "Expected ')' after expression"
            )

            return Grouping(expr)

        self.error(
            self.peek(),
            "Expected an expression"
        )

    def match(self, *types):
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True

        return False

    def consume(self, token_type, message):
        if self.check(token_type):
            return self.advance()

        self.error(self.peek(), message)

    def check(self, token_type):
        if self.is_at_end():
            return False

        return self.peek().token_type == token_type

    def advance(self):
        if not self.is_at_end():
            self.current += 1

        return self.previous()

    def is_at_end(self):
        return self.peek().token_type == TokenType.EOF

    def peek(self):
        if self.current >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def error(self, token, message):
        line = token.line

        if token.token_type == TokenType.EOF:
            location = "at end"
        else:
            location = f"at '{token.lexeme}'"

        raise ParseError(
            f"[line {line}] Syntax error {location}: {message}"
        )
