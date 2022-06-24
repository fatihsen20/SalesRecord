class TeknikServis():
    def __init__(self,Tarih,Islem,Tutar,Maliyet):
        self.Tarih = Tarih
        self.Islem = Islem
        self.Tutar = Tutar
        self.Maliyet = Maliyet
    def __str__(self):
        return f"{self.Tarih} {self.Islem} {self.Tutar} {self.Maliyet}"
