import sys
from src.scanner import Scanner


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_file(path):
    try:
        with open(path, "r") as file:
            source = file.read()

        run(source)

    except FileNotFoundError:
        print(f"Error: Could not find file '{path}'.")
        sys.exit(1)


def run_prompt():
    print("Neon Interactive Scanner")
    print("Type 'exit' to quit.")

    while True:
        try:
            source = input("> ")

            if source == "exit":
                break

            run(source)

        except EOFError:
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
