class Hayvandunyası() :
    def __init__(self) :
        print("hayvan sınıfındaki init çağıldı.")
    
    def ayaksayısı():
        print("hayvanların ayak sayısı çağıldı.")
    
    

çağırma1=Hayvandunyası()
# ilk çağırmada sorun yok hayvan dünyasındaki init çalışıyor.

class kediler(Hayvandunyası):
    

    def __init__(self) :
        Hayvandunyası.__init__(self)
        print("kediler içersindeki init çağrıldı")

#burada ise hayvandunyasındaki ayaksayısını kullanbiliyorum.eger kedide olsaydı önce kedidekini kullanırdı.
        
        
        
çağırma2=kediler.ayaksayısı()


        



