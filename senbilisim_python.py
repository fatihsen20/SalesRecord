from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class Ui_AnaMenu(object):
    def setupUi(self, AnaMenu):
        AnaMenu.setObjectName("AnaMenu")
        AnaMenu.resize(646, 360)
        self.pushButton = QtWidgets.QPushButton(AnaMenu)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 300, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 300, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 300, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 300, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 300, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 200, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 200, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 200, 91, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 200, 91, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(AnaMenu)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 200, 91, 31))
        self.pushButton_11.setObjectName("pushButton_11")


        self.retranslateUi(AnaMenu)
        QtCore.QMetaObject.connectSlotsByName(AnaMenu)

    def retranslateUi(self, AnaMenu):
        _translate = QtCore.QCoreApplication.translate
        AnaMenu.setWindowTitle(_translate("AnaMenu", "Ana Menü"))
        self.pushButton.setText(_translate("AnaMenu", "Alım Yap"))
        self.pushButton_2.setText(_translate("AnaMenu", "Satış Yap"))
        self.pushButton_3.setText(_translate("AnaMenu", "Aksesuar Ekle"))
        self.pushButton_4.setText(_translate("AnaMenu", "Aksesuar Satış"))
        self.pushButton_5.setText(_translate("AnaMenu", "Teknik Servis"))
        self.pushButton_6.setText(_translate("AnaMenu", "Gider"))
        self.pushButton_7.setText(_translate("AnaMenu", "Alım Tablosu"))
        self.pushButton_8.setText(_translate("AnaMenu", "Satış Tablosu"))
        self.pushButton_9.setText(_translate("AnaMenu", "Kar Hesapla"))
        self.pushButton_10.setText(_translate("AnaMenu", "Aksesuar Tablosu"))
        self.pushButton_11.setText(_translate("AnaMenu", "Aksesuar Satış Tablosu"))


