# %%  Conditionals:
#İf Else Statement

ver1 = 10
ver2 = 20

if(ver1 > ver2):
    print("ver1 buyuktur ver2")
elif(ver1 == ver2):
    print("ver1 esittir ver2")
else:
    print("ver1 kucuktur ver2")
    
liste = [1,2,3,4,5]

if 6 in liste:
    print("6 degeri listenin icinde")
else:
    print("6 degeri listenin icinde degil")
    
value = 3
if value in liste:
    print("{} degeri listenin icinde".format(value))
else:
    print("{} degeri listenin icinde degil".format(value))