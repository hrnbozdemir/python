import numpy as np
import pandas as pd

dersprog={"dersler":["ders1","ders1","ders4","ders4","ders5"],"dersin hocası":["hoca1","hoca2","hoca4","hoca3","hoca6"],"ders saati":[1,2,3,4,5]}
dersDataFrame=pd.DataFrame(dersprog)
print(dersDataFrame)
dersgroup=dersDataFrame.groupby("dersler")

print(dersgroup.count()) #kaç tane bulunuyor

#print(dersgroup.mean()) #ortalası ne?(girilen değerler int değil )

print(dersgroup.min())

print(dersgroup.describe()) #herşey var
#55

