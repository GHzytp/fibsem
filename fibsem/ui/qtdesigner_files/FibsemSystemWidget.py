# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FibsemSystemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(302, 217)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_connect = QtWidgets.QPushButton(Form)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout.addWidget(self.pushButton_connect, 2, 0, 1, 2)
        self.label_title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 2)
        self.label_ip_address = QtWidgets.QLabel(Form)
        self.label_ip_address.setObjectName("label_ip_address")
        self.gridLayout.addWidget(self.label_ip_address, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_connect.setText(_translate("Form", "Connect"))
        self.label_title.setText(_translate("Form", "System"))
        self.label_ip_address.setText(_translate("Form", "IP Address"))
