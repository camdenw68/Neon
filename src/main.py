import sys

from src.scanner import Scanner
from src.parser_1 import Parser, ParseError
from src.ast_printer import ASTPrinter

def run(source):
    scanner = Scanner(source)

    try:
        tokens = scanner.scan_tokens()

        if scanner.had_error:
            print("Scanning failed. Fix the lexical errors.")
            return False

        parser = Parser(tokens)
        expression = parser.parse()

        printer = ASTPrinter()
        print(printer.print(expression))
        return True

    except ParseError as error:
        print(error)
        return False

    except (ValueError, TypeError, IndexError) as error:
        print(f"Invalid input: {error}")
        return False


def run_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            source = file.read()

        if not run(source):
            sys.exit(1)

    except OSError as error:
        print(f"Error reading file '{path}': {error}")
        sys.exit(1)


def run_prompt():
    print("Neon Interactive Parser")
    print("Type 'exit' to quit.")

    while True:
        try:
            source = input("> ")

            if source.strip().lower() == "exit":
                break

            if not source.strip():
                continue

            run(source)

        except (EOFError, KeyboardInterrupt):
            print()
            break


def main():
    if len(sys.argv) > 2:
        print("Usage: python3 -m src.main [script]")
        sys.exit(1)

    if len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


if __name__ == "__main__":
    main()
