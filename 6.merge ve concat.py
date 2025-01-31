import numpy as np
import pandas as pd

#concat birleştirme

tablo1={"isimler":["ahmet","veli","ayşe"],"puanlar":[25,31,68]}
tablo1DataFrame=pd.DataFrame(tablo1)
print(tablo1DataFrame)
print("----------------------------------------")

tablo2={"isimler":["harun","sinan","karsu"],"puanlar":[7,81,78]}
tablo2DataFrame=pd.DataFrame(tablo2,index=[3,4,5])

Tablobüyük=pd.concat([tablo1DataFrame,tablo2DataFrame],axis=0)

print(Tablobüyük)

#merge kaynaştırma

tablo21={"yazarlar":["ali","veli","deli"],"eserler":["don","ki","şot"]}
tablo22={"yazarlar":["ali","veli","deli"],"takipçi sayısı":[5,3,2],"ortalama puanaları":[56,68,98]}
yazar1DataFrame=pd.DataFrame(tablo21)
yazar2DataFrame=pd.DataFrame(tablo22)

yeniyazar=pd.merge(yazar1DataFrame,yazar2DataFrame,on="yazarlar")
print(yeniyazar)
print("----------------------------------------")



