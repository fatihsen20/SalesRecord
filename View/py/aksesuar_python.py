# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/aksesuar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aksesuar(object):
    def setupUi(self, aksesuar):
        aksesuar.setObjectName("aksesuar")
        aksesuar.resize(530, 243)
        self.label_5 = QtWidgets.QLabel(aksesuar)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(aksesuar)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.txt_aksesuar = QtWidgets.QLineEdit(aksesuar)
        self.txt_aksesuar.setGeometry(QtCore.QRect(150, 60, 331, 31))
        self.txt_aksesuar.setObjectName("txt_aksesuar")
        self.txt_fiyat = QtWidgets.QLineEdit(aksesuar)
        self.txt_fiyat.setGeometry(QtCore.QRect(150, 120, 331, 31))
        self.txt_fiyat.setObjectName("txt_fiyat")
        self.btn_kaydet = QtWidgets.QPushButton(aksesuar)
        self.btn_kaydet.setGeometry(QtCore.QRect(180, 200, 75, 23))
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_anamenu = QtWidgets.QPushButton(aksesuar)
        self.btn_anamenu.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")

        self.retranslateUi(aksesuar)
        QtCore.QMetaObject.connectSlotsByName(aksesuar)

    def retranslateUi(self, aksesuar):
        _translate = QtCore.QCoreApplication.translate
        aksesuar.setWindowTitle(_translate("aksesuar", "Aksesuar Ekle"))
        self.label_5.setText(_translate("aksesuar", "Aksesuar Adı:"))
        self.label_6.setText(_translate("aksesuar", "Alış Fiyatı:"))
        self.btn_kaydet.setText(_translate("aksesuar", "Kaydet"))
        self.btn_anamenu.setText(_translate("aksesuar", "Anamenü"))

