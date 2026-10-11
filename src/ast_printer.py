
from expression import Literal, Unary, Binary, Grouping

class ASTPrinter:
    def print(self, expression):
        if isinstance(expression, Literal):
            if expression.value is None:
                return "nil"
            if expression.value is True:
                return "true"
            if expression.value is False:
                return "false"
            return str(expression.value)

        elif isinstance(expression, Unary):
            return self.parenthesize(
                expression.operator.lexeme,
                expression.right
            )

        elif isinstance(expression, Binary):
            return self.parenthesize(
                expression.operator.lexeme,
                expression.left,
                expression.right
            )

        elif isinstance(expression, Grouping):
            return self.parenthesize(
                "group",
                expression.expression
            )

        else:
            raise ValueError("Unknown expression type")

    def parenthesize(self, name, *expressions):
        result = "(" + name

        for expression in expressions:
            result += " " + self.print(expression)

        result += ")"
        return result