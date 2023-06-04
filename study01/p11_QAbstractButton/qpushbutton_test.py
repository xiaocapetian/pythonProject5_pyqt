import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QPushButton, QApplication

# QPushButton是最常见的按钮，它的形状是长方形的
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        pb = QPushButton('PushButton', self)
        pb.move(50, 50)
        pb.clicked.connect(self.buttonClicked)
        
        self.setWindowTitle('PushButton')
        self.show()
    
    def buttonClicked(self):
        print('Button is clicked.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
