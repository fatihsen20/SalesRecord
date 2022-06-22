class AksesuarSatis():
    def __init__(self,Id,Ad,Tarih,Fiyat):
        self.Id = Id
        self.Ad = Ad
        self.Tarih = Tarih
        self.Fiyat = Fiyat
    def __str__(self):
        return "Id: {}, Ad: {}, Tarih: {}, Fiyat: {}".format(self.Id,self.Ad,self.Tarih,self.Fiyat)