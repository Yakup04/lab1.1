girilen_isim = str(input(""))
isim = "Joseph"
sifre = "W@12"
while True :
     if isim == girilen_isim :
         print("Merhaba {}! Sifre:{}".format(isim,sifre))
     else :
          print("Merhaba {}! Sonra görusuruz".format(girilen_isim))
     break