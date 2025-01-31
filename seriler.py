import numpy as np
import pandas as pd

sonuçlar={"harun":50,"elif":65,"sinan":100}
print(sonuçlar)

#pandas seri kullanımı

print(pd.Series(sonuçlar))
pandassonuç=pd.Series(sonuçlar)
#diğer bir kullanım şekli
kullanıcılar=["harun","elif","sinan"]
puanları=[45,50,78]
print(pd.Series(puanları,kullanıcılar))
sonuçlar2=pd.Series(puanları,kullanıcılar)
sonuçlar3=pd.Series([61,20,35],["harun","elif","sinan"])

numpydizisi=np.array([50,63,96])
print(pd.Series(numpydizisi,kullanıcılar))

#aynı kullanıcıları farklı sonuçları olan iki dizinin toplanması
print("sonuçlar 3 ve sonuçlar 2 nin toplanmış hali")
toplamları=sonuçlar3+sonuçlar2
print(toplamları)

#peki ya eksik veya fazla kullanıcı bulunan bir sonuç listesi ile toplanmaya çalışılsaydı ne olur ?
sonuçlar4=pd.Series([50,97,64,5,37],["harun","berkay","okan","yaren","zehra"])
yenitoplam=sonuçlar3+sonuçlar4
print(yenitoplam)
#eksik  veya fazladan bulunan kullanıcılar nan yani boşluk oluşur.

