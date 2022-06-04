# int diziler
dizi = [40,  1, 2, 3, 4, 5, 6, 7, 8, 9]
print(dizi)
print()

# dizinin N. indisini değiştir
dizi[0] = 0
print(dizi)
print()

# diziyi yazdır
print(dizi)
print()

# dizinin N. indisini yazdır
print(dizi[0])
print()

# dizinin a. indisinden b. indisine kadar yazdır (b hariç)
print(dizi[0:5])
print()

# dizinin 0 dan b. indisine kadar yazdır (b dahil)
print(dizi[:3])
print()

# dizinin a dan sonuncu indisine kadar yazdır (son dahil)
print(dizi[5:])
print()

# dizinin sondan a. indisini yazdır
print(dizi[-1])
print()

# dizi uzunluğu
print(len(dizi))
print()


# str diziler
sdizi = ["elma", "armut", "portakal", "muz"]
print(sdizi)
print()

# yeni eleman ekle
sdizi.append("üzüm")
print(sdizi)
print()

# N. indisi sil
del sdizi[1]              # dizinin N. indisin sil (1. indis armut)
print(sdizi)
print()

sdizi.remove("portakal")  # elemanını sil ("portakal")
print(sdizi)
print()

sdizi.pop(2)              # dizinin N. indisin sil (2. indis üzüm)
print(sdizi)
print()

# diziye yeni elemanlar ekle
sdizi += ["armut", "üzüm", "portakal"]
print(sdizi)
print()

# diziyi kartezyen olarak çarptır
sdizi *= 2
print(sdizi)
print()


sayilar = [21, 34, 56, 21, 78, 23, 67, 90, 21]

# diziyi küçükten büyüğe sırala
sayilar.sort()
print(sayilar)
print()

# diziyi tersine çevir
sayilar.reverse()
print(sayilar)
print()

# dizinin  içideki eleman kaç kez tekrar ettti
a = sayilar.count(21)
print(a)
print()

# diziyi sil
sayilar.clear()
print(sayilar)
print()

# dizinin N. indisine (0) eleman ekle (12)
sayilar.insert(0, 12)
sayilar.insert(1, 34)
print(sayilar)
print()

# dizinin N. indisine eleman ekle (ara eleman olarak ekler. Dizinin mevcut elealarına dokumaz)
sayilar.insert(1, 23)
print(sayilar)
print()


# 2 boyutlu diziler
matris = [[1, 3, 6], [0, 3, 2], [2, 7, 3]]
print(matris)
print()

# matrisin ilk satırını yazdır
print(matris[0])
print()

# matrisin N. satırdaki x. indisini yazdır
print(matris[0][2])
print()
