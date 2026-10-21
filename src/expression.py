class Literal:
    def __init__(self, value):
        self.value = value


class Unary:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right


class Binary:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Grouping:
    def __init__(self, expression):
        self.expression = expression

class Variable:
    def __init__(self, name):
        self.name = name

