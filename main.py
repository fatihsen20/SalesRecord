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
from aksesuarSatis_python import Ui_AksesuarSatis
from teknikServis_python import Ui_teknik_servis
from gider_python import Ui_gider
from alimTable_python import Ui_showAlimTable

#Database Object
db_obj = DATABASE()

#Set default date
def set_date(date_object):
    date_object.setDate(QDate.currentDate())

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AnaMenu()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.pushButton2Clicked)
        self.ui.pushButton_3.clicked.connect(self.pushButton3Clicked)
        self.ui.pushButton_4.clicked.connect(self.pushButton4Clicked)
        self.ui.pushButton_5.clicked.connect(self.pushButton5Clicked)
        self.ui.pushButton_6.clicked.connect(self.pushButton6Clicked)
        self.ui.pushButton_7.clicked.connect(self.pushButton7Clicked)

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
    
    def pushButton4Clicked(self):
        dialog = aksesuarSatisWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def pushButton5Clicked(self):
        dialog = teknikServisWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton6Clicked(self):
        dialog = giderWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton7Clicked(self):
        dialog = showAlimTableWindow()
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

        set_date(self.ui.txt_Tarih)
    
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

        set_date(self.ui.txt_SatisTarihi)

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
    
class aksesuarSatisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AksesuarSatis()
        self.ui.setupUi(self)
        self.dialogs = list()

        #Add elements combobox
        self.addComboBox()

        set_date(self.ui.txt_Tarih)

        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_Kaydet.clicked.connect(self.KaydetButtonClicked)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def KaydetButtonClicked(self):
        from AksesuarSatis import AksesuarSatis
        fiyat = int(self.ui.txt_Fiyat.text())
        tarih = self.ui.txt_Tarih.text()
        ad = self.ui.comboBox.currentText()
        id = db_obj.getAksesuarId(ad)

        aksesuarObj = AksesuarSatis(id,ad,tarih,fiyat)
        db_obj.addAksesuarSatisTable(aksesuarObj)
        QMessageBox.about(self,"Kayıt","Kayıt Başarıyla Eklendi!")
        self.AnamenuButtonClicked()

    
    def addComboBox(self):
        comboBox = self.ui.comboBox
        items = db_obj.getAksesuarName()
        for itm in items:
            comboBox.addItem(str(itm))

class teknikServisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_teknik_servis()
        self.ui.setupUi(self)
        self.dialogs = list()

        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_kaydet.clicked.connect(self.KaydetButtonClicked)

        set_date(self.ui.txt_tarih)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def KaydetButtonClicked(self):
        from TeknikServis import TeknikServis
        Tarih = self.ui.txt_tarih.text()
        Islem = self.ui.txt_islem.text()
        Tutar = int(self.ui.txt_tutar.text())
        Maliyet = int(self.ui.txt_maliyet.text())
        
        teknikServis_obj = TeknikServis(Tarih,Islem,Tutar,Maliyet)
        db_obj.addTeknikServisTable(teknikServis_obj)
        QMessageBox.about(self,"Kayıt","Kayıt Başarıyla Eklendi!")
        self.AnamenuButtonClicked()

class giderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_gider()
        self.ui.setupUi(self)
        self.dialogs = list()
    
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_kaydet.clicked.connect(self.KaydetButtonClicked)

        set_date(self.ui.txt_tarih)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def KaydetButtonClicked(self):
        from Gider import Gider
        Tarih = self.ui.txt_tarih.text()
        GiderAdi = self.ui.txt_ad.text()
        Miktar = int(self.ui.txt_miktar.text())
        
        gider_obj = Gider(Tarih,GiderAdi,Miktar)
        db_obj.addGiderTable(gider_obj)
        QMessageBox.about(self,"Kayıt","Kayıt Başarıyla Eklendi!")
        self.AnamenuButtonClicked()

class showAlimTableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_showAlimTable()
        self.ui.setupUi(self)
        self.dialogs = list()
        
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_ara.clicked.connect(self.AraButtonClicked)

        self.setTableData()

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()

    def setTableData(self):
        items = db_obj.getFulldataAlimTable()
        self.ui.tbl_alim.setRowCount(len(items))
        j = 0
        for itm in items:
            self.ui.tbl_alim.setItem(j,0,QTableWidgetItem(str(itm[0])))
            self.ui.tbl_alim.setItem(j,1,QTableWidgetItem(str(itm[1])))
            self.ui.tbl_alim.setItem(j,2,QTableWidgetItem(str(itm[2])))
            self.ui.tbl_alim.setItem(j,3,QTableWidgetItem(str(itm[3])))
            self.ui.tbl_alim.setItem(j,4,QTableWidgetItem(str(itm[4])))
            self.ui.tbl_alim.setItem(j,5,QTableWidgetItem(str(itm[5])))
            j+=1

    def AraButtonClicked(self):
        Id = self.ui.txt_ara.text()
        for row in range(self.ui.tbl_alim.rowCount()):
            if self.ui.tbl_alim.item(row,0).text() == str(Id):
                self.ui.tbl_alim.setCurrentCell(row,0)
                break
        else:
            QMessageBox.about(self,"Hata","Kayıt Bulunamadı!")
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = mainWindow()
    window.show()
    sys.exit(app.exec())