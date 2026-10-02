from src.scanner import Scanner

source = """
i32 health = 100;
i32 damage = 25;

if (health <= 50 && damage != 0) {
    console.write("Low health");
}

health = health - damage;
"""

scanner = Scanner(source)
tokens = scanner.scan_tokens()

for token in tokens:
    print(token)
