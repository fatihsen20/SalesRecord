# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/teknikServis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_teknik_servis(object):
    def setupUi(self, teknik_servis):
        teknik_servis.setObjectName("teknik_servis")
        teknik_servis.resize(440, 292)
        self.label_7 = QtWidgets.QLabel(teknik_servis)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(teknik_servis)
        self.label_8.setGeometry(QtCore.QRect(30, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(teknik_servis)
        self.label_9.setGeometry(QtCore.QRect(30, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(teknik_servis)
        self.label_10.setGeometry(QtCore.QRect(-10, 140, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.txt_tarih = QtWidgets.QDateEdit(teknik_servis)
        self.txt_tarih.setGeometry(QtCore.QRect(130, 30, 271, 31))
        self.txt_tarih.setObjectName("txt_tarih")
        self.txt_islem = QtWidgets.QLineEdit(teknik_servis)
        self.txt_islem.setGeometry(QtCore.QRect(130, 70, 271, 31))
        self.txt_islem.setObjectName("txt_islem")
        self.txt_tutar = QtWidgets.QLineEdit(teknik_servis)
        self.txt_tutar.setGeometry(QtCore.QRect(130, 110, 271, 31))
        self.txt_tutar.setObjectName("txt_tutar")
        self.txt_maliyet = QtWidgets.QLineEdit(teknik_servis)
        self.txt_maliyet.setGeometry(QtCore.QRect(130, 150, 271, 31))
        self.txt_maliyet.setObjectName("txt_maliyet")
        self.btn_kaydet = QtWidgets.QPushButton(teknik_servis)
        self.btn_kaydet.setGeometry(QtCore.QRect(130, 240, 75, 23))
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_anamenu = QtWidgets.QPushButton(teknik_servis)
        self.btn_anamenu.setGeometry(QtCore.QRect(230, 240, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")

        self.retranslateUi(teknik_servis)
        QtCore.QMetaObject.connectSlotsByName(teknik_servis)

    def retranslateUi(self, teknik_servis):
        _translate = QtCore.QCoreApplication.translate
        teknik_servis.setWindowTitle(_translate("teknik_servis", "Teknik Servis Formu"))
        self.label_7.setText(_translate("teknik_servis", "İşlem Tarihi:"))
        self.label_8.setText(_translate("teknik_servis", "İşlem:"))
        self.label_9.setText(_translate("teknik_servis", "Tutar:"))
        self.label_10.setText(_translate("teknik_servis", "Maliyet:"))
        self.btn_kaydet.setText(_translate("teknik_servis", "Kaydet"))
        self.btn_anamenu.setText(_translate("teknik_servis", "AnaMenü"))

