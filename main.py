import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg

w1, w2, alpha = 0.0, 0.0, 0.0
OPR = ""


class Windows:
    def __init__(self):
        self.main = Ui_MainWindow()
        self.func = Ui_func()

    def show_main(self):
        self.main.setupUi(self.main.window)
        self.main.window.show()

    def switch_window(self):
        self.main.window.close()
        self.func.setupUi(self.func.window)
        self.func.window.show()

    def switch_back(self):
        self.func.window.close()
        self.main.setupUi(self.main.window)
        self.main.window.show()


class Ui_MainWindow(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 335)
        MainWindow.setMinimumSize(QtCore.QSize(850, 335))
        MainWindow.setMaximumSize(QtCore.QSize(850, 335))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 831, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 831, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.NOR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.NOR.setObjectName("NOR")
        self.gridLayout.addWidget(self.NOR, 1, 0, 1, 1)
        self.AND = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.AND.setObjectName("AND")
        self.gridLayout.addWidget(self.AND, 0, 1, 1, 1)
        self.OR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OR.setObjectName("OR")
        self.gridLayout.addWidget(self.OR, 0, 0, 1, 1)
        self.XOR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.XOR.setObjectName("XOR")
        self.gridLayout.addWidget(self.XOR, 0, 2, 1, 1)
        self.NAND = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.NAND.setObjectName("NAND")
        self.gridLayout.addWidget(self.NAND, 1, 1, 1, 1)
        self.XNOR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.XNOR.setObjectName("XNOR")
        self.gridLayout.addWidget(self.XNOR, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.NOR.clicked.connect(lambda: self.switchWindow('NOR'))
        self.XNOR.clicked.connect(lambda: self.switchWindow('XNOR'))
        self.OR.clicked.connect(lambda: self.switchWindow('OR'))
        self.AND.clicked.connect(lambda: self.switchWindow('AND'))
        self.NAND.clicked.connect(lambda: self.switchWindow('NAND'))
        self.XOR.clicked.connect(lambda: self.switchWindow('XOR'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate("MainWindow", "WELCOME TO GATE NETWORKS!!!"))
        self.NOR.setText(_translate("MainWindow", "NOR"))
        self.AND.setText(_translate("MainWindow", "AND"))
        self.OR.setText(_translate("MainWindow", "OR"))
        self.XOR.setText(_translate("MainWindow", "XOR"))
        self.NAND.setText(_translate("MainWindow", "NAND"))
        self.XNOR.setText(_translate("MainWindow", "XNOR"))

    def switchWindow(self, text):
        global OPR
        OPR = text
        Page.switch_window()
        print(text)


class Ui_func(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, func):
        func.setObjectName("func")
        func.resize(850, 554)
        func.setMinimumSize(QtCore.QSize(850, 554))
        func.setMaximumSize(QtCore.QSize(850, 554))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        func.setFont(font)
        self.centralwidget = QtWidgets.QWidget(func)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 831, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 341, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(10, 0, 10, 5)
        self.grid.setHorizontalSpacing(17)
        self.grid.setVerticalSpacing(39)
        self.grid.setObjectName("grid")
        self.alpha = QtWidgets.QSlider(self.gridLayoutWidget)
        self.alpha.setOrientation(QtCore.Qt.Horizontal)
        self.alpha.setObjectName("alpha")
        self.grid.addWidget(self.alpha, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.grid.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.grid.addWidget(self.label_2, 0, 0, 1, 1)
        self.w1 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.w1.setOrientation(QtCore.Qt.Horizontal)
        self.w1.setObjectName("w1")
        self.grid.addWidget(self.w1, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.grid.addWidget(self.label_3, 2, 0, 1, 1)
        self.w2 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.w2.setOrientation(QtCore.Qt.Horizontal)
        self.w2.setObjectName("w2")
        self.grid.addWidget(self.w2, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.submit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.grid.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 50, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        func.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(func)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 28))
        self.menubar.setObjectName("menubar")
        func.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(func)
        self.statusbar.setObjectName("statusbar")
        func.setStatusBar(self.statusbar)
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        # self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(400, 50, 431, 441))
        self.retranslateUi(func)
        QtCore.QMetaObject.connectSlotsByName(func)

        self.alpha.setRange(1, 100)
        self.w1.setRange(-100, 100)
        self.w2.setRange(-100, 100)
        self.alpha.valueChanged.connect(lambda: self.updateLabel())
        self.w1.valueChanged.connect(lambda: self.updateLabel())
        self.w2.valueChanged.connect(lambda: self.updateLabel())
        self.back.clicked.connect(lambda: self.switchWindow())
        self.submit.clicked.connect(lambda: self.plot(w1, w2, alpha))

    def retranslateUi(self, func):
        global w1, w2, alpha
        _translate = QtCore.QCoreApplication.translate
        func.setWindowTitle(_translate("func", "MainWindow"))
        self.label.setText(_translate("func", "Enter Variables"))
        self.label_4.setText(_translate("func", f"W2: {w2}"))
        self.label_2.setText(_translate("func", f"Alpha: {alpha}"))
        self.label_3.setText(_translate("func", f"W1: {w1}"))
        self.back.setText(_translate("func", "Back"))
        self.submit.setText(_translate("func", "Submit"))

    def updateLabel(self):
        global w1, w2, alpha
        w2 = self.w2.value() / 100
        w1 = self.w1.value() / 100
        alpha = self.alpha.value() / 100
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("func", f"W2: {w2}"))
        self.label_2.setText(_translate("func", f"Alpha: {alpha}"))
        self.label_3.setText(_translate("func", f"W1: {w1}"))

    def switchWindow(self):
        Page.switch_back()

    def plot(self, w1, w2, alpha):
        self.graphicsView.clear()
        global OPR
        def AND(x, y): return int(x and y)
        def NAND(x, y): return int(not (x and y))
        def OR(x, y): return int(x or y)
        def NOR(x, y): return int(not (x or y))
        def XOR(x, y): return int(x ^ y)
        inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
        def XNOR(x, y): return int(not (x ^ y))
        counter = 0
        b = 0

        for i in inputs:
            if eval(OPR)(i[0], i[1]):
                self.graphicsView.plot(
                    [i[0]], [i[1]], pen=None, symbolBrush=(255, 255, 255), symbol='o')
            else:
                self.graphicsView.plot(
                    [i[0]], [i[1]], pen=None, symbolBrush=(0, 0, 0), symbol='o')
        for i in range(50):

            if i % 4 == 0:
                counter = 0
            x, y = inputs[i % 4]
            f = 1 if (w1 * x + w2 * y) + b > 0 else 0
            E = eval(OPR)(x, y) - f
            if E != 0:
                w1 = w1 + alpha * x * E
                w2 = w2 + alpha * y * E
                counter = 0
                b = b + alpha * E
            else:
                counter += 1
            if counter == 4:
                break
            p1 = self.graphicsView.plot(
                [x for x in [-0.2, 1.2]], [(-w1 * x - b) / w2 for x in [-0.2, 1.2]], pen=(100+3*i, 0, 0))
        if counter == 4:
            p1 = self.graphicsView.plot(
                [x for x in [-0.2, 1.2]], [(-w1 * x - b) / w2 for x in [-0.2, 1.2]], pen=(0, 200, 0))
        # print(f'{i} : {x}, {y} ,{w1}, {w2}, {f}, {E}, {counter}')

        self.graphicsView.mapToScene(10, 10, 10, 10)


app = QtWidgets.QApplication(sys.argv)
Page = Windows()
Page.show_main()
sys.exit(app.exec_())
