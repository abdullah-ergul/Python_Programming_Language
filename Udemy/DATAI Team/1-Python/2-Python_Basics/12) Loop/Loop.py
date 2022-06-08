# %% For Loop:

for each in range(1,11):
    print(each)
    
for each in "ankara,intanbul":
    print(each)
    
for each in "ankara istnabul".split():
    print(each)
    
liste = [1,4,5,6,8,3,3,4,67]
count = 0
# ==>
summation = sum(liste) #yada
for each in liste:
    count = count + each
    print(count)
    
    
#%% While Loop:
    
i = 0
while (i < 4):
    print(i)
    i = i + 1
   
liste = [10,4,5,6,8,7,3,4,48]
sinir = len(liste)
each = 0
count = 0
while(each < sinir):
    count = count + liste[each]
    each = each + 1
    print(count)
