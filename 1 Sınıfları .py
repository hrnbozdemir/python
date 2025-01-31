class Benimakrdaşlarım():
    def __init__(self,sevgiderecesiinput,nezamandırinput,iyimiinput) :
        print("init çağrıldı")
        self.sevgiderece=sevgiderecesiinput
        self.nezamandır=nezamandırinput
        self.iyimi=iyimiinput
        #self burada benim arkdaşlarım adındak, sınıfı kullanırken özellik olarak sevgi derecesi 
        # veya ne zamandır özellikleri gibi özellikleri kullanmamı sağlıyor.

sinan=Benimakrdaşlarım("az","3.sınıftan beri","idare eder")


print(f" sinan ne kadar iyi bir insan {sinan.iyimi}")
print(f" sinanı ne zamandır tanıyorsun {sinan.nezamandır}")
print(f"sinan ne kadar sevilebilir bir insan {sinan.sevgiderece}")




def ornekmethod ():
    print( f"deneme 1 2  {self.sevgiderece}")

        #aşka bir ethottan parametre alabilmek için 
ornekmethod()
