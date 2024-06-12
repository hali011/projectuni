# calculator_gui.py

import tkinter as tk
from calculator_functions import add, subtract, multiply, divide

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.total = 0
        self.entered_number = 0

        self.entry_value = tk.StringVar(root, value="")
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.entry_value, width=15)
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char in '0123456789':
            current = self.entry_value.get()
            new = current + char
            self.entry_value.set(new)
        elif char == 'C':
            self.entry_value.set("")
        elif char == '=':
            expression = self.entry_value.get()
            self.entry_value.set(str(eval(expression)))
        else:
            current = self.entry_value.get()
            new = current + char
            self.entry_value.set(new)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
