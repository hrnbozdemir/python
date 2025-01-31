import numpy as np
import pandas as pd

ilkindexler=["pazartesi","pazartesi","pazartesi","salı","salı","çarşamba","çarşamba","perşembe","cuma"]
ikincindexler=["power elo lab","dalga","otomatik","engineering","dalga","aydınlatma","optic","biyomedikal","power"]
birleşmişindex=list(zip(ilkindexler,ikincindexler))
birleşmişindex=pd.MultiIndex.from_tuples(birleşmişindex)
saatler1=[1.30,3.30,5.30,10.30,3.30,1.30,5.30,4.30,2]
saatler=np.array(saatler1)
print(saatler.shape)
dersler=pd.DataFrame(saatler,index=birleşmişindex,columns=["saat"])
print(dersler)


print(dersler.loc["pazartesi"])

print(dersler.loc["pazartesi"].loc["dalga"])

#pazartesi salı çarş... günlerini içeren başka bir tabloyu birleştirmek için concat kullan.