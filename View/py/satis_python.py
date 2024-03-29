# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_satisTable(object):
    def setupUi(self, satisTable):
        satisTable.setObjectName("satisTable")
        satisTable.resize(489, 396)
        self.label = QtWidgets.QLabel(satisTable)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(satisTable)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(satisTable)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(satisTable)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(satisTable)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(satisTable)
        self.comboBox.setGeometry(QtCore.QRect(130, 60, 321, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.txt_Model = QtWidgets.QLineEdit(satisTable)
        self.txt_Model.setGeometry(QtCore.QRect(130, 110, 321, 31))
        self.txt_Model.setObjectName("txt_Model")
        self.txt_Model.setReadOnly(True)
        self.txt_Imei = QtWidgets.QLineEdit(satisTable)
        self.txt_Imei.setGeometry(QtCore.QRect(130, 160, 321, 31))
        self.txt_Imei.setObjectName("txt_Imei")
        self.txt_Imei.setReadOnly(True)
        self.txt_SatisTarihi = QtWidgets.QDateEdit(satisTable)
        self.txt_SatisTarihi.setGeometry(QtCore.QRect(130, 210, 321, 31))
        self.txt_SatisTarihi.setObjectName("txt_SatisTarihi")
        self.txt_SatisFiyati = QtWidgets.QLineEdit(satisTable)
        self.txt_SatisFiyati.setGeometry(QtCore.QRect(130, 260, 321, 31))
        self.txt_SatisFiyati.setObjectName("txt_SatisFiyati")
        self.btn_kaydet = QtWidgets.QPushButton(satisTable)
        self.btn_kaydet.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_anamenu = QtWidgets.QPushButton(satisTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(270, 340, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")

        self.retranslateUi(satisTable)
        QtCore.QMetaObject.connectSlotsByName(satisTable)

    def retranslateUi(self, satisTable):
        _translate = QtCore.QCoreApplication.translate
        satisTable.setWindowTitle(_translate("satisTable", "Satış Formu"))
        self.label.setText(_translate("satisTable", "Ürün No:"))
        self.label_2.setText(_translate("satisTable", "Model:"))
        self.label_3.setText(_translate("satisTable", "Imei:"))
        self.label_4.setText(_translate("satisTable", "Satış Tarihi:"))
        self.label_6.setText(_translate("satisTable", "Satış  Fiyatı:"))
        self.btn_kaydet.setText(_translate("satisTable", "Kaydet"))
        self.btn_anamenu.setText(_translate("satisTable", "AnaMenü"))

