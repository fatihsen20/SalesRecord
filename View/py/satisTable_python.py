# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showSatisTable(object):
    def setupUi(self, showSatisTable):
        showSatisTable.setObjectName("showSatisTable")
        showSatisTable.resize(1067, 537)
        self.tbl_satis = QtWidgets.QTableWidget(showSatisTable)
        self.tbl_satis.setGeometry(QtCore.QRect(10, 20, 871, 421))
        self.tbl_satis.setObjectName("tbl_satis")
        self.tbl_satis.setColumnCount(8)
        self.tbl_satis.setHorizontalHeaderLabels(["Urun No","IMEI","Model","Alım Tarihi","Satış Tarihi","Alım Fiyatı","Satış Fiyatı","Alım Yeri"])
        self.tbl_satis.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.tbl_satis.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.btn_anamenu = QtWidgets.QPushButton(showSatisTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(450, 480, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.btn_ara = QtWidgets.QPushButton(showSatisTable)
        self.btn_ara.setGeometry(QtCore.QRect(930, 90, 75, 23))
        self.btn_ara.setObjectName("btn_ara")
        self.txt_ara = QtWidgets.QLineEdit(showSatisTable)
        self.txt_ara.setGeometry(QtCore.QRect(900, 50, 141, 31))
        self.txt_ara.setObjectName("txt_ara")
        self.txt_ara.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(showSatisTable)
        QtCore.QMetaObject.connectSlotsByName(showSatisTable)

    def retranslateUi(self, showSatisTable):
        _translate = QtCore.QCoreApplication.translate
        showSatisTable.setWindowTitle(_translate("showSatisTable", "Satış Tablosu"))
        self.btn_anamenu.setText(_translate("showSatisTable", "AnaMenü"))
        self.btn_ara.setText(_translate("showSatisTable", "Ara"))
        self.txt_ara.setPlaceholderText(_translate("showAlimTable", "Imei veya Ürün No Giriniz"))

