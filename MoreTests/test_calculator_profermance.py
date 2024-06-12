import timeit
import sys
import os
import tkinter as tk
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator_gui import CalculatorApp

class TestCalculatorPerformance(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)

    def test_evaluate_expression_performance(self):
        expression = "2+2*3-5/2"

        time_taken = timeit.timeit(lambda: self.app.evaluate_expression(expression), number=1000)

        print("Average time taken to evaluate expression:", time_taken / 1000, "seconds")

if __name__ == '__main__':
    unittest.main()
