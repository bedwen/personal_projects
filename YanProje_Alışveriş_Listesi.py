#def alıştırması için def kullanılarak yazılmıştır

print('=Alışveriş Listesi='
      '\nListeye ekleme yapmak için: 1'
      '\nListeden çıkarma yapmak için: 2'
      '\nListeyi görmek için: 3'
      '\nListeyi temizlemek için: 4'
      '\nÇıkış yapmak için: 5')

liste = []

def ekle():
    eklenen_madde = input("Madde giriniz: ")
    liste.append(eklenen_madde)
    print(f"Alışveriş Listeniz: {liste}")


def sil():
    silinen_madde = int(input("Silmek istediğiniz madde: "))
    liste.pop(silinen_madde+1)
    print(f"Alışveriş Listeniz: {liste}")


def goster():
    print(f"Alışveriş Listeniz: {liste}")


def temizle():
    liste.clear()
    print("Liste tamamen temizlendi.")

while True:
    secim = int(input("Seçenek: "))
    if secim==1:
        ekle()

    elif secim==2:
        sil()

    elif secim==3:
        goster()

    elif secim==4:
        temizle()

    elif secim==5:
        break

    else:
        print("Geçerli seçenek giriniz!")









