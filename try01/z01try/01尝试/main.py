from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.show_cv_image()
    def initUI(self):
        self.setGeometry(500, 500, 500, 550)
        self.setWindowTitle('输液干预血钠预测')

        self.lb1 = QLabel('晶体输液：', self)
        self.lb1.move(20, 20)

        self.lb2 = QLabel('胶体输液：', self)
        self.lb2.move(20, 80)



        self.lb6 = QLabel('1000', self)
        self.lb6.move(120, 20)

        self.lb7 = QLabel('1000', self)
        self.lb7.move(120, 80)



        self.bt1 = QPushButton('修改晶体输液', self)
        self.bt1.move(200, 20)

        self.bt2 = QPushButton('修改胶体输液', self)
        self.bt2.move(200, 80)

        #self.main_layout = QtWidgets.QHBoxLayout()
        #self.label_image = QtWidgets.QLabel()
        #self.main_layout.addWidget(self.label_image)
        #self.setLayout(self.main_layout)

        self.show()

        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)


    def showDialog(self):
        sender = self.sender()

        if sender == self.bt1:
            text, ok = QInputDialog.getInt(self, '修改晶体输液', '请输入晶体输液量：', min=0, step=50)
            if ok:
                self.lb6.setText(str(text))
        elif sender == self.bt2:
            text, ok = QInputDialog.getInt(self, '修改胶体体输液', '请输入胶体输液量：', min=0, step=50)
            if ok:
                self.lb7.setText(str(text))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())