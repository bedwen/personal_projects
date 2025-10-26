import random


print("=Şifre Oluşturucusu="
      "\n1-Büyük Harf"
      "\n2-Küçük Harf"
      "\n3-Rakam"
      "\n4-Özel Karakter"
      "\n5-Oluştur"
      "\nŞifrenizde olmasını istediğiniz seçenekleri numaraları ile seçiniz.")

uzunluk = int(input("Şifre uzunluğunu giriniz: ")) #Kullanıcıdan input almak.
rakam=list("0123456789")
buyuk_h=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
kucuk_h=list("abcdefghijklmnopqrstuvwxyz")
ozel_k=list("!@#$%^&*")
sifre_listesi=[]

while(1): #Kullanıcıdan input alarak aldığımız veriyi işleyerek değerlere atamak.
    secim = int(input("Listeden seçim yapınız: "))
    if(secim==1):
        sifre_listesi.extend(buyuk_h)
    elif(secim==2):
        sifre_listesi.extend(kucuk_h)
    elif(secim==3):
        sifre_listesi.extend(rakam)
    elif(secim==4):
        sifre_listesi.extend(ozel_k)
    elif(secim==5):
        break
    else:
        print("Lütfen geçerli seçeneklerde seçim yapınız.") #Kullanıcının inputlarını denetlemek ve feedback vermek.

sifre=[]
for i in range(uzunluk): #Atadığımız değerler ile şifre oluşturuyoruz.
    random_karakterler = random.choice(sifre_listesi)
    sifre.append(random_karakterler)
print("Şifreniz: ","".join(sifre)) #Oluşturduğumuz şifreyi output ediyoruz.




