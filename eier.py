from bil import Bil 

class Eier:
    def __init__(self,navn):
        self._navn = navn 
        self._konto = 1000000
        self._biler = []
    
    def hent_navn(self):
        return self._navn 
    
    def hent_biler(self): 
        return self._biler 

    def legg_til_biler(self,bil):
        for linje in linjer[1:-1]:
            splittet_linje = linje.split(";")
        self._biler.append(Bil(splittet_linje[0],splittet_linje[1],splittet_linje[2],splittet_linje[3],splittet_linje[4],splittet_linje[5],splittet_linje[6],splittet_linje[7])


