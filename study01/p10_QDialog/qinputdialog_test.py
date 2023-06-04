import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# 对话框是人机交互中最常用的一种方式。PyQt5中使用QDialog来表示对话框，它有几个常用的子类，QMessageBox、QFileDialog、QInputDialog、QFontDialog。

# QFileDialog 跳一个输入框       输入对话框，包含一个输入框和二个按钮

class DialogDemo(QMainWindow):
    
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("QInputDialog demo")
        self.resize(600, 400)
        
        self.button = QPushButton(self)
        self.button.setText("点击弹出QInputDialog")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        name, okPressed = QInputDialog.getText(self, "迷途小书童", "请输入你的大名:", QLineEdit.Normal, " ")  # QFileDialog输入对话框！
        if okPressed and name:
            print(f'Welcome {name}')
        else:
            QMessageBox.critical(self, "Error", "请输入大名并点击OK!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())