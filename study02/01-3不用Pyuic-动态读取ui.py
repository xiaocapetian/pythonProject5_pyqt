from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Stats:
    def __init__(self):
        # self.ui = QUiLoader().load('ui/01_3.ui')
        qfile_stats = QFile("ui/01_3.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意:里面的控件对象也成为窗口对象的属性了
        # 如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)
        # 这里的ui是一个QWidget类的实例对象
        # 那么ui下有什么，在qtdesign里也是能找到的
        # 这个self.ui.pushButton和plainTextEdit是ui文件里写的名字
        self.ui.pushButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.plainTextEdit.toPlainText()
        # print(info)
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

        QMessageBox.about(self.ui,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
