from random import randint 

class Bil:
    def __init__(self, merke, modell, aarsmodell, kilometer, gir, bil_type, pris, url):
        self._merke = merke
        self._modell = modell
        self._aarsmodell = aarsmodell
        self._kilometer = kilometer
        self._gir = gir
        self._type = bil_type
        self._pris = int(pris)
        self._url = url

    def hent_merke(self):
        return self._merke

    def hent_modell(self):
        return self._modell

    def hent_aarsmodell(self):
        return self._aarsmodell

    def hent_kilometer(self):
        return self._kilometer

    def hent_gir(self):
        return self._gir

    def hent_type(self):
        return self._type

    def hent_pris(self):
        return self._pris

    def hent_url(self):
        return self._url
    
    def verdiokning(self):
        verdiokning = randint(15000,40000)
        print(f"---- Bilen økte i verdi med {verdiokning}kr")
        self._pris += verdiokning 
    
    def hent_bil(self):
        return f"{self.hent_merke()} {self.hent_modell()} {self.hent_aarsmodell()} "
    
    


