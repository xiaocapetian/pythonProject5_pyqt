import sys

from PyQt5.QtWidgets import QApplication

from gui.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 首先来到工程的入口函数main.py，初始化app并进入事件循环
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
