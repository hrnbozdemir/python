import pandas as pd
import numpy as np

data=np.random.randn(3,2)

dataframe=pd.DataFrame(data)
print(dataframe)

print(type(dataframe))

#data Frame in indec ve colonları değiştirme
yenidataframe=pd.DataFrame(data,index=["hasan","samet","mami"],columns=["yemek mıktarı","saat"])
print(yenidataframe)

#sütun alma
print(yenidataframe["yemek mıktarı"])

#satır alma
print(yenidataframe.loc["hasan"])

#yeni columns ekleme
yenidataframe["uyku"]=24-yenidataframe["saat"]
print(yenidataframe)

#columns çıkarma(geçici olarak)
print(yenidataframe.drop("saat",axis= 1,inplace=False))

#columns çıkarma(kalıcı olarak)
print(yenidataframe.drop("saat",axis= 1,inplace=True))

#veriyi seçme
print(yenidataframe.loc["hasan","uyku"])

#büyüklük küçüklük
print(yenidataframe>0)
print(yenidataframe[yenidataframe>0])

#filtremeleme
print(yenidataframe[yenidataframe["uyku"]>23.5])


#index değiştirme sıfırlamak (kalıcı olması için inplace=true)
print(yenidataframe.reset_index())


#index değiştirmek (kalıcı olması için inplace=true)
yenidataframe["yenı"]=["berkay","toprak","mahir"]
print(yenidataframe.set_index("yenı"))

