import unittest
import tkinter as tk
from calculator import Calculator  # Assuming you saved the GUI code as calculator.py

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.root = tk.Tk()
        self.calculator = Calculator(self.root)
        # Give the GUI time to initialize before testing
        self.root.update_idletasks()

    def tearDown(self):
        """Clean up after test methods."""
        self.root.destroy()

    def enter_expression(self, expression):
        """Helper function to enter an expression into the calculator."""
        for char in expression:
            if char.isdigit() or char in "+-*/.^":
                self.calculator.press_key(char)
            elif char == "√":
                self.calculator.square_root_op() # Special case for sqrt
            self.root.update_idletasks() # Update the GUI for each press

    def get_display_value(self):
        """Helper function to get the value displayed in the input field."""
        return self.calculator.input_text.get()

    def click_equals(self):
        """Helper function to click the equals button."""
        self.calculator.calculate()
        self.root.update_idletasks()

    def click_clear(self):
        """Helper function to click the clear button."""
        self.calculator.clear_field()
        self.root.update_idletasks()


    def test_addition(self):
        self.enter_expression("5+3")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 8.0)

    def test_subtraction(self):
        self.enter_expression("10-4")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 6.0)

    def test_multiplication(self):
        self.enter_expression("6*7")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 42.0)

    def test_division(self):
        self.enter_expression("20/5")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 4.0)

    def test_division_by_zero(self):
        self.enter_expression("10/0")
        self.click_equals()
        # Check if error message appears (adapt to your GUI)
        self.assertTrue("Error" in self.get_display_value() or "inf" in self.get_display_value(), "Division by zero error not handled")
        self.click_clear() #Clear display after the error

    def test_exponential(self):
        self.enter_expression("2^3")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 8.0)

    def test_square_root(self):
        self.enter_expression("16√")  # Enter number first, *then* square root
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 4.0)

    def test_square_root_negative(self):
        self.enter_expression("-4√")
        self.click_equals()
        self.assertTrue("Error" in self.get_display_value(), "Square root of negative number error not handled")
        self.click_clear()

    def test_negative_number_calculation(self):
        self.enter_expression("-5+10")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 5.0)

    def test_clear(self):
        self.enter_expression("123")
        self.click_clear()
        self.assertEqual(self.get_display_value(), "")

    def test_non_integer_calculation(self):
        self.enter_expression("2.5*4")
        self.click_equals()
        self.assertEqual(float(self.get_display_value()), 10.0)  # Or a similar expected value


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Add each test individually
    suite.addTest(TestCalculator('test_addition'))
    suite.addTest(TestCalculator('test_subtraction'))
    suite.addTest(TestCalculator('test_multiplication'))
    suite.addTest(TestCalculator('test_division'))
    suite.addTest(TestCalculator('test_division_by_zero'))
    suite.addTest(TestCalculator('test_exponential'))
    suite.addTest(TestCalculator('test_square_root'))
    suite.addTest(TestCalculator('test_square_root_negative'))
    suite.addTest(TestCalculator('test_negative_number_calculation'))
    suite.addTest(TestCalculator('test_clear'))
    suite.addTest(TestCalculator('test_non_integer_calculation'))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\nTest Results:")

    # Create a dictionary to store the test results
    test_results = {}
    for test_name in suite._tests: #Use _tests to access the list of tests
        test_results[str(test_name).split(' ')[0]] = "Passed"  # Initialize all to passed.

    # Overwrite the results with failures and errors from the result object
    for failure in result.failures:
        test_results[str(failure[0]).split(' ')[0]] = "Failed"
    for error in result.errors:
         test_results[str(error[0]).split(' ')[0]] = "Error"


    for test_name, test_result in test_results.items():
        print(f"{test_name}: {test_result}")

    print(f"\nTotal Tests: {result.testsRun}")
    print(f"Passed: {result.testsRun - len(result.errors) - len(result.failures)}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")