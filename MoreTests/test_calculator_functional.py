import unittest
import sys
import os
import tkinter as tk

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator_gui import CalculatorApp

class TestCalculatorFunctional(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def test_addition(self):
        self.app.on_button_click('2')
        self.app.on_button_click('+')
        self.app.on_button_click('3')
        self.app.on_button_click('=')
        self.assertEqual(self.app.entry_value.get(), '5')

    def test_subtraction(self):
        self.app.on_button_click('5')
        self.app.on_button_click('-')
        self.app.on_button_click('3')
        self.app.on_button_click('=')
        self.assertEqual(self.app.entry_value.get(), '2')

    def test_multiplication(self):
        self.app.on_button_click('4')
        self.app.on_button_click('*')
        self.app.on_button_click('3')
        self.app.on_button_click('=')
        self.assertEqual(self.app.entry_value.get(), '12')

    def test_division(self):
        self.app.on_button_click('9')
        self.app.on_button_click('/')
        self.app.on_button_click('3')
        self.app.on_button_click('=')
        self.assertEqual(self.app.entry_value.get(), '3.0')

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
