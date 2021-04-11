# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileInfo_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 124)
        Form.setMinimumSize(QtCore.QSize(459, 124))
        Form.setMaximumSize(QtCore.QSize(459, 124))
        Form.setStyleSheet("background-color: rgb(69, 73, 74);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: rgb(60, 63, 65);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelFileLocation = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        self.labelFileLocation.setFont(font)
        self.labelFileLocation.setWordWrap(True)
        self.labelFileLocation.setObjectName("labelFileLocation")
        self.gridLayout_2.addWidget(self.labelFileLocation, 1, 0, 1, 2)
        self.buttonDelete = QtWidgets.QPushButton(self.frame)
        self.buttonDelete.setObjectName("buttonDelete")
        self.gridLayout_2.addWidget(self.buttonDelete, 3, 1, 1, 1)
        self.labelFilename = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelFilename.setFont(font)
        self.labelFilename.setObjectName("labelFilename")
        self.gridLayout_2.addWidget(self.labelFilename, 0, 0, 1, 2)
        self.labelFileSize = QtWidgets.QLabel(self.frame)
        self.labelFileSize.setObjectName("labelFileSize")
        self.gridLayout_2.addWidget(self.labelFileSize, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelFileLocation.setText(_translate("Form", "File Location"))
        self.buttonDelete.setText(_translate("Form", "Delete"))
        self.labelFilename.setText(_translate("Form", "Filename"))
        self.labelFileSize.setText(_translate("Form", "File Size"))

