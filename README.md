# Calculator App

A simple calculator application built with Python's Tkinter GUI library.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Code Examples](#code-examples)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Calculator App is a simple desktop application that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The application provides a user-friendly graphical interface built with Tkinter, ensuring ease of use.

## Installation

To install and run the Calculator App, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/calculator-app.git
   ```

2. Navigate to the project directory:

   ```
   cd calculator-app
   ```

3. Install the required dependencies (if any):

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python calculator_gui.py
   ```

## Usage

Upon launching the application, you will see a simple calculator interface. You can perform arithmetic operations by clicking the number and operator buttons, and the result will be displayed in the entry field. The application supports the following operations:

- Addition
- Subtraction
- Multiplication
- Division

To perform a calculation, follow these steps:

1. Click the number buttons to enter the first operand.
2. Click the desired operator button (+, -, *, /).
3. Click the number buttons to enter the second operand.
4. Click the equals (=) button to evaluate the expression and display the result.

The clear (C) button can be used to clear the entry field and start a new calculation.

## API Documentation

The Calculator App does not provide an API for external usage. It is a standalone desktop application.

## Code Examples

Here is an example of how to use the `calculator_functions` module:

```python
from calculator_functions import add, subtract, multiply, divide

result = add(2, 3)  # result = 5
result = subtract(10, 4)  # result = 6
result = multiply(5, 6)  # result = 30
result = divide(15, 3)  # result = 5.0
```

## Tests

The Calculator App includes several test suites to ensure the correctness and reliability of the application. The test suites cover functional, security, and performance aspects of the calculator.

### Running Tests

To run the tests, navigate to the project directory and execute the following commands:

#### Functional Tests

```
python test_calculator_functional.py
```

#### Security Tests

```
python test_calculator_security.py
```

#### Performance Tests

```
python test_calculator_performance.py
```

## Contributing

Contributions to the Calculator App are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Tkinter library for providing a cross-platform GUI toolkit for Python.
- The Python community for their valuable resources and contributions.
