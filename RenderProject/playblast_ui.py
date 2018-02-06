# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bum\Desktop\playblst.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    from PyQt5 import QtWidgets, QtCore, QtGui

class Play_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(280, 150))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(7)
        Form.setFont(font)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(70, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Fan Heiti Std B")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Fan Heiti Std B")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Fan Heiti Std B")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 151, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "playblst"))
        self.label_2.setText(_translate("Form", "ep"))
        self.label_3.setText(_translate("Form", "suver"))
        self.pushButton.setText(_translate("Form", "PushButton"))

