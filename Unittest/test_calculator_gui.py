import unittest
import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    def test_clear(self):
        self.app.on_button_click('1')
        self.app.on_button_click('C')
        self.assertEqual(self.app.entry_value.get(), '')

    def test_evaluate_expression(self):
        self.app.on_button_click('2')
        self.app.on_button_click('+')
        self.app.on_button_click('2')
        self.app.on_button_click('=')
        self.assertEqual(self.app.entry_value.get(), '4')

    # def test_evaluate_expression_with_enter_key(self):
    #     self.app.entry_value.set('2+2')
    #     self.app.root.event_generate('<Return>')
    #     self.root.update()  
    #     self.assertEqual(self.app.entry_value.get(), '4')

    #     self.app.entry_value.set('2*3')
    #     self.app.root.event_generate('<Return>')
    #     self.root.update()  
    #     self.assertEqual(self.app.entry_value.get(), '6')

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
