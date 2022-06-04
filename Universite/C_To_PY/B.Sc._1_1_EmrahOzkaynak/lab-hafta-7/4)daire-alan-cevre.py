pi= 3.1415926535


islem= int(input("Dairenin çevresini hesaplamak için 1,\nDairenin alanını hesaplamak için 2 giriniz\n\nYapmak istediğiniz işlem: "))

if islem == 1:
    r= int(input("\nDairenin yarıçapını giriniz: "))
    print("\nDairenin çevresi: {}".format(2*pi*r))
elif islem == 2:
    r = int(input("\nDairenin yarıçapını giriniz: "))
    print("\nDairenin alanı: {}".format(pi * r**2))