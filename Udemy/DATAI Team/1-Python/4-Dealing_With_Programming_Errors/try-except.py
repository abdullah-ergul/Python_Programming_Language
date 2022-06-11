try:
    filea= open("data.txt","r")
except:
    print("Cant Open File")
else:
    print("Selam!")
finally:
    print("--END OF FILE--")