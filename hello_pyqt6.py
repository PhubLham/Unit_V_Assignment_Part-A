import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class HelloWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World - Phub Lham")
        self.resize(350, 200)

        self.label = QLabel("Welcome! Click the button below.")
        button = QPushButton("Click Me")

        button.clicked.connect(self.show_message)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(button)

    def show_message(self):
        self.label.setText("Hello! You clicked the button.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    sys.exit(app.exec())