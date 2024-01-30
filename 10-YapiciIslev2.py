# Varsayılan (Default) değerler kullanıp kullanmamak bize bağlıdır
# Bütün niteliklere varsayılan değer vermek zorunda değiliz

class ArabaTuru:
    def __init__(self, araba_markasi = None, araba_renk = "Turuncu", araba_yil = 2024, vites_otomatikmi = False):
        self.araba_markasi = araba_markasi
        self.araba_renk = araba_renk
        self.araba_yil = araba_yil
        self.vites_otomatikmi = vites_otomatikmi
    
# Bu sınıftan nesneler oluşturalım

# Default değerleri değiştirmeden bir nesne oluşturalım
senin_araban = ArabaTuru("Toyota") # None olan değere Toyota verdik
#print(senin_araban.araba_markasi) # Toyota olarak çıktı alırız
#print(senin_araban.vites_otomatikmi) # False ile, varsayılan değeri yazdırdık

# Default değerleri değiştirmeyi deneyelim
onun_arabasi = ArabaTuru("Tesla", "Kara", 2022, True)
print(onun_arabasi.araba_markasi) # Tesla
print(onun_arabasi.araba_renk) # Kara
print(onun_arabasi.araba_yil) # 2022
print(onun_arabasi.vites_otomatikmi) # True
