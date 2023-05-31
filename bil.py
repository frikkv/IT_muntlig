class Bil:
    def __init__(self, merke, modell, aarsmodell, kilometer, gir, type, pris, url):
        self._merke = merke
        self._modell = modell
        self._aarsmodell = aarsmodell
        self._kilometer = kilometer
        self._gir = gir
        self._type = type
        self._pris = pris
        self._url = url

    def return_merke(self):
        return self._merke

    def return_modell(self):
        return self._modell

    def return_aarsmodell(self):
        return self._aarsmodell

    def return_kilometer(self):
        return self._kilometer

    def return_gir(self):
        return self._gir

    def return_type(self):
        return self._type

    def return_pris(self):
        x = self._pris.split(" ")
        a = f"{x[0]}{x[1]}"
        return int(a)

    def return_url(self):
        return self._url

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
    
    


