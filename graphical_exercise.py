import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Example')

        self.resize(270, 110)

        layout = QVBoxLayout()

        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
