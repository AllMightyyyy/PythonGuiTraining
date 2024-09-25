from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.userName = QLineEdit(self)
        self.passWord = QLineEdit(self)

        self.userName.setPlaceholderText("enter your username here")
        self.passWord.setPlaceholderText("enter your password here")
        self.passWord.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)

        self.login_result = QLabel("", self)

        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.userName)
        layout.addWidget(self.passWord)
        layout.addWidget(self.login_button)
        layout.addWidget(self.login_result)

        self.setLayout(layout)

    def login(self):
        username = self.userName.text()
        passWord = self.passWord.text()

        if ( username == "admin" ) and ( passWord == "password" ) :
            self.login_result.setText("Login successful")
        else :
            self.login_result.setText("Login Failed") 

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setFixedSize(200, 100)
    window.show()
    app.exec()
