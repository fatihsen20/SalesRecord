# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/kar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kar(object):
    def setupUi(self, kar):
        kar.setObjectName("kar")
        kar.resize(328, 390)
        self.txt_Satis = QtWidgets.QLineEdit(kar)
        self.txt_Satis.setGeometry(QtCore.QRect(170, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_Satis.setFont(font)
        self.txt_Satis.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_Satis.setObjectName("txt_Satis")
        self.txt_Satis.setReadOnly(True)
        self.txt_Aksesuar = QtWidgets.QLineEdit(kar)
        self.txt_Aksesuar.setGeometry(QtCore.QRect(170, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_Aksesuar.setFont(font)
        self.txt_Aksesuar.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_Aksesuar.setObjectName("txt_Aksesuar")
        self.txt_Aksesuar.setReadOnly(True)
        self.txt_TeknikServis = QtWidgets.QLineEdit(kar)
        self.txt_TeknikServis.setGeometry(QtCore.QRect(170, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_TeknikServis.setFont(font)
        self.txt_TeknikServis.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_TeknikServis.setObjectName("txt_TeknikServis")
        self.txt_TeknikServis.setReadOnly(True)
        self.label = QtWidgets.QLabel(kar)
        self.label.setGeometry(QtCore.QRect(40, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txt_Total = QtWidgets.QLineEdit(kar)
        self.txt_Total.setGeometry(QtCore.QRect(150, 290, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_Total.setFont(font)
        self.txt_Total.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_Total.setObjectName("txt_Total")
        self.txt_Total.setReadOnly(True)
        self.btn_anamenu = QtWidgets.QPushButton(kar)
        self.btn_anamenu.setGeometry(QtCore.QRect(110, 350, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.cmb_ay = QtWidgets.QComboBox(kar)
        self.cmb_ay.setGeometry(QtCore.QRect(40, 40, 91, 31))
        self.cmb_ay.setObjectName("cmb_ay")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_ay.addItem("")
        self.cmb_yil = QtWidgets.QComboBox(kar)
        self.cmb_yil.setGeometry(QtCore.QRect(180, 40, 91, 31))
        self.cmb_yil.setObjectName("cmb_yil")
        self.cmb_yil.addItem("")
        self.cmb_yil.addItem("")
        self.cmb_yil.addItem("")
        self.cmb_yil.addItem("")
        self.cmb_yil.addItem("")
        self.cmb_yil.addItem("")
        self.cmb_yil.addItem("")
        self.label_2 = QtWidgets.QLabel(kar)
        self.label_2.setGeometry(QtCore.QRect(30, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(kar)
        self.label_3.setGeometry(QtCore.QRect(180, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(kar)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(kar)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(kar)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(kar)
        QtCore.QMetaObject.connectSlotsByName(kar)

    def retranslateUi(self, kar):
        _translate = QtCore.QCoreApplication.translate
        kar.setWindowTitle(_translate("kar", "Kar Hesapla"))
        self.txt_Satis.setText(_translate("kar", "0"))
        self.txt_Aksesuar.setText(_translate("kar", "0"))
        self.txt_TeknikServis.setText(_translate("kar", "0"))
        self.label.setText(_translate("kar", "Toplam Kar:"))
        self.txt_Total.setText(_translate("kar", "0"))
        self.btn_anamenu.setText(_translate("kar", "AnaMenü"))
        self.cmb_ay.setItemText(0, _translate("kar", "1"))
        self.cmb_ay.setItemText(1, _translate("kar", "2"))
        self.cmb_ay.setItemText(2, _translate("kar", "3"))
        self.cmb_ay.setItemText(3, _translate("kar", "4"))
        self.cmb_ay.setItemText(4, _translate("kar", "5"))
        self.cmb_ay.setItemText(5, _translate("kar", "6"))
        self.cmb_ay.setItemText(6, _translate("kar", "7"))
        self.cmb_ay.setItemText(7, _translate("kar", "8"))
        self.cmb_ay.setItemText(8, _translate("kar", "9"))
        self.cmb_ay.setItemText(9, _translate("kar", "10"))
        self.cmb_ay.setItemText(10, _translate("kar", "11"))
        self.cmb_ay.setItemText(11, _translate("kar", "12"))
        self.cmb_yil.setItemText(0, _translate("kar", "2022"))
        self.cmb_yil.setItemText(1, _translate("kar", "2023"))
        self.cmb_yil.setItemText(2, _translate("kar", "2024"))
        self.cmb_yil.setItemText(3, _translate("kar", "2025"))
        self.cmb_yil.setItemText(4, _translate("kar", "2026"))
        self.cmb_yil.setItemText(5, _translate("kar", "2027"))
        self.cmb_yil.setItemText(6, _translate("kar", "2028"))
        self.label_2.setText(_translate("kar", "Ay Seçiniz"))
        self.label_3.setText(_translate("kar", "Yıl Seçiniz"))
        self.label_4.setText(_translate("kar", "Telefon Satış:"))
        self.label_5.setText(_translate("kar", "Aksesuar Satış:"))
        self.label_6.setText(_translate("kar", "Teknik Servis:"))

