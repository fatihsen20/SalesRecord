# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_teknikServisTable(object):
    def setupUi(self, teknikServisTable):
        teknikServisTable.setObjectName("teknikServisTable")
        teknikServisTable.resize(894, 439)
        self.tbl_teknikservis = QtWidgets.QTableWidget(teknikServisTable)
        self.tbl_teknikservis.setGeometry(QtCore.QRect(10, 10, 621, 341))
        self.tbl_teknikservis.setObjectName("tbl_teknikservis")
        self.tbl_teknikservis.setColumnCount(5)
        self.tbl_teknikservis.setHorizontalHeaderLabels(["Tamir No","Tarih","İşlem","Tutar","Maliyet"])
        self.tbl_teknikservis.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        #Table column resize
        header = self.tbl_teknikservis.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.btn_anamenu = QtWidgets.QPushButton(teknikServisTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(400, 390, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.txt_ara = QtWidgets.QLineEdit(teknikServisTable)
        self.txt_ara.setGeometry(QtCore.QRect(650, 40, 231, 31))
        self.txt_ara.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_ara.setObjectName("txt_ara")
        self.btn_ara = QtWidgets.QPushButton(teknikServisTable)
        self.btn_ara.setGeometry(QtCore.QRect(730, 90, 75, 23))
        self.btn_ara.setObjectName("btn_ara")

        self.retranslateUi(teknikServisTable)
        QtCore.QMetaObject.connectSlotsByName(teknikServisTable)

    def retranslateUi(self, teknikServisTable):
        _translate = QtCore.QCoreApplication.translate
        teknikServisTable.setWindowTitle(_translate("teknikServisTable", "Teknik Servis Tablosu"))
        self.btn_anamenu.setText(_translate("teknikServisTable", "AnaMenü"))
        self.txt_ara.setPlaceholderText(_translate("teknikServisTable", "İşlem Giriniz"))
        self.btn_ara.setText(_translate("teknikServisTable", "Ara"))

