import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# 对话框是人机交互中最常用的一种方式。PyQt5中使用QDialog来表示对话框，它有几个常用的子类，QMessageBox、QFileDialog、QInputDialog、QFontDialog。

# 首先是  QDialog
# 简简单单打开一个对话框
class DialogDemo(QMainWindow):
    
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("Dialog demo")
        self.resize(600, 400)
        
        self.button = QPushButton(self)
        self.button.setText("点击弹出对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)
        
    def showDialog(self):
        dialog = QDialog()  # QDialog类！
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        # Qt.WindowModal
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())