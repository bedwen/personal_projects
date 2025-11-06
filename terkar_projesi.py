#Öğrenci Yönetim Sistemi

#listeler
numara = []
ad = []
soy_ad = []
vize = []
final = []


def ogrenci_ekle(numara,ad,soy_ad,vize,final):
    numara.append(int(input("Öğrenci numarası: ")))
    ad.append(input("Öğrenci ad: "))
    soy_ad.append(input("Öğrenci soy adı: "))
    vize.append(input("Öğrenici vize notu: "))
    final.append(input("Öğrenci final notu: "))

def not_degistir(numara,vize,final):
    hangi_ogrenci = numara.index(int(input("Notunu değiştirmek istediğiniz öğrencinin numarasını giriniz: ")))
    secim = input("Hangi notu değiştirmek istiyorsunuz? (vize/final)")
    if secim.strip().lower() == "vize":
        yeni_vize_not = int(input("Yeni vize notunu giriniz: "))
        vize.insert(hangi_ogrenci, yeni_vize_not)
        vize.pop(hangi_ogrenci+1)
    elif secim.strip().lower() == "final":
        yeni_final_not = int(input("Yeni final notunu giriniz: "))
        final.insert(hangi_ogrenci, yeni_final_not)
        final.pop(hangi_ogrenci+1)
    else:
        print("Geçerli seçim yapınız!")



def ogrenci_bilgi(numara,ad,soy_ad,vize,final):
    hangi_ogrenci = numara.index(int(input("Bilgisini görmek istediğiniz öğrencinin numarasını giriniz: ")))
    print(f"{numara[hangi_ogrenci]} numaralı öğrencinin;"
          f"\n Adı: {ad[hangi_ogrenci]}"
          f"\n Soy Adı: {soy_ad[hangi_ogrenci]}"
          f"\n Vize Notu: {vize[hangi_ogrenci]}"
          f"\n Final Notu: {final[hangi_ogrenci]}")


print("ÖĞRENCİ BİLGİ SİSTEMİ"
      "\nYapmak istediğiniz işlemi seçiniz"
      "\n1.Öğrenci Ekle"
      "\n2.Not Değiştir"
      "\n3.Öğrenci Bilgi"
      "\n4.Çıkış")

while True:
    secim = int(input("Yapmak istediğinz işlem: "))
    if secim == 1:
        ogrenci_ekle(numara,ad, soy_ad, vize, final)
    elif secim == 2:
        not_degistir(numara,vize,final)
    elif secim == 3:
        ogrenci_bilgi(numara,ad, soy_ad, vize, final)
    elif secim == 4:
        break
    else:
        print("Geçerli seçenek giriniz!")

