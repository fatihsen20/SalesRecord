# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/aksesuarSatis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AksesuarSatis(object):
    def setupUi(self, AksesuarSatis):
        AksesuarSatis.setObjectName("AksesuarSatis")
        AksesuarSatis.resize(422, 348)
        self.label_5 = QtWidgets.QLabel(AksesuarSatis)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AksesuarSatis)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(AksesuarSatis)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btn_Kaydet = QtWidgets.QPushButton(AksesuarSatis)
        self.btn_Kaydet.setGeometry(QtCore.QRect(100, 270, 75, 23))
        self.btn_Kaydet.setObjectName("btn_Kaydet")
        self.btn_anamenu = QtWidgets.QPushButton(AksesuarSatis)
        self.btn_anamenu.setGeometry(QtCore.QRect(230, 270, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.comboBox = QtWidgets.QComboBox(AksesuarSatis)
        self.comboBox.setGeometry(QtCore.QRect(150, 50, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.txt_Tarih = QtWidgets.QDateEdit(AksesuarSatis)
        self.txt_Tarih.setGeometry(QtCore.QRect(150, 110, 251, 31))
        self.txt_Tarih.setObjectName("txt_Tarih")
        self.txt_Fiyat = QtWidgets.QLineEdit(AksesuarSatis)
        self.txt_Fiyat.setGeometry(QtCore.QRect(150, 180, 251, 31))
        self.txt_Fiyat.setObjectName("txt_Fiyat")

        self.retranslateUi(AksesuarSatis)
        QtCore.QMetaObject.connectSlotsByName(AksesuarSatis)

    def retranslateUi(self, AksesuarSatis):
        _translate = QtCore.QCoreApplication.translate
        AksesuarSatis.setWindowTitle(_translate("AksesuarSatis", "Aksesuar Satış Formu"))
        self.label_5.setText(_translate("AksesuarSatis", "Aksesuar Adı:"))
        self.label_6.setText(_translate("AksesuarSatis", "Satış Tarihi:"))
        self.label_7.setText(_translate("AksesuarSatis", "Satış Fiyatı:"))
        self.btn_Kaydet.setText(_translate("AksesuarSatis", "Kaydet"))
        self.btn_anamenu.setText(_translate("AksesuarSatis", "AnaMenü"))

