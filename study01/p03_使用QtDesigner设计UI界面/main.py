# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: xugx.ai@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: main.py
@time: 3/21/2019 11:13 AM
"""

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow

from designer import *
#import *    导入所有的（嗯，几乎。。。[见下文（a）所有内容）来自当前模块下的指定模块。这允许使用导入模块中的各种对象（变量、类、方法…），而不必在它们前面加上模块名。
#通常是“everything”的简写的*
if __name__ == '__main__':
    '''
    主函数
    '''

    app = QApplication(sys.argv) # 创建app对象
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()   # 显示widget
    sys.exit(app.exec_())    # 进入事件循环