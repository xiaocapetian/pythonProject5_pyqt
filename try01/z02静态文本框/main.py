import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit
class QTLineEditExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):                                # 初始化用户界面
        self.label_obj1 = QLabel(self)                # 静态标签
        self.label_obj1.setText(u"静态文本框在这里")
        self.label_obj1.move(60, 40)

        self.line_edit_obj1 = QLineEdit(self)        # 单行编辑框               QLineEdit单行输入！！！
        self.line_edit_obj1.move(60, 100)

        self.line_edit_obj1.textChanged[str].connect(self.onChanged)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle(u'演示QLineEdit的用法')
        self.show()
    def onChanged(self, text):
        self.label_obj1.setText(text)
        self.label_obj1.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTLineEditExample()
    sys.exit(app.exec_())