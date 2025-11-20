def permutasyon(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permutasyon(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

strListe = "ABC"
n = len(strListe)
a = list(strListe)
permutasyon(a, 0, n - 1)



