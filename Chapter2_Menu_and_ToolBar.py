import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.statusBar = self.statusBar()

        exitAct = QAction(QIcon('exit.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.setToolTip("Push to <b>quit</b>")
        exitAct.triggered.connect(self.close)

        viewAct = QAction("View Statusbar", self, checkable=True)
        viewAct.setStatusTip("View Statusbar")
        viewAct.setChecked(True)
        viewAct.triggered.connect(self.SetVisible)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        setMenu = menubar.addMenu('Set')
        setMenu.addAction(viewAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(400, 200, 350, 250)
        self.setWindowTitle("Menu Practice")
        self.setWindowIcon(QIcon("doge.jpg"))
        self.show()

    def SetVisible(self, state):

        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
