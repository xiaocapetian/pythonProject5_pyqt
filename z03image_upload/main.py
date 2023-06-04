from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
import sys
import ui_registration
from onepicture import path_to_img_flu, path_to_img_mix
import numpy as np


class Maincode(QMainWindow, ui_registration.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        super(Maincode, self).__init__(self)
        ui_registration.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.flu_pushButton.clicked.connect(self.on_open_vis)  # 手动连接槽
        self.mix_pushButton.clicked.connect(self.on_open_infr)
        self.CNN_registration.clicked.connect(self.cnngetresult)

    #img_flu = np.empty((1, 80, 80, 3))

    def on_open_vis(self):  # 槽函数编写
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片flu", "", "*.jpg;;*.png;;All Files(*)")
        # imgName = D:/PycharmProjects/pythonProject5_pyqt/z03image_upload/tree.jpg
        # imgType = *.jpg
        jpg = QtGui.QPixmap(imgName).scaled(self.vis_view.width(), self.vis_view.height())
        self.vis_view.setPixmap(jpg)
        global img_flu
        img_flu = path_to_img_flu(imgName)
        # print(img_flu.shape)
        print(img_flu)

    def on_open_infr(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片mix", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.infr_view.width(), self.infr_view.height())
        self.infr_view.setPixmap(jpg)
        global img_mix
        img_mix = path_to_img_mix(imgName)

    def cnngetresult(self):
        print(img_flu)
        #pass

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 实例化一个应用对象
    md = Maincode()
    md.show()
    sys.exit(app.exec_())
