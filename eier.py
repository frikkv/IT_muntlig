from bil import Bil 
from random import randint


class Eier:
    def __init__(self,navn):
        self._navn = navn 
        self._konto = 1000000
        self._biler = []
    
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
        self._konto -= pris
        return self.hent_konto()

    def reparer_bil(self,bil):
        kost = randint(5000,20000) 
        self._konto -= kost
        bil.verdiokning()


    def selg_bil(self,bil):
        for i in range(len(self._biler)):
            if self._biler.hent_id() == bil.hent_id():
                self._biler.remove(i) 
        pris = bil.hent_pris()
        self._konto += pris
    
    

        




