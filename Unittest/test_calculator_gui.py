# test_calculator_gui.py

import unittest
import tkinter as tk
from calculator_gui import CalculatorApp

class TestCalculatorGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def test_initial_value(self):
        self.assertEqual(self.app.entry_value.get(), "")

    def test_button_click(self):
        self.app.on_button_click('1')
        self.assertEqual(self.app.entry_value.get(), '1')
        self.app.on_button_click('2')
        self.assertEqual(self.app.entry_value.get(), '12')

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
