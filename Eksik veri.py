import numpy as np
import pandas as pd

#Data Frame oluşturma

havadurumu={"aksaray":[15,35,np.nan],"antalya":[36,np.nan,np.nan],"adana":[75,85,95]}
havadurumuDataFrame=pd.DataFrame(havadurumu)
print(havadurumuDataFrame)

#eksik veriler var ise yoksay

print(havadurumuDataFrame.dropna(axis=0))

# 2 eksik veri ve daha fazlasını alma

print(havadurumuDataFrame.dropna(axis=0,thresh=2))

#axis satır mı sütün mu belirler

# Eksik veri yerine ne yazılsın

print(havadurumuDataFrame.fillna("veri yok"))

