# user_interface_pyqt.py
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
# import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Onder First')

        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)


class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.text_label = QLabel()
        self.text_label.setText('Onder')
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)

        self.top_button = QPushButton('Top')
        self.top_button.clicked.connect(lambda: self.button_clicked('Top button'))

        self.bottom_button = QPushButton()
        self.bottom_button.setText('Bottom')
        self.bottom_button.clicked.connect(lambda: self.button_clicked('Bottom button'))
        # self.bottom_button.resize(100, 100)
        # self.bottom_button.move(100, 100)

        self.layout.addWidget(self.top_button)
        self.layout.addWidget(self.bottom_button)
        self.layout.addWidget(self.text_label)

        self.setLayout(self.layout)

    def button_clicked(self, text):
        self.text_label.setText(f'You clicked {text}!')


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
