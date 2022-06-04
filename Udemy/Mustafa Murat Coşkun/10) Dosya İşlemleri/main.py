file= open("data.txt","w",encoding="utf-8")           # "w" => Dosya yoksa oluşturur, varsa silip tekrar oluşturur.    <-
file.write("Abdullah Ergül")                          # .write modülü dosyanın içini düzenler.                          |
file.close()                                          # İşi biten dosyayı kapatır.   <-----------------------------------

file= open("data.txt","a",encoding="utf-8")           # "a" => Dosya yoksa oluşturur, varsa üzerine ekleme yapar.
file.write("\nYaş: 20")
file.close()

file= open("data.txt","r")                            # "r" => Dosyayı koda tanıtır, yoksa hata verir.
try:
    file = open("notdata.txt", "r")
except FileNotFoundError:
    print("Dosya Bulunamadı!")
file.close()
print("")

file= open("data.txt","r",encoding="utf-8")           # <---
for i in file:                                        #    |
    print(i,end="")                                   #    |
file.close()                                          #    |--> Dosya içeriğini yazdırma opsiyonları.
print("\n")                                           #    |
                                                      #    |
file= open("data.txt","r",encoding="utf-8")           # <---
print("Dosyanın içeriği:\n{}".format(file.read()))    # <== Dosya .read modülü ile okunursa file parametresi dosyanın sonunda kalır (örneğin 2.kez okumaya izin vermez)
file.close()
print("")

file= open("data.txt","r",encoding="utf-8")
print(file.readline(),end="")                         # <== Dosya .readline modülü ile okunursa bulunduğu satırı okuyup bir sonraki satıra geçecektir.
print(file.readline(),end="")
print("...........",end="")
print(file.readline(),end="")
file.close()
print("\n")

file= open("data.txt","r",encoding="utf-8")
liste= file.readlines()                               # <== Dosya .readlines modülü ile okunursa tüm dosyayı bir array olarak çıkartır.
print(liste)
file.close()
print("")

with open("data.txt","r",encoding="utf-8") as file:   # with bloğu .close modülüne ihtiyaç duymadan dosyayı otomatik kapatır.
    for i in file:
        print(i,end="")
print("\n")

with open("data.txt","r",encoding="utf-8") as file:
    print(file.tell())                                # .tell modülü file değişkeninin nerede olduğunu söyler.
    file.seek(9)                                      # .seek modülü file değişkenini içine girilen değer kadar byte ilerler.
    print(file.tell())
    print(file.read(5))                               # .read modülünün içine atılan değer kadar byte okur.
    print(file.tell())
    file.seek(0)
    print(file.read(8))
print("")

with open("data.txt","r+",encoding="utf-8") as file:  # "r+" dosyayı hem okur hem yazar.
    liste= file.readlines()
    liste.insert(1,"Eastrom ")                        # .intert modülü n. indise ekleme yapar.
    file.seek(0)
    file.writelines(liste)                            # .witelines modülü liste'yi file'nin içerisine aktarır (mevcut verinin üstüne yazar).

