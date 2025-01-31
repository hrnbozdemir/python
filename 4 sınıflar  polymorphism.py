class elma():
    def __init__(self,isim) :
        self.isim=isim
    def bilgiver(self):
        return self.isim + " 150 kaloridir"
    
elma=elma("elma")


print(elma.bilgiver())
#elma sınıfındaki bilgiyiveri aldı

class armut():
    def __init__(self,isim) :
        self.isim=isim
    def bilgiver(self):
        return self.isim + " 230 kaloridir"
    
armut=armut("armut")

print(armut.bilgiver())
#armut sınıfındaki bilgiveri aldı.

print("----------------------------------------------------")

meyvelistesi=[elma,armut]
for meyve in meyvelistesi:
    print(meyve.bilgiver())

#burada ise ikisinide çağırdı sırasıyla peki ya aşşağıda ise 

print("----------------------------------------------------")

def bilgial(meyve):
    print(meyve.bilgiver())

bilgial(elma)
#girilen meyvenin bilgisini vermekte.
    