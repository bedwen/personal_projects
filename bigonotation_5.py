def bubble_sirala(dizi):
    n = len(dizi)
    for i in range(n):
        for j in range(n - i - 1):
            if dizi[j] > dizi[j + 1]:
                dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]

sayilar = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
bubble_sirala(sayilar)
print(sayilar)