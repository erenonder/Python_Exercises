# tic_tac_toe.py

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
# import time
import threading
from PyQt5.QtMultimedia import QSound
import logging
from tictactoe_ui import Ui_tictactoe


class Game(QMainWindow, Ui_tictactoe):
    sleep_time_seconds = 0.5
    reset_game_time = 2.0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.player = "Player1"

        self.button_val_list = []

        self.sounds = dict(circle=QSound("Sounds/circle.wav"),
                           cross=QSound("Sounds/cross.wav"),
                           win=QSound("Sounds/win.wav"),
                           lose=QSound("Sounds/lose.wav"))
        self.set_log_properties()

        self.logger.info(self.sounds)

        for i in range(9):
            self.button_val_list.append(i)

        self.allButtons = self.frame.findChildren(QToolButton)

        self.actionNew_Game.triggered.connect(self.reset_game)
        # self.actionDark_Theme.toggled.connect(self.dark_theme)
        self.action_Exit.triggered.connect(self.close)

        xIconPath = os.path.join("Icons", "x.png")
        oIconPath = os.path.join("Icons", "o.png")

        self.xIcon = QIcon(xIconPath)
        self.oIcon = QIcon(oIconPath)

        self.xIcon.addPixmap(QPixmap(xIconPath), QIcon.Disabled)
        self.oIcon.addPixmap(QPixmap(oIconPath), QIcon.Disabled)

        for button in self.allButtons:
            button.pressed.connect(self.button_clicked)

    def set_log_properties(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.WARNING)
        file_handler = logging.FileHandler(filename='game_log.log')
        formatter = logging.Formatter(fmt='%(asctime)s %(name)s %(lineno)s %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def button_clicked(self):
        button = self.sender()
        self.logger.info(f"button clicked {button}")
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

        self.logger.debug(button_index)

        self.check_game(button_index, button_value)

    def check_game(self, button_index, button_value):
        self.button_val_list[button_index] = button_value
        self.logger.info(self.button_val_list)

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
            for check in self.button_val_list:
                if check != 'x' and check != 'o':
                    if self.player == "Player1":
                        self.sounds["cross"].play()
                        self.player = "Player2"
                    else:
                        self.sounds["circle"].play()
                        self.player = "Player1"
                    break
            else:
                self.logger.info('DRAW')
                self.sounds["lose"].play()
                reset_game_thread = threading.Timer(self.reset_game_time, self.reset_game)
                reset_game_thread.start()

    def disable_button(self):
        self.logger.info("disable now")
        self.button_to_disable.setEnabled(False)

    def end_game(self):
        self.sounds["win"].play()
        self.logger.info(f'Game Over {self.player} wins')
        reset_game_thread = threading.Timer(self.reset_game_time, self.reset_game)
        reset_game_thread.start()

    def reset_game(self):

        self.player = "Player1"

        self.button_val_list = []

        for i in range(9):
            self.button_val_list.append(i)

        for button in self.allButtons:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(True)

    def show_winner(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f'Game Over {self.player} wins')

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.reset_game()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    app.exec_()
