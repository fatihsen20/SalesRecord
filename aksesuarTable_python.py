# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/aksesuarTable.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showAksesuar(object):
    def setupUi(self, showAksesuar):
        showAksesuar.setObjectName("showAksesuar")
        showAksesuar.resize(796, 380)
        self.tbl_aksesuar = QtWidgets.QTableWidget(showAksesuar)
        self.tbl_aksesuar.setGeometry(QtCore.QRect(10, 20, 541, 301))
        self.tbl_aksesuar.setObjectName("tbl_aksesuar")
        self.tbl_aksesuar.setColumnCount(3)
        self.tbl_aksesuar.setHorizontalHeaderLabels(["Aksesuar No","Aksesuar Adı","Alış Fiyatı"])
        self.tbl_aksesuar.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.btn_anamenu = QtWidgets.QPushButton(showAksesuar)
        self.btn_anamenu.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.txt_ara = QtWidgets.QLineEdit(showAksesuar)
        self.txt_ara.setGeometry(QtCore.QRect(560, 30, 231, 41))
        self.txt_ara.setObjectName("txt_ara")
        self.btn_ara = QtWidgets.QPushButton(showAksesuar)
        self.btn_ara.setGeometry(QtCore.QRect(634, 90, 81, 31))
        self.btn_ara.setObjectName("btn_ara")

        self.retranslateUi(showAksesuar)
        QtCore.QMetaObject.connectSlotsByName(showAksesuar)

    def retranslateUi(self, showAksesuar):
        _translate = QtCore.QCoreApplication.translate
        showAksesuar.setWindowTitle(_translate("showAksesuar", "Aksesuar Tablosu"))
        self.btn_anamenu.setText(_translate("showAksesuar", "AnaMenü"))
        self.btn_ara.setText(_translate("showAksesuar", "Ara"))

