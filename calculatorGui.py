from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.first_number_field = QLineEdit(self)
        self.second_number_field = QLineEdit(self)

        self.add_button = QPushButton("Add", self)
        self.substract_button = QPushButton("Substract", self)
        self.multiplication_button = QPushButton("Multiply", self)
        self.division_button = QPushButton("Division", self)

        self.result = QLabel(self)

        self.result.setText("result")
        self.first_number_field.setPlaceholderText("enter first number here")
        self.second_number_field.setPlaceholderText("enter second number here")

        self.add_button.clicked.connect(self.add)
        self.substract_button.clicked.connect(self.substract)
        self.multiplication_button.clicked.connect(self.multiply)
        self.division_button.clicked.connect(self.divide)

        layout = QVBoxLayout()

        layout.addWidget(self.first_number_field)
        layout.addWidget(self.second_number_field)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.substract_button)
        button_layout.addWidget(self.multiplication_button)
        button_layout.addWidget(self.division_button)

        layout.addLayout(button_layout)

        layout.addWidget(self.result)

        self.setLayout(layout)

    def get_numbers(self):
        """Utility method to get numbers from the input fields."""
        try: 
            num1 = float(self.first_number_field.text())
            num2 = float (self.second_number_field.text())
            return num1, num2
        except ValueError:
            self.result.setText("Error: Please enter valid numbers")
            return None, None
    
    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result.setText(f"Result: {result}")

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result.setText(f"Result: {result}")
    
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                result = num1 / num2
                self.result.setText(f"Result: {result}")
            else: 
                self.result.setText("Error: cannot divide by 0")

    def substract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result.setText(f"Result: {result}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Simple Calculator")
    window.setFixedSize(300, 200)
    window.show()
    app.exec()