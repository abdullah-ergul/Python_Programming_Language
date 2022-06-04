derece = int(input("Denklemin Derecesi:"))

if (derece == 1):
    a = int(input("X'in Katsayısı:"))
    b = int(input("Denklemin Sabit Sayısı:"))
    x = (-b)/a
    print("Kök : {}".format(x))

elif (derece == 2):
    a = int(input("X^2'nin Katsayısı:"))
    b = int(input("X'in Katsayısı:"))
    c = int(input("Denklemin Sabit Sayısı:"))
    delta = (b**2-4*a*c)
    if (delta < 0):
        print("Denklemin Reel Kökü Bulunmamaktadır.")
    elif (delta == 0):
        x = (-b - delta ** 0.5) / (2 * a)
        print("Kök : {}".format(x))
    elif (delta > 0):
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print("Birinci Kök: {}\nİkinci Kök: {}" .format(x1, x2))

else:
    print("Lütfen 1-2 Arasında Bir Değer Giriniz.")
