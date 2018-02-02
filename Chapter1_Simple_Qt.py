import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')  # "setToolTip()" 设置鼠标悬停时的提示

        btn = QPushButton('Button', self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())  # "sizeHint()" gives a recommended size
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip("Push this bottom to <b>QUIT</b>")
        qbtn.clicked.connect(QApplication.instance().quit)  # "clicked" is the event, "instance()" handle all process
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)

        # self.setGeometry(300, 300, 300, 200) 用setGeometry可同时设置位置与大小（前两参数为位置，后两为大小）
        self.setWindowTitle("First Chapter")
        self.setWindowIcon(QIcon("doge.jpg"))
        self.show()

# 此函数为右上角关闭时的确认对话框.该函数是父类QWidget中做好定义的，注意拼写必须如此。
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',                            # 变量依次为：title，# 内容，选项，默认选项
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

