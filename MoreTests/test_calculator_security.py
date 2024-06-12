import unittest
import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator_gui import CalculatorApp

class TestCalculatorSecurity(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def test_code_injection(self):
        self.app.entry_value.set('__import__("os").system("echo vulnerable")')
        self.app.evaluate_expression()
        self.assertNotEqual(self.app.entry_value.get(), "vulnerable")
        self.assertEqual(self.app.entry_value.get(), "Error")

    def test_division_by_zero(self):
        self.app.entry_value.set('10/0')
        self.app.evaluate_expression()
        self.assertEqual(self.app.entry_value.get(), "Error")

    def test_invalid_input(self):
        self.app.entry_value.set('abc')
        self.app.evaluate_expression()
        self.assertEqual(self.app.entry_value.get(), "Error")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
