import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.DBHandler import DATABASE
from View.py.senbilisim_python import Ui_AnaMenu
from View.py.alim_python import Ui_AlimTable
from View.py.satis_python import Ui_satisTable
from View.py.aksesuar_python import Ui_aksesuar
from View.py.aksesuarSatis_python import Ui_AksesuarSatis
from View.py.teknikServis_python import Ui_teknik_servis
from View.py.gider_python import Ui_gider
from View.py.alimTable_python import Ui_showAlimTable
from View.py.satisTable_python import Ui_showSatisTable
from View.py.kar_python import Ui_kar
from View.py.aksesuarTable_python import Ui_showAksesuar
from View.py.AksesuarSatisTable_python import Ui_aksesuarSatisTable
from View.py.teknikServisTable_python import Ui_teknikServisTable
from View.py.giderTable_python import Ui_giderTable

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
        self.ui.pushButton_8.clicked.connect(self.pushButton8Clicked)
        self.ui.pushButton_9.clicked.connect(self.pushButton9Clicked)
        self.ui.pushButton_10.clicked.connect(self.pushButton10Clicked)
        self.ui.pushButton_11.clicked.connect(self.pushButton11Clicked)
        self.ui.pushButton_12.clicked.connect(self.pushButton12Clicked)
        self.ui.pushButton_13.clicked.connect(self.pushButton13Clicked)

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
    
    def pushButton8Clicked(self):
        dialog = showSatisTableWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton9Clicked(self):
        dialog = karWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton10Clicked(self):
        dialog = showAksesuarTableWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton11Clicked(self):
        dialog = showAksesuarSatisTableWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton12Clicked(self):
        dialog = showTeknikServisTable()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def pushButton13Clicked(self):
        dialog = showGiderTable()
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
        from Model.Alim import Alim
        Imei = self.ui.txt_Imei.text()
        Model = self.ui.txt_Model.text()
        AlimTarihi = self.ui.txt_Tarih.date().toString("yyyy-MM-dd")
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
        from Model.Satis import Satis
        UrunNo = int(self.ui.comboBox.currentText())
        Imei = self.ui.txt_Imei.text()
        Model = self.ui.txt_Model.text()
        SatisTarihi = self.ui.txt_SatisTarihi.date().toString("yyyy-MM-dd")
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
        from Model.Aksesuar import Aksesuar
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
        from Model.AksesuarSatis import AksesuarSatis
        fiyat = int(self.ui.txt_Fiyat.text())
        tarih = self.ui.txt_Tarih.date().toString("yyyy-MM-dd")
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
        from Model.TeknikServis import TeknikServis
        Tarih = self.ui.txt_tarih.date().toString("yyyy-MM-dd")
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
        from Model.Gider import Gider
        Tarih = self.ui.txt_tarih.date().toString("yyyy-MM-dd")
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
        Imei = self.ui.txt_ara.text()
        for row in range(self.ui.tbl_alim.rowCount()):
            if self.ui.tbl_alim.item(row,1).text() == str(Imei):
                self.ui.tbl_alim.setCurrentCell(row,1)
                break
        else:
            QMessageBox.about(self,"Hata","Kayıt Bulunamadı!")

class showSatisTableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_showSatisTable()
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
        items = db_obj.getFulldataSatisTable()
        self.ui.tbl_satis.setRowCount(len(items))
        j = 0
        for itm in items:
            alimInfo = db_obj.getElementAlimTable(itm[0])
            self.ui.tbl_satis.setItem(j,0,QTableWidgetItem(str(itm[0])))
            self.ui.tbl_satis.setItem(j,1,QTableWidgetItem(str(itm[2])))
            self.ui.tbl_satis.setItem(j,2,QTableWidgetItem(str(itm[1])))
            self.ui.tbl_satis.setItem(j,3,QTableWidgetItem(alimInfo[3]))
            self.ui.tbl_satis.setItem(j,4,QTableWidgetItem(itm[3]))
            self.ui.tbl_satis.setItem(j,5,QTableWidgetItem(str(alimInfo[4])))
            self.ui.tbl_satis.setItem(j,6,QTableWidgetItem(str(itm[4])))
            self.ui.tbl_satis.setItem(j,7,QTableWidgetItem(str(alimInfo[5])))
            
            j+=1

    def AraButtonClicked(self):
        Imei = self.ui.txt_ara.text()
        for row in range(self.ui.tbl_satis.rowCount()):
            if self.ui.tbl_satis.item(row,1).text() == str(Imei):
                self.ui.tbl_satis.setCurrentCell(row,1)
                break
        else:
            QMessageBox.about(self,"Hata","Kayıt Bulunamadı!")

class karWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_kar()
        self.ui.setupUi(self)
        self.dialogs = list()
        
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.cmb_ay.currentIndexChanged.connect(self.getElements)
        self.ui.cmb_yil.currentIndexChanged.connect(self.getElements)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def calcSatisProfit(self,month,year):
        satisTableWindow = showSatisTableWindow()
        satisTable = satisTableWindow.ui.tbl_satis
        profit = 0
        for row in range(satisTable.rowCount()):
            if satisTable.item(row,4).text()[6] == month and satisTable.item(row,4).text()[0:4] == year:
                profit += int(satisTable.item(row,6).text()) - int(satisTable.item(row,5).text())
        print(profit)
        self.ui.txt_Satis.setText(str(profit))
        self.ui.txt_Total.setText(str(int(self.ui.txt_Total.text())+int(self.ui.txt_Satis.text())))
    
    def calcAksesuaryProfit(self,month,year):
        aksesuarTableWindow = showAksesuarSatisTableWindow()
        aksesuarTable = aksesuarTableWindow.ui.tbl_AksesuarSatis
        profit = 0
        for row in range(aksesuarTable.rowCount()):
            if aksesuarTable.item(row,2).text()[6] == month and aksesuarTable.item(row,2).text()[0:4] == year:
                profit += int(aksesuarTable.item(row,4).text()) - int(aksesuarTable.item(row,3).text())
        print(profit)
        self.ui.txt_Aksesuar.setText(str(profit))
        self.ui.txt_Total.setText(str(int(self.ui.txt_Total.text())+int(self.ui.txt_Aksesuar.text())))
    
    def calcTeknikServisProfit(self,month,year):
        teknikServisTableWindow = showTeknikServisTable()
        teknikServisTable = teknikServisTableWindow.ui.tbl_teknikservis
        profit = 0
        for row in range(teknikServisTable.rowCount()):
            if teknikServisTable.item(row,1).text()[6] == month and teknikServisTable.item(row,1).text()[0:4] == year:
                profit += int(teknikServisTable.item(row,3).text()) - int(teknikServisTable.item(row,4).text())
        print(profit)
        self.ui.txt_TeknikServis.setText(str(profit))
        self.ui.txt_Total.setText(str(int(self.ui.txt_Total.text())+int(self.ui.txt_TeknikServis.text())))
    
    def getElements(self):
        if self.ui.cmb_ay.currentText() !=None and self.ui.cmb_yil.currentText() !=None:
            self.ui.txt_Total.setText("0")
            self.calcSatisProfit(self.ui.cmb_ay.currentText(),self.ui.cmb_yil.currentText())
            self.calcAksesuaryProfit(self.ui.cmb_ay.currentText(),self.ui.cmb_yil.currentText())
            self.calcTeknikServisProfit(self.ui.cmb_ay.currentText(),self.ui.cmb_yil.currentText())
            

class showAksesuarTableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_showAksesuar()
        self.ui.setupUi(self)
        self.dialogs = list()

        self.setTableData()

        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_ara.clicked.connect(self.AraButtonClicked)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def AraButtonClicked(self):
        item = self.ui.txt_ara.text()
        for row in range(self.ui.tbl_aksesuar.rowCount()):
            if str(item) in self.ui.tbl_aksesuar.item(row,1).text():
                self.ui.tbl_aksesuar.showRow(row)
            else:
                self.ui.tbl_aksesuar.hideRow(row)
    
    def setTableData(self):
        items = db_obj.getFulldataAksesuarTable()
        self.ui.tbl_aksesuar.setRowCount(len(items))
        j = 0
        for itm in items: 
            self.ui.tbl_aksesuar.setItem(j,0,QTableWidgetItem(str(itm[0])))
            self.ui.tbl_aksesuar.setItem(j,1,QTableWidgetItem(str(itm[1])))
            self.ui.tbl_aksesuar.setItem(j,2,QTableWidgetItem(str(itm[2])))
            j+=1

class showAksesuarSatisTableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_aksesuarSatisTable()
        self.ui.setupUi(self)
        self.dialogs = list()

        self.setTableData()

        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_ara.clicked.connect(self.AraButtonClicked)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def AraButtonClicked(self):
        item = self.ui.txt_ara.text()
        for row in range(self.ui.tbl_AksesuarSatis.rowCount()):
            if str(item) in self.ui.tbl_AksesuarSatis.item(row,1).text():
                self.ui.tbl_AksesuarSatis.showRow(row)
            else:
                self.ui.tbl_AksesuarSatis.hideRow(row)
    
    def setTableData(self):
        items = db_obj.getFulldataAksesuarSatisTable()
        self.ui.tbl_AksesuarSatis.setRowCount(len(items))
        j = 0
        for itm in items: 
            alis = db_obj.getAksesuarFiyat(itm[0])
            self.ui.tbl_AksesuarSatis.setItem(j,0,QTableWidgetItem(str(itm[0])))
            self.ui.tbl_AksesuarSatis.setItem(j,1,QTableWidgetItem(str(itm[1])))
            self.ui.tbl_AksesuarSatis.setItem(j,2,QTableWidgetItem(str(itm[2])))
            self.ui.tbl_AksesuarSatis.setItem(j,3,QTableWidgetItem(str(alis)))
            self.ui.tbl_AksesuarSatis.setItem(j,4,QTableWidgetItem(str(itm[3])))
            j+=1

class showTeknikServisTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_teknikServisTable()
        self.ui.setupUi(self)
        self.dialogs = list()

        self.setTableData()
    
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.btn_ara.clicked.connect(self.AraButtonClicked)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def AraButtonClicked(self):
        item = self.ui.txt_ara.text()
        for row in range(self.ui.tbl_teknikservis.rowCount()):
            if str(item) in self.ui.tbl_teknikservis.item(row,2).text():
                self.ui.tbl_teknikservis.showRow(row)
            else:
                self.ui.tbl_teknikservis.hideRow(row)
    
    def setTableData(self):
        items = db_obj.getFulldataTeknikServisTable()
        self.ui.tbl_teknikservis.setRowCount(len(items))
        j = 0
        for itm in items: 
            self.ui.tbl_teknikservis.setItem(j,0,QTableWidgetItem(str(itm[0])))
            self.ui.tbl_teknikservis.setItem(j,1,QTableWidgetItem(str(itm[1])))
            self.ui.tbl_teknikservis.setItem(j,2,QTableWidgetItem(str(itm[2])))
            self.ui.tbl_teknikservis.setItem(j,3,QTableWidgetItem(str(itm[3])))
            self.ui.tbl_teknikservis.setItem(j,4,QTableWidgetItem(str(itm[4])))
            j+=1

class showGiderTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_giderTable()
        self.ui.setupUi(self)
        self.dialogs = list()

        self.setTableData()
        
        self.ui.btn_anamenu.clicked.connect(self.AnamenuButtonClicked)
        self.ui.cmb_ay.currentIndexChanged.connect(self.getElements)
        self.ui.cmb_yil.currentIndexChanged.connect(self.getElements)

    def AnamenuButtonClicked(self):
        dialog = mainWindow()
        self.dialogs.append(dialog)
        dialog.show()
        self.hide()
    
    def setTableData(self):
        items = db_obj.getFulldataGiderTable()
        self.ui.tbl_gider.setRowCount(len(items))
        
        for i in range(len(items)):
            self.ui.tbl_gider.setItem(i,0,QTableWidgetItem(str(items[i][0])))
            self.ui.tbl_gider.setItem(i,1,QTableWidgetItem(str(items[i][1])))
            self.ui.tbl_gider.setItem(i,2,QTableWidgetItem(str(items[i][2])))
            self.ui.tbl_gider.setItem(i,3,QTableWidgetItem(str(items[i][3])))
    
    def calcGider(self,month,year):
        giderTable = self.ui.tbl_gider
        gider = 0

        for row in range(giderTable.rowCount()):
            if giderTable.item(row,1).text()[6] == month and giderTable.item(row,1).text()[0:4] == year:
                gider += int(giderTable.item(row,3).text()) 

        print(gider)
        self.ui.txt_Gider.setText(str(gider))
    
    def getElements(self):
        if self.ui.cmb_ay.currentText() !=None and self.ui.cmb_yil.currentText() !=None:
            self.ui.txt_Gider.setText("0")
            self.calcGider(self.ui.cmb_ay.currentText(),self.ui.cmb_yil.currentText())
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = mainWindow()
    window.show()
    sys.exit(app.exec())