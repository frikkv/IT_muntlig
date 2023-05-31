import csv
from eier import Eier
from bil import Bil

fil = open("biler.csv")
data = fil.read()
linjer = data.split("\n")

alle_biler = []

n = 0 

for linje in linjer[1:-1]:
    splittet_linje = linje.split(";")
    x = splittet_linje[6].split(" ")
    a = f"{x[0]}{x[1]}"
    bil = Bil(splittet_linje[0],splittet_linje[1],splittet_linje[2],splittet_linje[3],splittet_linje[4],splittet_linje[5],a,splittet_linje[7])
    alle_biler.append(bil)

Thor = Eier("Thor")
assert Thor.hent_navn() == "Thor"
Thor.legg_til_bil(alle_biler[3])
Thor.legg_til_bil(alle_biler[8])
assert Thor.hent_biler()[0].hent_modell() == alle_biler[3].hent_modell()

a = Thor.hent_biler()[1].hent_pris()
Thor.reparer_bil(Thor.hent_biler()[1])
assert Thor.hent_konto() < 1000000
b = Thor.hent_biler()[1].hent_pris()
assert a < b








#storst = [None, 0]
#for i in range(1,len(alle_biler)):
    #if int(alle_biler[i].hent_pris()) > int(storst[1]):
        #storst = [alle_biler,alle_biler[i].hent_pris()]
#print(storst[0])






  


    





