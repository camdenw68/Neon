from enum import Enum, auto

class TokenType(Enum):
    # ai generated for an example for everything else, following the same pattern.
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    MODULO = auto()
    SLASH = auto()
    # end ai generated

    POWER = auto()

    AND = auto()
    OR = auto()
    NOT = auto()

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()

    EQUAL = auto()
    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()

    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    RETURN = auto()
    TRY = auto()
    CATCH = auto()
    FINALLY = auto()

    TRUE = auto()
    FALSE = auto()

    I8 = auto()
    I16 = auto()
    I32 = auto()
    I64 = auto()

    U8 = auto()
    U16 = auto()
    U32 = auto()
    U64 = auto()

    CHAR = auto()
    BOOL = auto()
    STRING_TYPE = auto()

    EOF = auto()