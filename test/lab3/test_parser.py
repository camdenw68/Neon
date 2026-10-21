
import io
import unittest
from contextlib import redirect_stdout

from src.main import run


class TestNeonParser(unittest.TestCase):

    # start ai generated 
    def check_expression(self, source, expected):
        output = io.StringIO()

        with redirect_stdout(output):
            success = run(source)

        self.assertTrue(success)
        self.assertEqual(output.getvalue().strip(), expected)

    def check_error(self, source):
        output = io.StringIO()

        with redirect_stdout(output):
            success = run(source)

        self.assertFalse(success)
        self.assertTrue(output.getvalue().strip())
        self.assertNotIn("Traceback", output.getvalue())

    # end ai generated
    def test_literals(self):
        self.check_expression("42", "42")
        self.check_expression("3.5", "3.5")
        self.check_expression('"hello"', "hello")

    def test_arithmetic(self):
        self.check_expression(
            "10 + 5 * 2",
            "(+ 10 (* 5 2))"
        )
        self.check_expression(
            "10 % 3",
            "(% 10 3)"
        )

    def test_grouping(self):
        self.check_expression(
            "(10 + 5) * 2",
            "(* (group (+ 10 5)) 2)"
        )

    def test_associativity(self):
        self.check_expression(
            "10 - 5 - 2",
            "(- (- 10 5) 2)"
        )

    def test_unary(self):
        self.check_expression(
            "-5 + 10",
            "(+ (- 5) 10)"
        )

    def test_comparison(self):
        self.check_expression(
            "10 >= 5",
            "(>= 10 5)"
        )

    def test_equality(self):
        self.check_expression(
            "5 == 5",
            "(== 5 5)"
        )

    def test_variables(self):
        self.check_expression(
            "score + 5",
            "(+ score 5)"
        )

    def test_errors(self):
        for source in [
            "10 +",
            "(10 + 5",
            "10 + * 5",
            "10 20",
            "* 5",
            "()"
        ]:
            with self.subTest(source=source):
                self.check_error(source)

    def test_boolean_and_null(self):
        self.check_expression("true", "true")
        self.check_expression("false", "false")
        self.check_expression("null", "null")

    def test_recovery(self):
        self.check_error("10 +")
        self.check_expression(
            "10 + 5",
            "(+ 10 5)"
        )


if __name__ == "__main__":
    unittest.main()

