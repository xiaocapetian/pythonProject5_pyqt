# -*- coding: utf-8 -*-

# 我们将UI主线程中的time.sleep(20)移动到子线程中就可以了。PyQt5中提供了线程类QThread，我们继承它并重写它的run方法，新建一个新的文件threads.py
"""
@author: Xu Gaoxiang
@license: Apache V2
@email: djstava@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: mainwindow.py
@time: 2019/1/10 10:49
"""

from PyQt5.QtWidgets import QMainWindow

from gui.ui_mainwindow import *  # mainwindow 要引 ui_mainwindow 里的东西
from .threads import WorkThread
# PyQt5中提供了线程类QThread
# QThread是Qt线程类中最核心的底层类。要使用QThread开始一个线程，必须创建一个QThread的子类，然后重写QThread.run方法。
# 如 class Worker(QThread):  # 定义了一个Worker，继承自QThread
# 在使用线程时，可以直接得到Thread实例，调用其start()方法即可启动线程。

""" 一般来讲，业务的线程任务就放在run方法中，当run退出之后，线程就结束了。 """
# WorkThread 所以说，任务要写在有class WorkThread的thread那里找
# QThread有started和finished信号，可以为这两个信号绑定相应的槽函数，在线程启动启动和结束时执行一些代码来记性资源的初始化和释放的动作。


class MainWindow(QMainWindow, Ui_MainWindow):
    # MainWindow类 要有两个输入，
    # 一个是PyQt5.QtWidgets里的QMainWindow，
    # 另外一个是ui_mainwindow里的类Ui_MainWindow

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_ok.clicked.connect(self.button_start)

    def button_start(self):
        print('button_start clicked.')

        self.button_ok.setChecked(True)
        self.button_ok.setDisabled(True)
# QThread有started和finished信号，可以为这两个信号绑定相应的槽函数，在线程启动启动和结束时执行一些代码来记性资源的初始化和释放的动作。
        self.th = WorkThread(ip='192.168.1.1', port=4000)   # WorkThread
        self.th.finishSignal.connect(self.button_finish) # finishSignal信号connect函数  button_finish
        self.th.start()

    def button_finish(self, msg):
        print('msg: {}'.format(msg))

        self.button_ok.setChecked(False)
        self.button_ok.setDisabled(False)
