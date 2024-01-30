# Bu bölümde yapıcı fonksiyonu (__init__()) kullanmaya başlayacağız
# Çünkü farklı özelliklere sahip nesneler oluşturmak isteyebiliriz
# Örneğin en başta araba üretim yılını belirtmiş olsak, varsayılan olarak, yeni oluşturulan nesneler için aynı yıl olmuş olacak
# Bunu değiştirmek istiyoruz


class ArabaTuru:
    def __init__(self, araba_markasi, araba_renk, araba_yil, vites_otomatikmi):
        self.araba_markasi = araba_markasi
        self.araba_renk = araba_renk
        self.araba_yil = araba_yil
        self.vites_otomatikmi = vites_otomatikmi
    
# Bu sınıftan nesneler oluşturalım

senin_araban = ArabaTuru("Toyota", "Mavi", 2021, True)

onun_arabasi = ArabaTuru("Hacı Murat", "Boz", 1978, False)
