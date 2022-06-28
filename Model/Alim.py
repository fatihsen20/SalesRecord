class Alim():
    def __init__(self,Imei,Model,AlimTarihi,AlimFiyati,AlimYeri):
        self.Imei = Imei
        self.Model = Model
        self.AlimTarihi = AlimTarihi
        self.AlimFiyati = AlimFiyati
        self.AlimYeri = AlimYeri
    def __str__(self):
        return "Imei: {}, Model: {}, AlimTarihi: {}, AlimFiyati: {}, AlimYeri: {}".format(self.Imei,self.Model,self.AlimTarihi,self.AlimFiyati,self.AlimYeri)
    