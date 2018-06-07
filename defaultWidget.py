# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/defaulWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 537)
        self.openFileButton = QtWidgets.QPushButton(Form)
        self.openFileButton.setGeometry(QtCore.QRect(330, 390, 131, 41))
        self.openFileButton.setObjectName("openFileButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.openFileButton.setText(_translate("Form", "Open File"))

