# tic_tac_toe.py

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import time
import threading
from PyQt5.QtMultimedia import QSound

# from Dialog import *
from tictactoe_ui import Ui_tictactoe


class Game(QMainWindow, Ui_tictactoe):
    sleep_time_seconds = 0.5

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.player = "Player1"

        self.button_val_list = []

        self.sounds = dict(circle=QSound("circle.wav"),
                           cross=QSound("cross.wav"),
                           win=QSound("win.wav"),
                           lose=QSound("lose.wav"))

        # print(self.sounds)

        for i in range(9):
            self.button_val_list.append(i)

        self.allButtons = self.frame.findChildren(QToolButton)

        xIconPath = os.path.join("Icons", "x.png")
        oIconPath = os.path.join("Icons", "o.png")

        self.xIcon = QIcon(xIconPath)
        self.oIcon = QIcon(oIconPath)

        self.xIcon.addPixmap(QPixmap(xIconPath), QIcon.Disabled)
        self.oIcon.addPixmap(QPixmap(oIconPath), QIcon.Disabled)

        for button in self.allButtons:
            button.pressed.connect(self.button_clicked)

    def button_clicked(self):
        button = self.sender()
        # print(f"button clicked {button}")
        # button.setText("1")
        if self.player == "Player1":
            button.setIcon(self.xIcon)
            button_value = 'x'
        else:
            button.setIcon(self.oIcon)
            button_value = 'o'

        self.button_to_disable = button
        disable_button_thread = threading.Timer(self.sleep_time_seconds, self.disable_button)
        disable_button_thread.start()

        button_index = int(button.objectName()[6]) - 1

        # print(button_name[6])

        self.check_game(button_index, button_value)

    def check_game(self, button_index, button_value):
        self.button_val_list[button_index] = button_value
        print(self.button_val_list)

        horizontal_check = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        vertical_check = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        corss_check = [[0, 4, 8], [2, 4, 6]]

        winner = False
        for hor in horizontal_check:
            if self.button_val_list[hor[0]] == self.button_val_list[hor[1]] and self.button_val_list[hor[1]] == self.button_val_list[hor[2]]:
                winner = True

        if not winner:
            for hor in vertical_check:
                if self.button_val_list[hor[0]] == self.button_val_list[hor[1]] and self.button_val_list[hor[1]] == self.button_val_list[hor[2]]:
                    winner = True

        if not winner:
            for hor in corss_check:
                if self.button_val_list[hor[0]] == self.button_val_list[hor[1]] and self.button_val_list[hor[1]] == self.button_val_list[hor[2]]:
                    winner = True

        if winner:
            self.end_game()
        else:
            if self.player == "Player1":
                self.player = "Player2"
            else:
                self.player = "Player1"

    def disable_button(self):
        # print("disable now")
        self.button_to_disable.setEnabled(False)

    def end_game(self):
        self.sounds["win"].play()
        time.sleep(3)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f'Game Over {self.player} wins')

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.reset_game()

    def reset_game(self):

        self.player = "Player1"

        self.button_val_list = []

        for i in range(9):
            self.button_val_list.append(i)

        for button in self.allButtons:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    app.exec_()
