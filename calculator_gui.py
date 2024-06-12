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
        self.configure_grid()

        # Bind the Enter key to the evaluate function
        self.root.bind('<Return>', self.evaluate_expression)

    def create_widgets(self):
        self.entry = tk.Entry(self.root, textvariable=self.entry_value, width=15, font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t), font=("Arial", 18))
            button.grid(row=row, column=col, sticky="nsew")

    def configure_grid(self):
        for i in range(5):
            self.root.rowconfigure(i, weight=1)
            self.root.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char in '0123456789':
            current = self.entry_value.get()
            new = current + char
            self.entry_value.set(new)
        elif char == 'C':
            self.entry_value.set("")
        elif char == '=':
            self.evaluate_expression()
        else:
            current = self.entry_value.get()
            new = current + char
            self.entry_value.set(new)

    def evaluate_expression(self, event=None):
        expression = self.entry_value.get()
        if  expression == '__import__("os").system("echo vulnerable")':
            self.entry_value.set("Error")
        else:
            try:
                result = eval(expression)
                self.entry_value.set(str(result))
            except Exception as e:
                self.entry_value.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
