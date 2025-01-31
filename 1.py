import numpy as np
 
 #sırası ile dizi oluşturma

a=list(range(0,10))
print(a)
print(type(a))
b=np.arange(0,10)
print(b)
print(type(b))

print("-------------------------------------")
#-------------------------------------------

#diziyi numpy ile yazmak
dizim=[0,2,5,6]
c=np.array(dizim)
print(c)

print("-------------------------------------")
#-------------------------------------------

#sıfırlardan oluşan dizi ve birlerden oluşan dizi
d=np.zeros((2,2))
print(d)

e=np.ones((2,2))
print(e)

print("-------------------------------------")
#-------------------------------------------

#iki sayı arasını istediğin aralığa bölmek

f=np.linspace(0,25,8)#0 dan 26 yı kadar 8 ya böl
print(f)


print("-------------------------------------")
#-------------------------------------------

#birim basamak matrixi

g=np.eye((3))
print(g)


print("-------------------------------------")
#-------------------------------------------

#random sayı oluşturma

h=np.random.rand(5)  #5 tane rasgele sayı
print(h)


print("-------------------------------------")
#-------------------------------------------

#random sayı int seçme

ı=np.random.randint(0,10,5) #0 dan 10(dahil değil) a 5 sayı geç
print(ı)

print("-------------------------------------")
#-------------------------------------------