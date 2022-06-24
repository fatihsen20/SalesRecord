class Gider():
    def __init__(self,Tarih,Ad,Miktar):
        self.Tarih = Tarih
        self.Ad = Ad
        self.Miktar = Miktar
    def __str__(self):
        return self.Tarih + " " + self.Ad + " " + str(self.Miktar)