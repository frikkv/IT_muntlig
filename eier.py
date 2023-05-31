
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
        self._biler.append(bil)
    
    def kjop_bil(self,bil):
        """Kjøp av bil

        Args:
            bil (object): selve bilen
        """        
        self.legg_til_bil(bil)
        pris = bil.hent_pris()
        self._kjopshistorikk.append([f"({bil.hent_merke()},{bil.hent_modell()},{bil.hent_aarsmodell()})",bil.hent_pris()]) # Lager en f-string med informasjon om bilen som man appender til en liste
        self._konto -= pris # trekker fra prisen til bilen fra saldoen 

    def reparer_bil(self,bil):
        """Reperasjon av bil

        Args:
            bil (object): selve bilen
        """        
        kost = randint(5000,20000) # Random hvor mye det koster å reparere bilen 
        print(f"---- Det kostet {kost}kr ----")
        self._konto -= kost # Trekker fra kosten av å reparere bilen 
        bil.verdiokning() # sier at den spesifike bilen vi har hentet inn skal kjøre funksjonen verdiokning


    def selg_bil(self,bil):
        """Salg av bil

        Args:
            bil (object): selve bilen
        """        
        self._biler.remove(bil) # Fjerner bilen fra listen med biler som eieren har 
        self._salgshistorikk.append([f"({bil.hent_merke()},{bil.hent_modell()},{bil.hent_aarsmodell()})",bil.hent_pris()]) # Legger til informasjon om bilen i en liste 
        pris = bil.hent_pris()
        self._konto += pris
    
    def hent_kjop(self):
        return self._kjopshistorikk 
    
    def hent_salg(self):
        return self._salgshistorikk 
    
    

        




