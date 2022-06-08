# %% Default and Flexible Functions
    
#Default Function: cemberin cevre uzunlugu = 2*pi*r
def cembercevresihesapla(r,pi):
    """
    cember cevresi hesaplayici
    input(parametre): r,pi
    output = cemberin cevresi
    """
    output = 2*pi*r
    return output

#Flexible Function: 
def hesapla1(boy,kilo,*args):
    print(args)
    output = boy+kilo
    return output

#Lambda Function:
def hesapla(x):
    return x*x
sonuc1 = hesapla(3)

sonuc2 = lambda x: x*x
print(sonuc2(3))