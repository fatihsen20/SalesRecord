class Aksesuar():
    def __init__(self,Ad,Fiyat):
        self.Ad = Ad
        self.Fiyat = Fiyat
    
    def __str__(self):
        return self.Ad + ", " + str(self.Fiyat)