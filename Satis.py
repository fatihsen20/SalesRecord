class Satis():
    def __init__(self,Urun_Id,Urun,Imei,Tarih,Fiyat):
        self.Urun_Id = Urun_Id
        self.Urun = Urun
        self.Imei = Imei
        self.Tarih = Tarih
        self.Fiyat = Fiyat
    def __str__(self):
        return "Urun_Id: {}, Urun: {}, Imei: {}, Tarih: {}, Fiyat: {}".format(self.Urun_Id,self.Urun,self.Imei,self.Tarih,self.Fiyat)