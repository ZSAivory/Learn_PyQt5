from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QTextEdit,
                             QFileDialog, QDialog, QAction, QMainWindow, QTabWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog,
                             QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        newAction = QAction("新建", self)
        newAction.setShortcut("Ctrl+N")
        newAction.triggered.connect(self.getInteger)
        # 新建的事件还没写

        importAction = QAction("导入", self)
        importAction.setShortcut("Ctrl+I")
        importAction.triggered.connect(self.openfile)

        helpAction = QAction("帮助", self)
        helpAction.triggered.connect(self.showhelp)

        authorAction = QAction("开发者", self)
        authorAction.triggered.connect(self.showauthor)

        menubar = self.menuBar()
        filemenu = menubar.addMenu("文件")
        filemenu.addAction(newAction)
        filemenu.addAction(importAction)
        menubar.addAction(helpAction)
        menubar.addAction(authorAction)

        self.setWindowTitle("不确定度计算器")
        self.setWindowIcon(QIcon("doge.jpg"))
        self.setGeometry(400, 200, 500, 400)
        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, "浏览", './')
        # print(fname)
        if fname[0]:
            with open(fname[0], 'r', encoding='gb18030', errors='ignore') as f:
                ()

    def getInteger(self):
        i, okpress = QInputDialog.getInt(self, '新建选项',
                                        '输入实验的变量个数:', 1, 1, 10)
        if okpress:
            self.var_num = i

            self.table_widget = MyTableWidget(self, self.var_num)
            self.setCentralWidget(self.table_widget)

    def showhelp(self):
        helptext = "谢谢使用。。。。。"

    def showauthor(self):
        authortext = "sss"


class MyTableWidget(QWidget):
    def __init__(self, parent, n):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.n = n

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab = []
        for i in range(n):
            message = QLabel("输入数据后点击计算按钮", self)
            self.tab.append(QWidget())
            layout = QGridLayout()
            layout.addWidget(self.creatTable(), 1, 0)
            layout.addWidget(message, 1, 1)
            self.tab[i].setLayout(layout)

        # Add tabs
        for i in range(n):

            self.tabs.addTab(self.tab[i], "变量"+str(i+1))

        # Add Button
        self.calButton = QPushButton("计算")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.calButton)
        self.setLayout(self.layout)

    def creatTable(self):
        table = QTableWidget()
        table.setRowCount(15)
        table.setColumnCount(1)
        for j in range(15):
            newItem = QTableWidgetItem("")
            newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table.setItem(j, 0, newItem)
            table.setRowHeight(j, 23)
        table.setHorizontalHeaderLabels(["数据"])
        return table


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
