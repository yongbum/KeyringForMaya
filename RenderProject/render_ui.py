# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bum\Desktop\render_set.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    from PyQt5 import QtWidgets, QtCore, QtGui

class Rander_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 830)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(530, 830))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(5)
        Form.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(430, 150, 81, 31))
        self.pushButton.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 180, 201, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 130, 110, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 140, 31, 21))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 41, 21))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 290, 151, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 290, 151, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 390, 121, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 390, 41, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 360, 151, 16))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 430, 181, 21))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.unknownnode = QtWidgets.QPushButton(Form)
        self.unknownnode.setGeometry(QtCore.QRect(190, 460, 111, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.unknownnode.setFont(font)
        self.unknownnode.setObjectName("unknownnode")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 500, 201, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 530, 111, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 20, 281, 41))
        self.label_7.setStyleSheet('border: 4px solid #389ebe;')
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 720, 201, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 770, 351, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 190, 81, 31))
        self.pushButton_9.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 620, 51, 31))
        self.pushButton_10.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(310, 620, 51, 31))
        self.pushButton_11.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(250, 580, 151, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 230, 61, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(190, 230, 61, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(430, 230, 81, 31))
        self.pushButton_12.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(190, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 550, 81, 31))
        self.pushButton_13.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(380, 550, 71, 31))
        self.pushButton_14.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(310, 510, 151, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(380, 620, 51, 31))
        self.pushButton_15.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(20, 350, 181, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.unknownplugin = QtWidgets.QPushButton(Form)
        self.unknownplugin.setGeometry(QtCore.QRect(330, 460, 101, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.unknownplugin.setFont(font)
        self.unknownplugin.setObjectName("unknownplugin")
        self.subdivision = QtWidgets.QPushButton(Form)
        self.subdivision.setGeometry(QtCore.QRect(50, 390, 101, 31))
        self.subdivision.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.subdivision.setFont(font)
        self.subdivision.setObjectName("subdivision")
        self.save_ma = QtWidgets.QPushButton(Form)
        self.save_ma.setGeometry(QtCore.QRect(480, 70, 35, 31))
        self.save_ma.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.save_ma.setFont(font)
        self.save_ma.setObjectName("save_ma")
        self.open = QtWidgets.QPushButton(Form)
        self.open.setGeometry(QtCore.QRect(430, 110, 81, 31))
        self.open.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.open.setFont(font)
        self.open.setObjectName("open")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(310, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(260, 90, 41, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 130, 160, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(20, 140, 41, 21))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.save_mb = QtWidgets.QPushButton(Form)
        self.save_mb.setGeometry(QtCore.QRect(426, 70, 35, 31))
        self.save_mb.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.save_mb.setFont(font)
        self.save_mb.setObjectName("save_mb")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(300, 550, 71, 31))
        self.pushButton_16.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(50, 600, 111, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(50, 640, 111, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(50, 680, 111, 31))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(20, 560, 201, 41))
        font = QtGui.QFont()
        font.setFamily("휴먼매직체")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "projct_set"))
        self.label.setText(_translate("Form", "surver:"))
        self.label_2.setText(_translate("Form", "ep:"))
        self.label_3.setText(_translate("Form", "sc :"))
        self.pushButton_2.setText(_translate("Form", "test_set"))
        self.pushButton_3.setText(_translate("Form", "final_set"))
        self.pushButton_4.setText(_translate("Form", "S M O O T H"))
        self.label_4.setText(_translate("Form", "♣ didvide"))
        self.label_5.setText(_translate("Form", "♣ erorr delete"))
        self.pushButton_5.setText(_translate("Form", "Tultle delete"))
        self.unknownnode.setText(_translate("Form", "unlnown node"))
        self.label_6.setText(_translate("Form", "♣  render set"))
        self.pushButton_7.setText(_translate("Form", "Layer_set"))
        self.label_7.setText(_translate("Form", "♣  PUCCA_Lighting"))
        self.label_8.setText(_translate("Form", "♣ Deadline"))
        self.pushButton_8.setText(_translate("Form", "Deadline_up"))
        self.pushButton_9.setText(_translate("Form", "camera"))
        self.pushButton_10.setText(_translate("Form", "CH"))
        self.pushButton_11.setText(_translate("Form", "PR"))
        self.label_9.setText(_translate("Form", "♣  vray_group"))
        self.label_10.setText(_translate("Form", "stert"))
        self.label_11.setText(_translate("Form", "end"))
        self.pushButton_12.setText(_translate("Form", "frame set"))
        self.label_12.setText(_translate("Form", "♣  Layer_in"))
        self.pushButton_13.setText(_translate("Form", "in"))
        self.pushButton_14.setText(_translate("Form", "shadow"))
        self.label_13.setText(_translate("Form", "♣ vary_override"))
        self.pushButton_15.setText(_translate("Form", "BG"))
        self.label_14.setText(_translate("Form", "♣ mesh subdivision"))
        self.unknownplugin.setText(_translate("Form", "unlnown plugin"))
        self.subdivision.setText(_translate("Form", "subdivision"))
        self.save_ma.setText(_translate("Form", "ma"))
        self.open.setText(_translate("Form", "opon"))
        self.label_15.setText(_translate("Form", "ver:"))
        self.label_16.setText(_translate("Form", "part:"))
        self.save_mb.setText(_translate("Form", "mb"))
        self.pushButton_16.setText(_translate("Form", "master"))
        self.pushButton_17.setText(_translate("Form", "outside_set"))
        self.pushButton_18.setText(_translate("Form", "holl_set"))
        self.pushButton_19.setText(_translate("Form", "room_set"))
        self.label_17.setText(_translate("Form", "♣  Lighting set"))
