# from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit,QMessageBox

def handleCalc():
    print('统计按钮被点击了')
    info = textEdit.toPlainText()
    # info 取了读取的内容

    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                      )


app = QApplication([])
# QApplication 提供了整个图形界面程序的底层管理功能，比如：
#
# 初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…

window = QMainWindow()  # 定一个主窗口
window.resize(500, 400)  # 大小
window.move(300, 310)  # 位置（窗口在显示器的位置）
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)  # 在主窗口上有一个副窗口
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCalc)
# 点击的信号连到handleCalc（槽函数）上

window.show()

app.exec_()  # 进入循环（否则一闪而过就退出了，等待用户
