from src.token_type import TokenType
from src.token_1 import Token


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.had_error = False

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        char = self.advance()

        if char == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif char == ")":
            self.add_token(TokenType.RIGHT_PAREN)
        elif char == "{":
            self.add_token(TokenType.LEFT_BRACE)
        elif char == "}":
            self.add_token(TokenType.RIGHT_BRACE)
        elif char == "[":
            self.add_token(TokenType.LEFT_BRACKET)
        elif char == "]":
            self.add_token(TokenType.RIGHT_BRACKET)
        elif char == ";":
            self.add_token(TokenType.SEMICOLON)
        elif char == ",":
            self.add_token(TokenType.COMMA)
        elif char == ".":
            self.add_token(TokenType.DOT)
        elif char == "+":
            self.add_token(TokenType.PLUS)
        elif char == "-":
            self.add_token(TokenType.MINUS)
        elif char == "*":
            self.add_token(TokenType.POWER if self.match("*") else TokenType.STAR)
        elif char == "%":
            self.add_token(TokenType.MODULO)
        elif char == "!":
            self.add_token(TokenType.NOT_EQUAL if self.match("=") else TokenType.NOT)
        elif char == "=":
            self.add_token(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL)
        elif char == "<":
            self.add_token(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS)
        elif char == ">":
            self.add_token(TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER)
        elif char == "&":
            if self.match("&"):
                self.add_token(TokenType.AND)
            else:
                self.error("Unexpected '&'. Did you mean '&&'?")
        elif char == "|":
            if self.match("|"):
                self.add_token(TokenType.OR)
            else:
                self.error("Unexpected '|'. Did you mean '||'?")
        # start ai generated 
        elif char == "/":
            if self.match("/"):
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif char in (" ", "\r", "\t"):
            pass
        elif char == "\n":
            self.line += 1
        elif char == '"':
            self.string()
        elif char.isdigit():
            self.number()
        elif char.isalpha() or char == "_":
            self.identifier()
        else:
            self.error(f"Unexpected character '{char}'.")
        # end ai generated 

    def identifier(self):
        while self.peek().isalnum() or self.peek() == "_":
            self.advance()

        text = self.source[self.start:self.current]

        keywords = {
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "while": TokenType.WHILE,
            "for": TokenType.FOR,
            "return": TokenType.RETURN,
            "try": TokenType.TRY,
            "catch": TokenType.CATCH,
            "finally": TokenType.FINALLY,
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "i8": TokenType.I8,
            "i16": TokenType.I16,
            "i32": TokenType.I32,
            "i64": TokenType.I64,
            "u8": TokenType.U8,
            "u16": TokenType.U16,
            "u32": TokenType.U32,
            "u64": TokenType.U64,
            "char": TokenType.CHAR,
            "bool": TokenType.BOOL,
            "string": TokenType.STRING_TYPE,
        }

        token_type = keywords.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)

    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == "." and self.peek_next().isdigit():
            self.advance()

            while self.peek().isdigit():
                self.advance()

        text = self.source[self.start:self.current]

        if "." in text:
            literal = float(text)
        else:
            literal = int(text)

        self.add_token(TokenType.NUMBER, literal)
    #start ai generated
    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1

            self.advance()

        if self.is_at_end():
            self.error("Unterminated string.")
            return

        self.advance()

        literal = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, literal)
    #end ai generated
    def advance(self):
        char = self.source[self.current]
        self.current += 1
        return char

    def match(self, expected):
        if self.is_at_end():
            return False

        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.is_at_end():
            return "\0"

        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"

        return self.source[self.current + 1]

    def add_token(self, token_type, literal=None):
        lexeme = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, lexeme, literal, self.line))

    def is_at_end(self):
        return self.current >= len(self.source)

    def error(self, message):
        self.had_error = True
        print(f"[line {self.line}] Scanner error: {message}")
