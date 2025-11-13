def index_bulma(dizi, hedef):
    taban, tavan = 0, len(dizi) - 1

    while taban <= tavan:
        ort_sayi = (taban + tavan) // 2

        if dizi[ort_sayi] == hedef:
            return ort_sayi
        elif dizi[ort_sayi] < hedef:
            taban = ort_sayi + 1
        else:
            tavan = ort_sayi - 1

    return -1

sayilar = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22]
hedef = int(input("Bulmak istediğiniz sayıyı giriniz: "))
sonuc = index_bulma(sayilar, hedef)
print(sonuc)

