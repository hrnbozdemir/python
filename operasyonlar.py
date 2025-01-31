import numpy as np

yenidizi=np.random.randint(1,100,10)
print(yenidizi)

büyükmü=yenidizi>25
print(büyükmü)#dizide 25den büyük olanları bul

print(yenidizi[büyükmü])
#dizide sadece 25den büyük olanları yazdırma
