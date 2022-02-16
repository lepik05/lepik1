#henri lepik
#harjutus 8
#16.02.22

class auto:
    mark= 'Nissan Neegra'
    aasta= 0
    hind= 0
    varv=0
    kiir=0
    
    def lisaaasta(self,x):
        self.aasta = x
    
    def lisahind(self,x):
        self.hind = x
        
    def lisamark(self,x):
        self.mark = x
    
    def lisavarv(self,x):
        self.varv = x
        
    def lisakiir(self,x):
        self.kiir = x
        
    def kuva(self):
        print(f"{self.mark} {self.aasta} {self.hind} {self.varv} {self.kiir}")

uusobjekt = auto()
uusobjekt.lisamark('Nissan Neegra')
uusobjekt.lisahind("21RUB")
uusobjekt.lisaaasta("1032a")
uusobjekt.lisavarv('sinine')
uusobjekt.lisakiir("14Km/h")
uusobjekt.kuva()

uus = auto()
uus.lisamark('Nissan spedo')
uus.lisahind("25RUB")
uus.lisaaasta("1038a")
uus.lisavarv('kollane')
uus.lisakiir("965Km/h")
uus.kuva()
