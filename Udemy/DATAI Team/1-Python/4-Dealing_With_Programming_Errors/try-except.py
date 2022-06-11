try:
    file= open("data.txt","r",encoding="utf-8")
except:
    print("Cant Open File")
else:
    file.write("Selam!")
finally:
    file.write("--END OF FILE--")