from random import randint 

class Bil:
    def __init__(self, merke, modell, aarsmodell, kilometer, gir, type, pris, url, id):
        self._merke = merke
        self._modell = modell
        self._aarsmodell = aarsmodell
        self._kilometer = kilometer
        self._gir = gir
        self._type = type
        self._pris = int(pris)
        self._url = url
        self._id = id 

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
    
    def hent_id(self):
        return self._id
    
    def verdiokning(self):
        verdiokning = randint(15000,40000)
        self_pris += verdiokning 
        


    def legg_til_bil(self):
        nytt_merke = input("Hvilket merke er bilen?")
        nytt_modell = input("Hvilken modell er bilen?")
        nytt_aarsmodell = input("Hvilken aarsmodell er bilen?")
        nytt_km = input("Hvor mange kilometer har bilen kjørt?")
        nytt_gir = input("Hva slags type gir har bilen?")
        nytt_type = input("Hva slags type drivstoff bruker bilen?")
        nytt_pris = input("Hvor mye koster bilen?")
        url = "ingen url"
        ny_bil = Bil(nytt_merke,nytt_modell,nytt_aarsmodell,nytt_km,nytt_gir,nytt_type,nytt_pris)
        return ny_bil 
    
    


