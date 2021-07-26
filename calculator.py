from PyQt5 import QtCore, QtGui, QtWidgets
# this project is finished in 01/12/2020 #_completed 100%


class Ui_Calcultor(object):

    def setupUi(self, Calcultor):

        Calcultor.setObjectName("Calcultor")
        Calcultor.setWindowModality(QtCore.Qt.ApplicationModal)
        Calcultor.resize(960, 493)
        Calcultor.setMaximumHeight(493)
        Calcultor.setMaximumWidth(960)
        Calcultor.setMinimumHeight(493)
        Calcultor.setMinimumWidth(960)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Calcultor.setFont(font)
        Calcultor.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Calcultor.setToolTipDuration(1)
        Calcultor.setLayoutDirection(QtCore.Qt.RightToLeft)
        Calcultor.setStyleSheet("QPushButton::default{\n"
                                "    border-style: solid;\n"
                                "    border-color: #050a0e;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 5px;\n"
                                "    color: #FFFFFF;\n"
                                "    padding: 2px;\n"
                                "    background-color: #151a1e;;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "    border-style: solid;\n"
                                "    border-color: #050a0e;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 5px;\n"
                                "    color: #d3dae3;\n"
                                "    padding: 2px;\n"
                                "    background-color: #1c1f1f;\n"
                                "}\n"
                                "QPushButton:pressed{\n"
                                "    border-style: solid;\n"
                                "    border-color: #050a0e;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 5px;\n"
                                "    color: #d3dae3;\n"
                                "    padding: 2px;\n"
                                "    background-color: #2c2f2f;\n"
                                "}\n"
                                "QPushButton:disabled{\n"
                                "    border-style: solid;\n"
                                "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                "    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
                                "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
                                "    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 5px;\n"
                                "    color: #808086;\n"
                                "    padding: 2px;\n"
                                "    background-color: rgb(142,142,142);\n"
                                "}\n"
                                "QLineEdit {\n"
                                "    border-width: 1px;\n"
                                "    border-style: solid;\n"
                                "    border-color: #4fa08b;\n"
                                "    background-color: #222b2e;\n"
                                "    color: #d3dae3;\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(Calcultor)
        self.centralwidget.setObjectName("centralwidget")
        self.screen = QtWidgets.QLineEdit(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(80, 8, 721, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.screen.setFont(font)
        self.screen.setStyleSheet("QTextEdit {\n"
                                  "    background-color:rgb(42, 42, 42);\n"
                                  "    color: rgb(0, 255, 0);\n"
                                  "}")
        self.screen.setText("")
        self.screen.setObjectName("screen")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(30, 90, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(210, 90, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(390, 90, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(30, 180, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(210, 180, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(390, 180, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(30, 270, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(210, 270, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(390, 270, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(30, 360, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.Button_point = QtWidgets.QPushButton(self.centralwidget)
        self.Button_point.setGeometry(QtCore.QRect(210, 360, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_point.setFont(font)
        self.Button_point.setObjectName("Button_point")
        # connect numbers Buttons:
        self.Button_point.clicked.connect(lambda: self.show("."))
        self.Button_0.clicked.connect(lambda: self.show(0))
        self.Button_1.clicked.connect(lambda: self.show(1))
        self.Button_2.clicked.connect(lambda: self.show(2))
        self.Button_3.clicked.connect(lambda: self.show(3))
        self.Button_4.clicked.connect(lambda: self.show(4))
        self.Button_5.clicked.connect(lambda: self.show(5))
        self.Button_6.clicked.connect(lambda: self.show(6))
        self.Button_7.clicked.connect(lambda: self.show(7))
        self.Button_8.clicked.connect(lambda: self.show(8))
        self.Button_9.clicked.connect(lambda: self.show(9))

        self.Button_eq = QtWidgets.QPushButton(self.centralwidget)
        self.Button_eq.setGeometry(QtCore.QRect(390, 360, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_eq.setFont(font)
        self.Button_eq.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_eq.setStyleSheet("\n"
                                     "\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "    border-style: solid;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: transparent;\n"
                                     "    border-width: 1px;\n"
                                     "    border-style: solid;\n"
                                     "    color: #FFFFFF;\n"
                                     "    padding: 2px;\n"
                                     "    background-color: #ff5500;\n"
                                     "}\n"
                                     "QPushButton::default{\n"
                                     "    border-style: inset;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: #04b97f;\n"
                                     "    border-width: 1px;\n"
                                     "    color: #FFFFFF;\n"
                                     "    padding: 2px;\n"
                                     "    background-color: #ff5500;\n"
                                     "}\n"
                                     "QToolButton {\n"
                                     "    border-style: solid;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: #04b97f;\n"
                                     "    border-bottom-width: 1px;\n"
                                     "    border-style: solid;\n"
                                     "    color: #a9b7c6;\n"
                                     "    padding: 2px;\n"
                                     "    background-color: #1e1d23;\n"
                                     "}\n"
                                     "QToolButton:hover{\n"
                                     "    border-style: solid;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: #37efba;\n"
                                     "    border-bottom-width: 2px;\n"
                                     "    border-style: solid;\n"
                                     "    color: #FFFFFF;\n"
                                     "    padding-bottom: 1px;\n"
                                     "    background-color: #1e1d23;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    border-style: solid;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: #37efba;\n"
                                     "    border-bottom-width: 1px;\n"
                                     "    border-style: solid;\n"
                                     "    color: #FFFFFF;\n"
                                     "    padding-bottom: 2px;\n"
                                     "    background-color: #1e1d23;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    border-style: solid;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: #37efba;\n"
                                     "    border-bottom-width: 2px;\n"
                                     "    border-style: solid;\n"
                                     "    color: #37efba;\n"
                                     "    padding-bottom: 1px;\n"
                                     "    background-color: #1e1d23;\n"
                                     "}\n"
                                     "QPushButton:disabled{\n"
                                     "    border-style: solid;\n"
                                     "    border-top-color: transparent;\n"
                                     "    border-right-color: transparent;\n"
                                     "    border-left-color: transparent;\n"
                                     "    border-bottom-color: #808086;\n"
                                     "    border-bottom-width: 2px;\n"
                                     "    border-style: solid;\n"
                                     "    color: #808086;\n"
                                     "    padding-bottom: 1px;\n"
                                     "    background-color: #1e1d23;\n"
                                     "}")
        self.Button_eq.setObjectName("Button_eq")

        self.Button_eq.clicked.connect(self.operation)
        self.Button_eq.setAutoDefault(True)
        self.Button_eq.setDefault(False)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(570, 90, 391, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Button_add = QtWidgets.QPushButton(self.frame)
        self.Button_add.setGeometry(QtCore.QRect(150, 0, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_add.setFont(font)
        self.Button_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_add.setStyleSheet("\n"
                                      "\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "    border-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QPushButton::default{\n"
                                      "    border-style: inset;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-width: 1px;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QToolButton {\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #a9b7c6;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QToolButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #37efba;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:disabled{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #808086;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #808086;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}")
        self.Button_add.setAutoRepeat(True)
        self.Button_add.setAutoRepeatInterval(102)
        self.Button_add.setObjectName("Button_add")
        self.Button_suo = QtWidgets.QPushButton(self.frame)
        self.Button_suo.setGeometry(QtCore.QRect(150, 90, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_suo.setFont(font)
        self.Button_suo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_suo.setStyleSheet("\n"
                                      "\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "    border-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QPushButton::default{\n"
                                      "    border-style: inset;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-width: 1px;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QToolButton {\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #a9b7c6;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QToolButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #37efba;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:disabled{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #808086;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #808086;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}")
        self.Button_suo.setAutoRepeat(True)
        self.Button_suo.setAutoRepeatInterval(102)
        self.Button_suo.setObjectName("Button_suo")
        self.Button_div = QtWidgets.QPushButton(self.frame)
        self.Button_div.setGeometry(QtCore.QRect(150, 270, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_div.setFont(font)
        self.Button_div.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_div.setStyleSheet("\n"
                                      "\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "    border-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QPushButton::default{\n"
                                      "    border-style: inset;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-width: 1px;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QToolButton {\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #a9b7c6;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QToolButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #37efba;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:disabled{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #808086;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #808086;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}")
        self.Button_div.setAutoRepeat(True)
        self.Button_div.setAutoRepeatInterval(102)
        self.Button_div.setObjectName("Button_div")
        self.Button_mul = QtWidgets.QPushButton(self.frame)
        self.Button_mul.setGeometry(QtCore.QRect(150, 180, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_mul.setFont(font)
        self.Button_mul.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_mul.setStyleSheet("\n"
                                      "\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: transparent;\n"
                                      "    border-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QPushButton::default{\n"
                                      "    border-style: inset;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-width: 1px;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #ff5500;\n"
                                      "}\n"
                                      "QToolButton {\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #04b97f;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #a9b7c6;\n"
                                      "    padding: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QToolButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #FFFFFF;\n"
                                      "    padding-bottom: 2px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #37efba;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #37efba;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}\n"
                                      "QPushButton:disabled{\n"
                                      "    border-style: solid;\n"
                                      "    border-top-color: transparent;\n"
                                      "    border-right-color: transparent;\n"
                                      "    border-left-color: transparent;\n"
                                      "    border-bottom-color: #808086;\n"
                                      "    border-bottom-width: 2px;\n"
                                      "    border-style: solid;\n"
                                      "    color: #808086;\n"
                                      "    padding-bottom: 1px;\n"
                                      "    background-color: #1e1d23;\n"
                                      "}")
        self.Button_mul.setAutoRepeat(True)
        self.Button_mul.setAutoRepeatInterval(102)
        self.Button_mul.setObjectName("Button_mul")

        self.Button_add.clicked.connect(lambda: self.show('+'))
        self.Button_mul.clicked.connect(lambda: self.show('*'))
        self.Button_div.clicked.connect(lambda: self.show('/'))
        self.Button_suo.clicked.connect(lambda: self.show('-'))

        self.Button_Clear = QtWidgets.QPushButton(self.frame)
        self.Button_Clear.setGeometry(QtCore.QRect(10, 0, 131, 79))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_Clear.setFont(font)
        self.Button_Clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_Clear.setToolTipDuration(-2)
        self.Button_Clear.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Button_Clear.setAutoRepeatDelay(296)
        self.Button_Clear.setObjectName("Button_Clear")

        self.Button_Clear.clicked.connect(lambda: self.show("c"))
        self.Button_all_clear = QtWidgets.QPushButton(self.frame)
        self.Button_all_clear.setGeometry(QtCore.QRect(10, 90, 131, 81))
        self.Button_all_clear.clicked.connect(lambda: self.show("ac"))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_all_clear.setFont(font)
        self.Button_all_clear.setObjectName("Button_all_clear")
        self.Button_modulu = QtWidgets.QPushButton(self.frame)
        self.Button_modulu.setGeometry(QtCore.QRect(10, 180, 131, 81))
        self.Button_modulu.clicked.connect(lambda: self.show('%'))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setStrikeOut(False)
        self.Button_modulu.setFont(font)
        self.Button_modulu.setObjectName("Button_modulu")
        self.screen.raise_()
        self.Button_7.raise_()
        self.Button_8.raise_()
        self.Button_9.raise_()
        self.Button_4.raise_()
        self.Button_5.raise_()
        self.Button_6.raise_()
        self.Button_1.raise_()
        self.Button_2.raise_()
        self.Button_3.raise_()
        self.Button_0.raise_()
        self.Button_point.raise_()
        self.frame.raise_()
        self.Button_eq.raise_()

        Calcultor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calcultor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 37))
        self.menubar.setObjectName("menubar")
        Calcultor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calcultor)
        self.statusbar.setObjectName("statusbar")

        Calcultor.setStatusBar(self.statusbar)

        self.retranslateUi(Calcultor)
        QtCore.QMetaObject.connectSlotsByName(Calcultor)

    def show(self, TXT):
        # enter nubmers and opertions in the screen :
        # clear button

        if TXT == 'c':
            current = self.screen.text()
            if current != '':
                f = len(current)
                l = current[f-1]
                current = current.replace(l, "")
                self.screen.setText(current)
            else:
                pass
        elif TXT == 'ac':
            self.screen.clear()
        elif TXT != ('c'):
            current = self.screen.text()
            if (current == '') and (TXT == 0):
                self.screen.clear()
            else:
                self.screen.setText(current + str(TXT))

    def operation(self):
        oper = self.screen.text()
        try:
            result = eval(oper)

        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            result = "Math ERROR"

        self.screen.setText(str(result))

    def retranslateUi(self, Calcultor):
        _translate = QtCore.QCoreApplication.translate
        Calcultor.setWindowTitle(_translate("Calcultor", "Simple Calculator"))
        self.Button_7.setText(_translate("Calcultor", "7"))
        self.Button_8.setText(_translate("Calcultor", "8"))
        self.Button_9.setText(_translate("Calcultor", "9"))
        self.Button_4.setText(_translate("Calcultor", "4"))
        self.Button_5.setText(_translate("Calcultor", "5"))
        self.Button_6.setText(_translate("Calcultor", "6"))
        self.Button_1.setText(_translate("Calcultor", "1"))
        self.Button_2.setText(_translate("Calcultor", "2"))
        self.Button_3.setText(_translate("Calcultor", "3"))
        self.Button_0.setText(_translate("Calcultor", "0"))
        self.Button_point.setText(_translate("Calcultor", "."))
        self.Button_eq.setText(_translate("Calcultor", "="))
        self.Button_add.setText(_translate("Calcultor", "+"))
        self.Button_suo.setText(_translate("Calcultor", "-"))
        self.Button_div.setText(_translate("Calcultor", "÷"))
        self.Button_mul.setText(_translate("Calcultor", "x"))
        self.Button_Clear.setText(_translate("Calcultor", "C"))
        self.Button_all_clear.setText(_translate("Calcultor", "AC"))
        self.Button_modulu.setText(_translate("Calcultor", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calcultor = QtWidgets.QMainWindow()
    Calcultor.setWindowIcon(QtGui.QIcon('logo.png'))
    Calcultor.setFocus()
    ui = Ui_Calcultor()
    ui.setupUi(Calcultor)
    Calcultor.show()
    sys.exit(app.exec_())
