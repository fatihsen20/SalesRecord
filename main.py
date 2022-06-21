import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from DBHandler import DATABASE
from senbilisim_python import Ui_AnaMenu
from alim_python import Ui_AlimTable
from satis_python import Ui_satisTable
from aksesuar_python import Ui_aksesuar

#Database Object
db_obj = DATABASE()

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AnaMenu()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.pushButton2Clicked)
        self.ui.pushButton_3.clicked.connect(self.pushButton3Clicked)
    
    def pushButtonClicked(self):
        dialog = alimWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton2Clicked(self):
        dialog = satisWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton3Clicked(self):
        dialog = aksesuarWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

class alimWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AlimTable()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_kayit.clicked.connect(self.KaydetButtonClicked)
    
    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def KaydetButtonClicked(self):
        from Alim import Alim
        Imei = self.ui.txt_Imei.text()
        Model = self.ui.txt_Model.text()
        AlimTarihi = self.ui.txt_Tarih.text()
        AlimFiyati = self.ui.txt_Fiyat.text()
        AlimYeri = self.ui.txt_Alimyeri.text()

        alimobj = Alim(Imei,Model,AlimTarihi,int(AlimFiyati),AlimYeri)
        db_obj.addAlimTable(alimobj)
        QMessageBox.about(self,"Kayıt","Kayıt Başarıyla Eklendi!")
        self.AnamenuButtonClicked()

class satisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_satisTable()
        self.ui.setupUi(self)
        self.dialogs = list()
        
        #Add elements for combobox
        self.addComboBox()

        #Get elements
        self.ui.comboBox.currentIndexChanged.connect(self.getElements)

        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_kaydet.clicked.connect(self.KaydetButtonClicked)

    def addComboBox(self):
        comboBox = self.ui.comboBox
        items = db_obj.getIdAlimTable()
        for itm in items:
            comboBox.addItem(str(itm))
    
    def getElements(self):
        Imei = self.ui.txt_Imei
        Model = self.ui.txt_Model
        Id = int(self.ui.comboBox.currentText())
        elements = db_obj.getElementAlimTable(Id)
        Imei.setText(elements[1])
        Model.setText(elements[2])
    
    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def KaydetButtonClicked(self):
        from Satis import Satis
        UrunNo = int(self.ui.comboBox.currentText())
        Imei = self.ui.txt_Imei.text()
        Model = self.ui.txt_Model.text()
        SatisTarihi = self.ui.txt_SatisTarihi.text()
        SatisFiyati = int(self.ui.txt_SatisFiyati.text())

        satis_obj = Satis(UrunNo,Model,Imei,SatisTarihi,SatisFiyati)
        db_obj.addSatisTable(satis_obj)
        QMessageBox.about(self,"Kayıt","Kayıt Başarıyla Eklendi!")
        self.AnamenuButtonClicked()

class aksesuarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_aksesuar()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_kaydet.clicked.connect(self.KaydetButtonClicked)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def KaydetButtonClicked(self):
        from Aksesuar import Aksesuar
        AksesuarAdi = self.ui.txt_aksesuar.text()
        AksesuarFiyati = int(self.ui.txt_fiyat.text())

        aksesuar_obj = Aksesuar(AksesuarAdi,AksesuarFiyati)
        db_obj.addAksesuar(aksesuar_obj)
        QMessageBox.about(self,"Kayıt","Kayıt Başarıyla Eklendi!")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = mainWindow()
    window.show()
    sys.exit(app.exec())