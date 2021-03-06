# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locker2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 434)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(69, 73, 74);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 2)
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setMinimumSize(QtCore.QSize(0, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelInfo.setFont(font)
        self.labelInfo.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 127);")
        self.labelInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setWordWrap(True)
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout_2.addWidget(self.labelInfo, 6, 0, 1, 2)
        self.listView = QtWidgets.QTreeWidget(self.centralwidget)
        self.listView.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.listView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listView.setObjectName("listView")
        self.listView.headerItem().setText(0, "1")
        self.gridLayout_2.addWidget(self.listView, 4, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 61))
        self.frame.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonStart = QtWidgets.QPushButton(self.frame)
        self.buttonStart.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonStart.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonStart.setObjectName("buttonStart")
        self.gridLayout.addWidget(self.buttonStart, 0, 1, 1, 1)
        self.textInput = QtWidgets.QLineEdit(self.frame)
        self.textInput.setMinimumSize(QtCore.QSize(0, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textInput.setFont(font)
        self.textInput.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.textInput.setText("")
        self.textInput.setFrame(False)
        self.textInput.setAlignment(QtCore.Qt.AlignCenter)
        self.textInput.setObjectName("textInput")
        self.gridLayout.addWidget(self.textInput, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(6, 3, 6, 3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.buttonClose = QtWidgets.QToolButton(self.frame_2)
        self.buttonClose.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonClose.setFont(font)
        self.buttonClose.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.buttonClose.setObjectName("buttonClose")
        self.gridLayout_3.addWidget(self.buttonClose, 0, 4, 1, 1)
        self.buttonMinimize = QtWidgets.QToolButton(self.frame_2)
        self.buttonMinimize.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonMinimize.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonMinimize.setFont(font)
        self.buttonMinimize.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.buttonMinimize.setObjectName("buttonMinimize")
        self.gridLayout_3.addWidget(self.buttonMinimize, 0, 3, 1, 1)
        self.labelTitleText = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.labelTitleText.setFont(font)
        self.labelTitleText.setStyleSheet("color: rgb(170, 255, 127);")
        self.labelTitleText.setObjectName("labelTitleText")
        self.gridLayout_3.addWidget(self.labelTitleText, 0, 0, 1, 1)
        self.buttonAbout = QtWidgets.QToolButton(self.frame_2)
        self.buttonAbout.setMinimumSize(QtCore.QSize(20, 20))
        self.buttonAbout.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonAbout.setFont(font)
        self.buttonAbout.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.buttonAbout.setObjectName("buttonAbout")
        self.gridLayout_3.addWidget(self.buttonAbout, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelInfo.setText(_translate("MainWindow", "Info"))
        self.buttonStart.setText(_translate("MainWindow", "Encrypt / Decrypt"))
        self.textInput.setPlaceholderText(_translate("MainWindow", "Drag and Drop Files / Folders to Lock or unlocked here...."))
        self.buttonClose.setText(_translate("MainWindow", "X"))
        self.buttonMinimize.setText(_translate("MainWindow", "-"))
        self.labelTitleText.setText(_translate("MainWindow", "JbAdonai Ventures "))
        self.buttonAbout.setText(_translate("MainWindow", "?"))
