m1 = [[2, 0,  3],
      [4, 5, 2],
      [7, 0, 1]]

# matrisin N. satırını yazdırma
print(m1[0])
print()

# matrisin her bir satırıı yazdır
for i in range(3):
    print(m1[i])
print()

m2 = [[0, 1, 4],
      [0, 1, 2],
      [0, 1, 1]]

for i in range(3):
    print(m2[i])
print()

m3 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

# 2 matrisin aynı satır ve aynı indislerindeki sayıları toplayıp yeni bir öatris oluştur
for i in range(3):
    for j in range(3):
        m3[i][j] = m1[i][j] + m2[i][j]

for i in range(3):
    print(m3[i])
