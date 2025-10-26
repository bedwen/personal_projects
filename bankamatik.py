#Bankamatik

import random


print("=ATM="
      "\n1.Bakiye Sorgulama"
      "\n2.Para Yatırma"
      "\n3.Para Çekme"
      "\n4.Çıkış")


#Bakiye
bakiye = random.randint(1000,10000)

while True:
    secim = int(input("Yapmak istediğiniz işlem: "))
    if secim==1:
        print(f"Bakiyeniz: {bakiye}₺")
    elif secim==2:
        eklenen_para = int(input("Eklemek istediğiniz miktar: "))
        print(f"İlk Bakiyeniz: {bakiye}₺"
              f"\nYeni Bakiyeniz: {bakiye + eklenen_para}₺")
    elif secim==3:
        print("Lütfen çekmek istediğiniz parayı 10'un katları şeklinde yazınız.")
        cekilen_para = int(input("Çekmek istediğiniz miktar: "))
        if (cekilen_para)%10==0:
            print(f"Çekilen para miktarı: {cekilen_para}₺"
                      f"\nİlk Bakiyeniz: {bakiye}₺"
                      f"\nYeni Bakiye: {bakiye - cekilen_para}")
        else:
            print("Lütfen çekmek istediğiniz miktarı 10'un katları halinde giriniz!")
    elif secim==4:
        print("Bankamatikten çıkış yaptınız.")
        break

