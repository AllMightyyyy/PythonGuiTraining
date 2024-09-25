from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog

class ColorPickerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.pick_color_button = QPushButton("Pick a color", self)
        self.pick_color_button.clicked.connect(self.open_color_picker)

        self.layout.addWidget(self.pick_color_button)

        self.setLayout(self.layout)

    def open_color_picker(self):
        """Open the color picker dialog and change the background color."""
        color = QColorDialog.getColor()

        if color.isValid(): 
            self.setStyleSheet(f"background-color: {color.name()};")

if __name__ == "__main__":
    app = QApplication([])
    window = ColorPickerApp()
    window.setWindowTitle("color picker app")
    window.setFixedSize(300, 200)

    window.show()
    app.exec()