
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from expression import Literal, Unary, Binary, Grouping
from ast_printer import ASTPrinter
from token_1 import Token
from token_type import TokenType

printer = ASTPrinter()


def operator(token_type, lexeme):
    return Token(token_type, lexeme, None, 1)


def check(name, expression, expected):
    actual = printer.print(expression)
    result = "PASS" if actual == expected else "FAIL"

    print("Test:", name)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Result:", result)
    print()

# start ai generated 
# Test 1: Basic arithmetic and grouping
expression1 = Binary(
    Unary(operator(TokenType.MINUS, "-"), Literal(123)),
    operator(TokenType.STAR, "*"),
    Grouping(Literal(45.67))
)

check(
    "Arithmetic and grouping",
    expression1,
    "(* (- 123) (group 45.67))"
)

# Test 2: Arithmetic operators
for token_type, symbol in [
    (TokenType.PLUS, "+"),
    (TokenType.MINUS, "-"),
    (TokenType.STAR, "*"),
    (TokenType.SLASH, "/"),
    (TokenType.MODULO, "%")
]:
    expression = Binary(
        Literal(10),
        operator(token_type, symbol),
        Literal(3)
    )

    check(
        "Arithmetic " + symbol,
        expression,
        "(" + symbol + " 10 3)"
    )

# end ai generated 
# Test 3: Comparison and equality
for token_type, symbol in [
    (TokenType.EQUAL_EQUAL, "=="),
    (TokenType.NOT_EQUAL, "!="),
    (TokenType.LESS, "<"),
    (TokenType.LESS_EQUAL, "<="),
    (TokenType.GREATER, ">"),
    (TokenType.GREATER_EQUAL, ">=")
]:
    expression = Binary(
        Literal(5),
        operator(token_type, symbol),
        Literal(10)
    )

    check(
        "Comparison " + symbol,
        expression,
        "(" + symbol + " 5 10)"
    )


# Test 4: Logical operators
for token_type, symbol in [
    (TokenType.AND, "&&"),
    (TokenType.OR, "||")
]:
    expression = Binary(
        Literal(True),
        operator(token_type, symbol),
        Literal(False)
    )

    check(
        "Logical " + symbol,
        expression,
        "(" + symbol + " true false)"
    )

#ai generated start
# Test 5: Unary NOT
expression5 = Unary(
    operator(TokenType.NOT, "!"),
    Literal(True)
)

check(
    "Unary NOT",
    expression5,
    "(! true)"
)
#end ai generated

# Test 6: Literal values
for name, value, expected in [
    ("Integer", 100, "100"),
    ("Decimal", 3.14, "3.14"),
    ("String", "hello", "hello"),
    ("True", True, "true"),
    ("False", False, "false"),
    ("Nulll", None, "nulll")
]:
    check(
        "Literal " + name,
        Literal(value),
        expected
    )


# Test 7: Nested expressions
expression7 = Binary(
    Grouping(
        Binary(
            Literal(5),
            operator(TokenType.PLUS, "+"),
            Literal(3)
        )
    ),
    operator(TokenType.STAR, "*"),
    Binary(
        Literal(10),
        operator(TokenType.MINUS, "-"),
        Literal(2)
    )
)

check(
    "Nested expressions",
    expression7,
    "(* (group (+ 5 3)) (- 10 2))"
)
