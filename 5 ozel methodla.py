

#özel methotlar 


class meyve ():
    def __init__(self,isim,kalori) -> None:
        self.isim=isim
        self.kalori=kalori
    
    def __str__(self) -> str:
        return f"{self.isim} kalori miktarı: {self.kalori}"
    # <__main__.meyve object at 0x00000223EBB24610> hatası alınır olmaz ise

    def __len__(self):
        return self.kalori
    # aşşağıdaki len komutunun çalışması için


muz=meyve("muz",250)

print(muz) #print ile yazdırılırken


print(len(muz))

