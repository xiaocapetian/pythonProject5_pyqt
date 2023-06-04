import sys
from PyQt5.QtWidgets import QApplication, QWidget#导入相应的包，我们用到了QApplication和QWidget

if __name__ == '__main__':

    # 创建app对象
    app = QApplication(sys.argv)

    # 创建widget对象
    w = QWidget()

    # 定制widget的大小
    w.resize(400, 300)

    # 移动到对应位置
    w.move(500, 250)

    # 设置窗口名称
    w.setWindowTitle('Hello PyQt5!')

    # 显示widget
    w.show()

    # 进入事件循环
    sys.exit(app.exec_())
