# Lab 1 - Neon Scanner

## About Neon
For this lab I created a language called Neon. I wanted Neon to have some lower-level features like C while still keeping the syntax simple. Right now Neon only has a scanner, so it cannot actually execute code yet. The scanner reads Neon source code and breaks it into tokens.

For example, `i32 health = 100;` becomes `I32`, `IDENTIFIER`, `EQUAL`, `NUMBER`, and `SEMICOLON`.

## Keywords
Neon currently recognizes:

`if`, `else`, `while`, `for`, `return`, `try`, `catch`, `finally`, `true`, `false`, `i8`, `i16`, `i32`, `i64`, `u8`, `u16`, `u32`, `u64`, `char`, `bool`, `string`

If a word follows the identifier rules but is not a keyword, it becomes an `IDENTIFIER`.

## Operators and Punctuation
Neon supports the following operators:

`+` addition, `-` subtraction, `*` multiplication, `/` division, `%` modulo, `**` power

`=` assignment, `==` equal, `!=` not equal, `<` less than, `<=` less than or equal, `>` greater than, `>=` greater than or equal

`&&` AND, `||` OR, `!` NOT

Neon also recognizes the punctuation:

`(` `)` `{` `}` `[` `]` `;` `,` `.`

The dot allows code such as `console.write("Hello");`. At this point, the scanner only recognizes `console` and `write` as identifiers with a dot between them. It does not execute `console.write`.

## Identifiers
The regular expression for identifiers is:

`[A-Za-z_][A-Za-z0-9_]*`

An identifier starts with a letter or underscore. After that, it can contain letters, numbers, or underscores.

Examples: `health`, `player2`, `player_score`, `_privateValue`

## Numbers
The regular expression for numbers is:

`[0-9]+(\.[0-9]+)?`

This allows whole numbers such as `100` and decimal numbers such as `99.5`. Whole numbers are stored as integers and decimals are stored as floats.

## Strings
The basic regular expression for strings is:

`"[^"]*"`

Strings start and end with double quotes. The lexeme keeps the quotes because it represents the original source code, while the literal does not.

Example: the source `"Hello"` has the lexeme `"Hello"` and the literal `Hello`.

If the scanner reaches the end of the source without finding the closing quote, it reports an unterminated string error.

## Comments and Whitespace
Neon uses `//` for single-line comments. Everything after `//` on that line is ignored. Spaces and tabs are also ignored. New lines increase the line counter so errors can report where they happened.

## Tokens
Every Token stores four things: token type, lexeme, literal, and line number.

The token type says what was found. The lexeme is the exact source text. The literal is the actual value when there is one. The line number stores where the token came from.

## Differences From Lox
I made several changes from Lox. Neon has explicit integer types such as `i8`, `i16`, `i32`, `i64`, `u8`, `u16`, `u32`, and `u64`. It also has `char`, `bool`, and `string` type keywords.

Neon uses `&&` and `||` for AND and OR. I added `**` as a power operator and added `try`, `catch`, and `finally` as reserved keywords for possible future error handling. I also added square brackets and a dot token for syntax such as `console.write("Hello");`.

## Running Neon
Neon uses Python 3 and does not require any extra dependencies. Commands should be run from the main Neon directory.

Interactive mode:

`python3 -m src.main`

Type `exit` to close interactive mode.

To scan a file:

`python3 -m src.main <filename>`

Example:

`python3 -m src.main test/lab1/all_tokens.neon`

# Tests

## Test 1 - Basic Token
**Purpose:** Make sure a Token stores and prints its information correctly.  
**Expected:** A NUMBER token containing `"100"`, the value `100`, and line 1.  
**Actual:** `TokenType.NUMBER, 100, 100, 1`  
**Result:** PASS

## Test 2 - Scanner
**Purpose:** Test a small Neon program containing variables, numbers, an if statement, operators, a string, and `console.write`.  
**Expected:** The source should be separated into the correct tokens.  
**Actual:** The scanner correctly recognized tokens including `I32`, `IDENTIFIER`, `EQUAL`, `NUMBER`, `IF`, `LESS_EQUAL`, `AND`, `NOT_EQUAL`, `STRING`, `DOT`, and `SEMICOLON`.  
**Result:** PASS

## Test 3 - All Tokens
**Input:** `test/lab1/all_tokens.neon`  
**Purpose:** Test most of Neon's supported syntax in one file.  
**Expected:** Supported types, keywords, operators, punctuation, numbers, and strings should be recognized and the scanner should reach EOF.  
**Actual:** The scanner recognized the tested types, keywords, operators, strings, brackets, braces, parentheses, commas, dots, and semicolons. It ended with `TokenType.EOF, , None, 50`.  
**Result:** PASS

## Test 4 - Literals and Identifiers
**Input:** `test/lab1/literals.neon`  
**Purpose:** Test integers, decimals, strings, and different identifier formats.  
**Expected:** Each valid literal and identifier should be recognized.  
**Actual:** Integers and strings were recognized correctly. `99.5` was recognized as a NUMBER. `player_score`, `_privateValue`, and `player2` were all recognized as identifiers.  
**Result:** PASS

## Test 5 - Comments
**Input:** `test/lab1/comments.neon`  
**Purpose:** Make sure comments and whitespace are ignored.  
**Expected:** Comment text should not create tokens, while normal code should still scan correctly.  
**Actual:** The comments produced no tokens. Code on lines 3 and 7 was scanned correctly, showing that line tracking also continued through comments and whitespace.  
**Result:** PASS

## Test 6 - Unexpected Character
**Input:** `test/lab1/unexpected_character.neon`  
**Purpose:** Test a character that Neon does not recognize.  
**Expected:** Neon should report an error for `@` with its line number.  
**Actual:** `[line 2] Scanner error: Unexpected character '@'.` The scanner continued processing the valid source.  
**Result:** PASS

## Test 7 - Interactive Error Recovery
**Purpose:** Make sure interactive mode still works after an error.  
**Expected:** Invalid input should report an error without closing Neon.  
**Actual:** Entering `@` produced `[line 1] Scanner error: Unexpected character '@'.` A single `&` and `|` also gave useful errors suggesting `&&` and `||`. Neon stayed open after the errors. `/` was recognized as division while `//` was treated as a comment.  
**Result:** PASS

## Test 8 - Unterminated String
**Input:** `test/lab1/unterminated_string.neon`  
**Purpose:** Make sure a missing closing quote produces an error.  
**Expected:** Neon should report an unterminated string error with a line number.  
**Actual:** NOT TESTED YET  
**Result:** NOT TESTED

# Known Limitations
Neon currently only scans code and cannot parse or execute programs. Block comments, scientific notation, and string escape sequences are not supported. The `char` keyword exists, but separate single-quoted character literals are not implemented yet.