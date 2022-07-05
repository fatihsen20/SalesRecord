from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showAlimTable(object):
    def setupUi(self, showAlimTable):
        showAlimTable.setObjectName("showAlimTable")
        showAlimTable.resize(854, 398)
        self.btn_anamenu = QtWidgets.QPushButton(showAlimTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(390, 360, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.tbl_alim = QtWidgets.QTableWidget(showAlimTable)
        self.tbl_alim.setGeometry(QtCore.QRect(30, 20, 630, 321))
        self.tbl_alim.setObjectName("tbl_alim")
        self.tbl_alim.setColumnCount(6)
        self.tbl_alim.setHorizontalHeaderLabels(["Urun No","IMEI","Model","Alım Tarihi","Alım Fiyatı","Alım Yeri"])
        self.tbl_alim.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.tbl_alim.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.txt_ara = QtWidgets.QLineEdit(showAlimTable)
        self.txt_ara.setGeometry(QtCore.QRect(680, 30, 150, 30))
        self.txt_ara.setObjectName("txt_ara")
        self.txt_ara.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_ara = QtWidgets.QPushButton(showAlimTable)
        self.btn_ara.setGeometry(QtCore.QRect(710, 70, 75, 23))
        self.btn_ara.setObjectName("btn_ara")

        self.retranslateUi(showAlimTable)
        QtCore.QMetaObject.connectSlotsByName(showAlimTable)

    def retranslateUi(self, showAlimTable):
        _translate = QtCore.QCoreApplication.translate
        showAlimTable.setWindowTitle(_translate("showAlimTable", "Alım Tablosu"))
        self.btn_anamenu.setText(_translate("showAlimTable", "AnaMenü"))
        self.txt_ara.setText(_translate("showAlimTable", ""))
        self.btn_ara.setText(_translate("showAlimTable", "Ara"))
        self.txt_ara.setPlaceholderText(_translate("showAlimTable", "Imei veya Ürün Kodu Giriniz"))

