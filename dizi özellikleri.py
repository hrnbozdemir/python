import numpy as np

h=np.random.rand(30)  #5 tane rasgele sayı
print(h)


h=h.reshape(5,6) #5 e 6 lık matrix oluşturdu 
print(h)

print(h.max())   #max ve min değerler
print(h.min())

print(h.argmax()) #kaçıncı sayı max ve min
print(h.argmin())

print(h.shape) #kaça kaçlık matrix




