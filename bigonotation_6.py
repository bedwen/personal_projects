#fibonacci dizi 0 ve 1 ile başlar her seferinde önceki elemanla toplanır
fibo = [0,1]

for i in range(2,20): #10'u 20 yaparsak ilk 22'i elemanı bulur
    fibo.append(fibo[i-2]+fibo[i-1])

print(fibo)


