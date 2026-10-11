# Neon Lab 2: AST Printer

## 1. Introduction
For this lab, I continued working on my programming language, Neon. In Lab 1, I made a scanner that reads code and turns it into tokens. In Lab 2, I created an Abstract Syntax Tree (AST) and an AST printer. The AST stores expressions, and the printer shows how they are organized using parentheses.
## 2. Expression Grammar
This is the grammar I used for Neon's expressions.
```text
expression  → logic_or ;
logic_or   → logic_and ( "||" logic_and )* ;
logic_and  → equality ( "&&" equality )* ;
equality   → comparison ( ( "==" | "!=" ) comparison )* ;
comparison → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term       → factor ( ( "+" | "-" ) factor )* ;
factor     → unary ( ( "*" | "/" | "%" ) unary )* ;
unary      → ( "!" | "-" ) unary | primary ;
primary    → NUMBER | STRING | "true" | "false" | "nil" | "(" expression ")" ;
```
Neon supports arithmetic (`+`, `-`, `*`, `/`, `%`), comparison (`<`, `>`, `<=`, `>=`), equality (`==`, `!=`), and logical (`&&`, `||`, `!`) operators. It also supports numbers, strings, booleans, and `nil`. Neon is similar to Lox, but it uses `&&` and `||` instead of `and` and `or`. Neon also supports `%` for modulo.
## 3. AST Classes
I created four classes in `expression.py`:
- **Literal:** Stores a value like `5` or `true`.
- **Unary:** Stores one operator and expression, like `-5`.
- **Binary:** Stores two expressions and an operator, like `5 + 3`.
- **Grouping:** Stores an expression inside parentheses.
I also created `ast_printer.py`, which prints expressions using parentheses to show their structure. For example, `-123 * (45.67)` prints as `(* (- 123) (group 45.67))`. The printer does not calculate the expression.
## 4. Running the Tests
The program uses Python and does not need extra libraries. The main code is in `src/`, and the tests are in `test/lab2/`. Run the tests from the main Neon folder using:

python3 test/lab2/ast_printer_test.py

## 5. Test Results
I created tests for every AST class, operator, literal type, and nested expressions. Each test compares the expected output with the actual output.
### Test 1: Arithmetic and Grouping
AST:
```python
Binary(Unary(operator(TokenType.MINUS, "-"), Literal(123)), operator(TokenType.STAR, "*"), Grouping(Literal(45.67)))
```
Expected: `(* (- 123) (group 45.67))`  
Actual: `(* (- 123) (group 45.67))`  
Result: PASS
### Test 2: Arithmetic Operators
AST used: `Binary(Literal(10), operator(token_type, symbol), Literal(3))`
| Operator | Expected and Actual | Result |
|---|---|---|
| + | `(+ 10 3)` | PASS |
| - | `(- 10 3)` | PASS |
| * | `(* 10 3)` | PASS |
| / | `(/ 10 3)` | PASS |
| % | `(% 10 3)` | PASS |
### Test 3: Comparison Operators
AST used: `Binary(Literal(5), operator(token_type, symbol), Literal(10))`
| Operator | Expected and Actual | Result |
|---|---|---|
| == | `(== 5 10)` | PASS |
| != | `(!= 5 10)` | PASS |
| < | `(< 5 10)` | PASS |
| <= | `(<= 5 10)` | PASS |
| > | `(> 5 10)` | PASS |
| >= | `(>= 5 10)` | PASS |
### Test 4: Logical Operators
AST used: `Binary(Literal(True), operator(token_type, symbol), Literal(False))`
| Operator | Expected and Actual | Result |
|---|---|---|
| && | `(&& true false)` | PASS |
| \|\| | `(\|\| true false)` | PASS |
### Test 5: Unary NOT
AST: `Unary(operator(TokenType.NOT, "!"), Literal(True))`  
Expected: `(! true)`  
Actual: `(! true)`  
Result: PASS
### Test 6: Literal Values
AST used: `Literal(value)`
| Literal | Expected and Actual | Result |
|---|---|---|
| Integer | `100` | PASS |
| Decimal | `3.14` | PASS |
| String | `hello` | PASS |
| True | `true` | PASS |
| False | `false` | PASS |
| Nil | `nil` | PASS |
### Test 7: Nested Expressions
AST:
```python
Binary(Grouping(Binary(Literal(5), operator(TokenType.PLUS, "+"), Literal(3))), operator(TokenType.STAR, "*"), Binary(Literal(10), operator(TokenType.MINUS, "-"), Literal(2)))
```
Expected: `(* (group (+ 5 3)) (- 10 2))`  
Actual: `(* (group (+ 5 3)) (- 10 2))`  
Result: PASS
### Test Summary
I ran 22 tests, and all 22 passed. Every actual output matched the expected output.
## 6. Limitations
The AST printer only prints expressions and does not calculate answers or read Neon source code directly. Expressions must be created manually because Neon does not have a parser yet. The printer supports `nil`, but scanner support for it has not been verified.
## 7. Conclusion
In this lab, I made an AST and a printer for Neon. I learned how expressions can be stored and printed using a tree structure. All 22 tests passed, and this will help when I add more features to Neon later.