def birlestir(sol, sag):
    sonuc = []
    i = j = 0

    while i < len(sol) and j < len(sag):
        if sol[i] < sag[j]:
            sonuc.append(sol[i])
            i += 1
        else:
            sonuc.append(sag[j])
            j += 1

    sonuc.extend(sol[i:])
    sonuc.extend(sag[j:])
    return sonuc

def birlestirme_siralamasi(dizi):
    if len(dizi) <= 1:
        return dizi

    orta_sayi = len(dizi) // 2
    sol = birlestirme_siralamasi(dizi[:orta_sayi])
    sag = birlestirme_siralamasi(dizi[orta_sayi:])

    return birlestir(sol, sag)

sayilar = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
siralanmis_sayilar = birlestirme_siralamasi(sayilar)
print(siralanmis_sayilar)



