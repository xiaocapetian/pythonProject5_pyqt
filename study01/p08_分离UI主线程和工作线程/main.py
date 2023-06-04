# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: djstava@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: main.py
@time: 2019/1/10 10:50
"""
# 这一节讲 分离UI主线程 与 耗时线程
# main0是没有分离的，用户体验差
# main里，把耗时的time.sleep(5)从mainwindow分离
import sys

from PyQt5.QtWidgets import QApplication

from gui.mainwindow import MainWindow

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())