def dogrusal_ara(dizi, hedef):
    for i, eleman in enumerate(dizi):
        if eleman == hedef:
            return i
    return -1

sayilar = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
hedef = 13
sonuc = dogrusal_ara(sayilar, hedef)
print(sonuc)

