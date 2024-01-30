# Sınıf oluşturma ve sınıf nitelikleri

# Arabanın nitelikleri olarak marka, renk ve yıl örnek olarak yeterli

class ArabaTuru:
    araba_markasi = ""
    araba_renk = ""
    araba_yil = ""
    
    
# Bu sınıftan nesneler (örnek arabalar) oluşturalım

# Arkadaşımız Bilge'nin arabası

bilgenin_arabasi = ArabaTuru()
bilgenin_arabasi.araba_markasi = "Toyota"
bilgenin_arabasi.araba_renk = "Ak"
bilgenin_arabasi.araba_yil = "2022"

# Bu bilgileri ekranda bastıralım

print(f"Arkadaşımız Bilge'nin araba markası {bilgenin_arabasi.araba_markasi}, arabasının rengi {bilgenin_arabasi.araba_renk.lower()} ve arabanın üretim yılı {bilgenin_arabasi.araba_yil}.")

# Arkadaşımız Bilge'nin araba markası Toyota, arabasının rengi ak ve arabanın üretim yılı 2022.

# Başka bir arkadaşımız  içinde ArabaTuru adlı sınıftan nesne (object) oluşturabiliriz. 
