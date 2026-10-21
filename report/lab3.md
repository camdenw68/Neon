# Lab 3: Parser
## Overview
For this lab, I added a parser to Neon. In Lab 1, I created a scanner that reads source code and turns it into tokens. In Lab 2, I created expression classes and an AST printer. In this lab, I connected everything so Neon can read an expression, turn it into tokens, build an abstract syntax tree (AST), and print the result.
## Implementation
I created a Parser class in parser_1.py. The parser uses recursive descent, which means it has separate methods for different types of expressions. These methods handle operator precedence, so operations happen in the correct order. For example, multiplication has higher precedence than addition.
I reused my scanner, token classes, expression classes, and AST printer from the previous labs. I also added a Variable expression class so Neon can recognize variable names such as score.
The main.py file now connects the scanner, parser, and AST printer. It supports both interactive input and reading an expression from a file.
## Expression Grammar
expression → equality
equality → comparison (("==" | "!=") comparison)*
comparison → term ((">" | ">=" | "<" | "<=") term)*
term → factor (("+" | "-") factor)*
factor → unary (("*" | "/" | "%") unary)*
unary → ("-" | "!") unary | power
power → primary ("**" unary)?
primary → NUMBER | STRING | true | false | null | IDENTIFIER | "(" expression ")"
```
## Precedence and Associativity
The parser handles precedence in this order, from highest to lowest:
1. Parentheses
2. Exponentiation (**)
3. Unary minus and NOT (-, !)
4. Multiplication, division, and modulo (*, /, %)
5. Addition and subtraction (+, -)
6. Comparison operators (>, >=, <, <=)
7. Equality operators (==, !=)
Most operators are left-associative, meaning expressions with the same precedence group from left to right. Exponentiation is right-associative, meaning `2 ** 3 ** 2` groups as `2 ** (3 ** 2)`. Unary operators apply to the expression on their right. In an expression such as `-2 ** 2`, exponentiation groups before unary minus.
## Differences From Lox
Neon is based partly on Lox, but I changed some features. Neon uses null instead of nil. I also added modulo (%) and exponentiation (**) as expression operators. The scanner recognizes additional keywords and data types for future parts of the language. I kept the AST classes from Lab 2 and added a Variable class for identifiers. The parser only handles expressions right now, not full statements or programs.
## Setup and Running
Neon uses Python 3 with no external dependencies. All commands should be run from the main Neon repository folder.
Interactive mode:
python3 -m src.main

File mode:
python3 -m src.main test/lab3/valid.neon

Run automated tests:
python3 -m unittest discover -s test/lab3 -v

## Tests
I created tests in test/lab3/test_parser.py to check the parser. The tests cover literals, arithmetic, precedence, associativity, grouping, unary expressions, comparisons, equality, variables, and error handling.
After adding support for variables, all 11 automated tests passed.

test_arithmetic ... ok
test_associativity ... ok
test_boolean_and_null ... ok
test_comparison ... ok
test_equality ... ok
test_errors ... ok
test_grouping ... ok
test_literals ... ok
test_recovery ... ok
test_unary ... ok
test_variables ... ok

Ran 11 tests
OK

## Valid Test Cases
The following table shows the inputs and expected AST outputs used to check the parser. The passing automated tests confirm the results for these cases.
| Input | Expected and Actual AST | Result |
|---|---|---|
| `42` | `42` | Pass |
| `3.5` | `3.5` | Pass |
| `"hello"` | `hello` | Pass |
| `true` | `true` | Pass |
| `false` | `false` | Pass |
| `null` | `null` | Pass |
| `10 + 5 * 2` | `(+ 10 (* 5 2))` | Pass |
| `(10 + 5) * 2` | `(* (group (+ 10 5)) 2)` | Pass |
| `10 - 5 - 2` | `(- (- 10 5) 2)` | Pass |
| `-5 + 10` | `(+ (- 5) 10)` | Pass |
| `10 >= 5` | `(>= 10 5)` | Pass |
| `5 == 5` | `(== 5 5)` | Pass |
| `10 % 3` | `(% 10 3)` | Pass |
| `score + 5` | `(+ score 5)` | Pass |
## Invalid Test Cases
These tests check that Neon reports errors instead of crashing.
| Input | Expected Problem | Result |
|---|---|---|
| `10 +` | Missing right operand | Pass |
| `(10 + 5` | Missing closing parenthesis | Pass |
| `10 + * 5` | Unexpected operator | Pass |
| `10 20` | Unexpected trailing token | Pass |
| `* 5` | Missing left operand | Pass |
| `()` | Missing expression | Pass |
The tests confirm that invalid expressions are rejected. For example, `10 +` ends before the parser finds the second value. The expression `(10 + 5` does not have a closing parenthesis. The input `10 20` contains an extra token after the expression. The parser reports a syntax error with the line number and location of the problem.
## Syntax Tree Example
For the expression `10 + 5 * 2`, the tree is:
```text
       +
      / \
    10   *
        / \
       5   2
```
The printed AST is:
```text
(+ 10 (* 5 2))
```
The root of the tree is addition. Its left child is 10, and its right child is multiplication. Multiplication has two children, 5 and 2. The printed AST represents the same tree because multiplication is grouped inside addition.
## Error Handling
The parser uses ParseError to report problems in expressions. It checks for missing operands, missing parentheses, unexpected tokens, and extra tokens after an expression. The scanner also checks for invalid characters and unterminated strings. If the scanner or parser finds an error, main.py does not print a successful AST. Interactive mode can continue after an invalid expression. The recovery test passed.
## Known Limitations
The parser currently handles one expression at a time. It cannot parse full Neon programs with functions, variable declarations, loops, or conditional statements. Identifiers are supported as expressions, but the parser does not evaluate variables or store their values. Logical AND and OR are recognized by the scanner but are not yet implemented in the parser.
