vize= int(input("Vize Notunuzu Giriniz: "))
final= int(input("Final Notunuzu Giriniz: "))

ort= vize*0.4 + final*0.6

if ort >= 50:
    print("{} ile Geçtiniz. Tebrikler!".format(ort))
elif ort < 50:
    print("{} ile Kaldınız. Daha çok çalışınız!".format(ort))
else:
    print("Yanlış değer girdiniz.")