
from random import randint


class Eier:
    def __init__(self,navn):
        self._navn = navn 
        self._konto = 1000000
        self._biler = []
        self._salgshistorikk = []
        self._kjopshistorikk = []
    
    def hent_navn(self):
        return self._navn 
    
    def hent_biler(self): 
        return self._biler 
    
    def hent_konto(self):
        return self._konto
    
    def legg_til_bil(self,bil):
        #merke,modell,aarsmodell,kilometer,gir,bil_type,pris,url,bil_id = str(bil[0]),str(bil[1]),str(bil[2]),str(bil[3]),str(bil[4]),str(bil[5]),str(bil[6]),str(bil[7],str(bil[8]))
        #self._biler.append(Bil(merke, modell, aarsmodell, kilometer, gir, bil_type, pris, url,bil_id))
        self._biler.append(bil)
    
    def kjop_bil(self,bil):
        self.legg_til_bil(bil)
        pris = bil.hent_pris()
        self._kjopshistorikk.append([f"({bil.hent_merke()},{bil.hent_modell()},{bil.hent_aarsmodell()})",bil.hent_pris()])
        self._konto -= pris

    def reparer_bil(self,bil):
        kost = randint(5000,20000) 
        print(f"---- Det kostet {kost}kr ----")
        self._konto -= kost
        bil.verdiokning()


    def selg_bil(self,bil):
        self._biler.remove(bil)
        self._salgshistorikk.append([f"({bil.hent_merke()},{bil.hent_modell()},{bil.hent_aarsmodell()})",bil.hent_pris()])
        pris = bil.hent_pris()
        self._konto += pris
    
    def hent_kjop(self):
        return self._kjopshistorikk 
    
    def hent_salg(self):
        return self._salgshistorikk 
    
    

        




