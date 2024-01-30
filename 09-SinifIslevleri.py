# Sınıf işlevleri (methods) oluşturalım

# Araba için hızlan, yavaşla ve dur işlevlerini yazalım

# Arabanın başlangıç hızını sıfır olarak kabul edelim. Ki doğal olan:)


class ArabaTuru:
    araba_markasi = ""
    araba_renk = ""
    araba_yil = ""
    araba_hizi = 0
    
    # Her çağrıldığında, araba nesnesini 10 KM hızlandıran işlev
    def araba_hizlan(self):
        self.araba_hizi += 10
        return self.araba_hizi
    
    # Her çağrıldığında, araba nesnesini 10 KM yavaşlatan işlev
    # Araba hızı sıfırdan küçük olabilir mi? 
    def araba_yavaslat(self):
        self.araba_hizi -= 10
        if self.araba_hizi < 0:
            self.araba_hizi = 0
            return self.araba_hizi
        else:
            return self.araba_hizi
        
    # Arabayı durduran bir işlev
    def araba_dur(self):
        self.araba_hizi = 0
        return self.araba_hizi
    
# ArabaTuru sınıfından bir nesne oluşturalım
senin_araban = ArabaTuru()
senin_araban.araba_markasi = "Tesla"
senin_araban.araba_renk = "Mavi"
senin_araban.araba_yil = "2024"

# Arabanı hızlandıralım ve hızını 40 KM'ye çıkartalım. İlgili işlevi 4 defa çalıştırmalıyız.
senin_araban.araba_hizlan()
senin_araban.araba_hizlan()
senin_araban.araba_hizlan()
senin_araban.araba_hizlan()

# Arabanın hızına bakalım
print(senin_araban.araba_hizi) # 40

# Yaya geçidi gördük ve arabayı biraz yavaşlatalım
senin_araban.araba_yavaslat()

# Arabanın hızına bakalım
print(senin_araban.araba_hizi) # 30

# Art arda yavaşlamaya çalışalım. Hız sıfırın altına düşecek mi? 
senin_araban.araba_yavaslat()
senin_araban.araba_yavaslat()
senin_araban.araba_yavaslat()
senin_araban.araba_yavaslat()
senin_araban.araba_yavaslat()

# Arabanın hızına bakalım
print(senin_araban.araba_hizi) # 0

# Şimdi biraz hızlanalım. Ki son işlevi de deneyelim.
senin_araban.araba_hizlan()
print(senin_araban.araba_hizi) # 10

# Önümüze aniden bir kedi atladı ve fren yaptık.
senin_araban.araba_dur()

print(senin_araban.araba_hizi) # 0
