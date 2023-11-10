import unittest
from math_quiz import generate_random_no, select_operator, calculate


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the returned value is one of the expected operators
        operators = set(['+', '-', '*'])
        result = select_operator()
        self.assertIn(result, operators)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '*', '8 * 3', 24),
                (10, 2, '-', '10 - 2', 8),
                (1, 5, '+', '1 + 5', 6),
                (9, 4, '-', '9 - 4', 5 ),
                (7, 1, '*', '7 * 1', 7),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result = calculate(num1, num2, operator)
                self.assertEqual(result[0], expected_problem)  # Check the generated problem
                self.assertEqual(result[1], expected_answer)   # Check the expected answer

if __name__ == "__main__":
    unittest.main()
