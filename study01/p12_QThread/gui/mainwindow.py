import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from .ui_mainwindow import Ui_MainWindow  # mainwindow 要引 ui_mainwindow 里的东西————一个类Ui_MainWindow
# ui_mainwindow.py由qtdesinger自动生成，里面就一个类，叫Ui_MainWindow，这个类有两个函数  setupUi和 retranslateUi

class MainWindow(QMainWindow, Ui_MainWindow):
    #  mainwindow文件里有一个MainWindow类
    #  MainWindow类 要有两个输入，
    # 一个是PyQt5.QtWidgets 里的 QMainWindow，
    # 另外一个是 ui_mainwindow 里的类Ui_MainWindow
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.thread = Worker()
        self.thread.sig.connect(self.updateLabel)
        """！信号connect 函数！"""
        
        self.pushButton.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        self.thread.start()
    
    def updateLabel(self, text):
        self.label.setText(text)

# QThread是Qt线程类中最核心的底层类。要使用QThread开始一个线程，必须创建一个QThread的子类，然后重写QThread.run方法。
# 在使用线程时，可以直接得到Thread实例，调用其start()方法即可启动线程。

class Worker(QThread):
    # 定义了一个Worker，继承自QThread
    sig = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.count = 0
    
    def run(self):
        
        while True:
            time.sleep(1)
            self.count += 1
            if (self.count % 5 == 0):
                self.sig.emit(f"已执行{self.count}秒")
