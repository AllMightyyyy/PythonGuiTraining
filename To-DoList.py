from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QMessageBox

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter a task to add")
        self.layout.addWidget(self.input_field)

        self.add_button = QPushButton("add task", self)
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        self.delete_button = QPushButton("delete task", self)
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)
    
    def add_task(self):
        """Add a new task to the tasks list."""
        task_text = self.input_field.text()

        if task_text.strip() == "":
            QMessageBox.warning(self, "Input Error", "Task cannot be empty")
        else:
            self.task_list.addItem(task_text)
            self.input_field.clear()

    def delete_task(self):
        """Delete the selected task from the task list."""
        selected_task = self.task_list.currentItem()

        if selected_task:
            self.task_list.takeItem(self.task_list.row(selected_task))
        else:
            QMessageBox.warning(self, "Selection Error", "No task selected")

if __name__ == "__main__":
    app = QApplication([])
    window = TodoApp()
    window.setWindowTitle("To-Do List")
    window.setFixedSize(300, 400)
    window.show()
    app.exec()