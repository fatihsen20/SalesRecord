# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/AksesuarSatisTable.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aksesuarSatisTable(object):
    def setupUi(self, aksesuarSatisTable):
        aksesuarSatisTable.setObjectName("aksesuarSatisTable")
        aksesuarSatisTable.resize(900, 437)
        self.tbl_AksesuarSatis = QtWidgets.QTableWidget(aksesuarSatisTable)
        self.tbl_AksesuarSatis.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.tbl_AksesuarSatis.setObjectName("tbl_AksesuarSatis")
        self.tbl_AksesuarSatis.setColumnCount(5)
        self.tbl_AksesuarSatis.setHorizontalHeaderLabels(["Aksesuar No","Aksesuar Adı","Tarih","Alış Fiyatı","Satış Fiyatı"])
        self.tbl_AksesuarSatis.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.btn_anamenu = QtWidgets.QPushButton(aksesuarSatisTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(420, 400, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.txt_ara = QtWidgets.QLineEdit(aksesuarSatisTable)
        self.txt_ara.setGeometry(QtCore.QRect(660, 30, 221, 41))
        self.txt_ara.setObjectName("txt_ara")
        self.btn_ara = QtWidgets.QPushButton(aksesuarSatisTable)
        self.btn_ara.setGeometry(QtCore.QRect(740, 90, 75, 23))
        self.btn_ara.setObjectName("btn_ara")

        self.retranslateUi(aksesuarSatisTable)
        QtCore.QMetaObject.connectSlotsByName(aksesuarSatisTable)

    def retranslateUi(self, aksesuarSatisTable):
        _translate = QtCore.QCoreApplication.translate
        aksesuarSatisTable.setWindowTitle(_translate("aksesuarSatisTable", "Aksesuar Satış Tablosu"))
        self.btn_anamenu.setText(_translate("aksesuarSatisTable", "AnaMenu"))
        self.btn_ara.setText(_translate("aksesuarSatisTable", "Ara"))

