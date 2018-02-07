from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QTextEdit,
                             QFileDialog, QDialog, QAction, QMainWindow, QTabWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QInputDialog,
                             QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
import numpy as np

def t_k(X):
    N = X.size
    k = N-1
    t = 0.96+0.83/k
    return t

def S_xi(X):
    N=X.size
    x_mean=X.mean()
    v=0
    for i in range(0,N):
       v+=abs((X[i]-x_mean)**2)
    S_i=np.sqrt(v/(N-1))
    return S_i

def S_mean(X):
    N=X.size
    return S_xi(X)/np.sqrt(N)

def u_a(X):
    return t_k(X)*S_mean(X)



class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        noteAction = QAction("说明", self)
        noteAction.triggered.connect(self.showdialog)

        menubar = self.menuBar()
        menubar.addAction(noteAction)

        self.setWindowTitle("不确定度计算器")
        self.setWindowIcon(QIcon("doge.jpg"))
        self.setGeometry(400, 200, 500, 400)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    def showdialog(self):
        dialog_text = ("谢谢使用我的计算器！\n" +
                    "本品只是半成品，只能计算A类不确定度，无法计算合成不确定度。\n" +
                       "单位、有效数字啥的得靠你自己了。\n" +
                       "\n\nHave Fun!")
        QMessageBox.question(self, "说明", dialog_text, QMessageBox.Ok, QMessageBox.Ok)


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Initialize tab screen
        self.layout = QGridLayout(self)
        self.table = self.creatTable()
        self.layout.addWidget(self.table, 1, 0)

        spacetext = 40 * " "
        self.message = QLabel(spacetext, self)

        # Add Button
        self.calButton = QPushButton("计算")
        self.calButton.clicked.connect(self.calbuttonClicked)
        self.layout.addWidget(self.calButton, 2, 0)

        self.layout.addWidget(self.message, 1, 1)

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

    def calbuttonClicked(self):
        Items = []
        data = []
        for i in range(15):
            Item = self.table.item(i, 0)
            Items.append(Item)
        for Item in Items:
            if Item.text():
                data.append(np.double(Item.text()))
        data = np.array(data)
        Sxi = S_xi(data)
        Smean = S_mean(data)
        ua = u_a(data)
        s = 2*'\n'
        self.message.setText("  数据的平均值为： " + str(data.mean()) + s +
                             "  S_xi的值为： " + str(Sxi) + s +
                             "  S_x_mean的值为： " + str(Smean) + s +
                             "  第一类不确定度的值为： " + str(ua) + '\n' +
                             40 * ' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
