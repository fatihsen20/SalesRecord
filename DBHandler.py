import pyodbc 
from Alim import Alim 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-77IR8J7;'
                      'Database=Satis;'
                      'Trusted_Connection=yes;')

class DATABASE():
    def __init__(self):
        self.conn = conn
        self.cursor = conn.cursor()
    
    def addAlimTable(self,alimobj):
        print(alimobj.__str__())
        self.cursor.execute("INSERT INTO tbl_Alim (IMEI,Marka,AlimTarihi,AlimFiyati,AlimYeri) VALUES (?,?,?,?,?)",
        alimobj.Imei,alimobj.Model,alimobj.AlimTarihi,alimobj.AlimFiyati,alimobj.AlimYeri)
        self.conn.commit()
    
    def getElementAlimTable(self,Id):
        self.cursor.execute("SELECT * FROM tbl_Alim WHERE UrunId = ?",Id)
        row = self.cursor.fetchone()
        return row
    
    def getIdAlimTable(self):
        my_list = []
        self.cursor.execute("SELECT UrunId FROM tbl_Alim")
        for row in self.cursor.fetchall():
            my_list.append(row[0])
        return my_list
    
    def addSatisTable(self,satisobj):
        print(satisobj.__str__())
        self.cursor.execute("INSERT INTO tbl_Satis (Urun_Id,Urun,IMEI,Tarih,Satis_Fiyati) VALUES (?,?,?,?,?)",
        satisobj.Urun_Id,satisobj.Urun,satisobj.Imei,satisobj.Tarih,satisobj.Fiyat)
        self.conn.commit()
    
    def addAksesuar(self,aksesuarobj):
        print(aksesuarobj.__str__())
        self.cursor.execute("INSERT INTO tbl_Aksesuar (Ad,AlisFiyati) VALUES (?,?)",
        aksesuarobj.Ad,aksesuarobj.Fiyat)
        self.conn.commit()
    
    def getAksesuarName(self):
        my_list = []
        self.cursor.execute("SELECT Ad from tbl_Aksesuar")
        for row in self.cursor.fetchall():
            my_list.append(row[0])
        return my_list
    
    def getAksesuarId(self,name):
        self.cursor.execute("SELECT Id from tbl_Aksesuar WHERE Ad = ?", name)
        row = self.cursor.fetchone()
        return row[0]
    
    def addAksesuarSatisTable(self,aksesuarobj):
        print(aksesuarobj.__str__())
        self.cursor.execute("INSERT INTO tbl_AksesuarSatis (Aksesuar_Id,Aksesuar_Adi,Tarih,Aksesuar_Satis) VALUES (?,?,?,?)",
        aksesuarobj.Id,aksesuarobj.Ad,aksesuarobj.Tarih,aksesuarobj.Fiyat)
        self.conn.commit()
    
    def addTeknikServisTable(self,teknikServisobj):
        print(teknikServisobj.__str__())
        self.cursor.execute("INSERT INTO tbl_TeknikServis (Tarih,Islem,Tutar,Maliyet) VALUES (?,?,?,?)",
        teknikServisobj.Tarih,teknikServisobj.Islem,teknikServisobj.Tutar,teknikServisobj.Maliyet)
        self.conn.commit()  

    def addGiderTable(self,giderobj):
        print(giderobj.__str__())
        self.cursor.execute("INSERT INTO tbl_Gider (Tarih,GiderAdi,GiderMiktari) VALUES (?,?,?)",
        giderobj.Tarih,giderobj.Ad,giderobj.Miktar)
        self.conn.commit()
    
    def getFulldataAlimTable(self):
        self.cursor.execute("SELECT * FROM tbl_Alim")
        rows = self.cursor.fetchall()
        return rows


# db = DATABASE()
# print(db.getFulldataAlimTable())