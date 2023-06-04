"""
@author: Xu Gaoxiang
@license: Apache V2
@email: xugx.ai@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: mainwindow.py
@time: 2019/1/10 10:49
"""

import time

from PyQt5.QtWidgets import QMainWindow

from gui.ui_mainwindow import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定点击事件
        self.button_ok.clicked.connect(self.button_start)

    def button_start(self):  #点击事件

        self.button_ok.setChecked(True)
        self.button_ok.setDisabled(True)

        time.sleep(5)