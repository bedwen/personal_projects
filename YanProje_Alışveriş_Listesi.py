print('=Alışveriş Listesi=\nListeye ekleme yapmak için: ekle yazınız. \nListeden çıkarma yapmak için: cıkar yazınız.'
      '\nListeyi görmek için: bitti yazınız.\nListeyi temizlemek için: temizle yazınız.')

durum = input("İşlem giriniz: ")
liste = []
if durum == "ekle":
    madde = ""
    while madde != "bitti":
        madde = input("Madde giriniz: ")
        liste.append(madde)
        if durum == "cıkar":
            numara = int(input("Numara giriniz: "))
            del liste[numara-1]
            print(f"Listedeki {numara} numaralı maddeyi sildiniz.")

        elif durum == "temizle":
            liste.clear()
            print("Liste temizlendi.")

    print(f"Alışveriş Listeniz: {liste}")
else:
    print("Geçerli komudu girmediniz.")







