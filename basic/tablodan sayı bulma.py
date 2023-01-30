import numpy as np
 
row = int(input("Satır sayısını giriniz: "))
column = int(input("Sütün sayısını giriniz: "))
y = int(input("Bulmak istediğniz sayısı giriniz: "))

x = np.random.randint(1,100,size=(row,column))

z = np.where(x == y)
print(x)
print(z)



