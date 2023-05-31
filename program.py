import csv
from eier import Eier
from bil import Bil

fil = open("biler.csv")
data = fil.read()
linjer = data.split("\n")

alle_biler = []

n = 0 

for linje in linjer[1:-1]:
    n +=1
    splittet_linje = linje.split(";")
    x = splittet_linje[6].split(" ")
    a = f"{x[0]}{x[1]}"
    bil = Bil(splittet_linje[0],splittet_linje[1],splittet_linje[2],splittet_linje[3],splittet_linje[4],splittet_linje[5],a,splittet_linje[7],n)
    alle_biler.append(bil)

Thor = Eier("Thor")
Thor.legg_til_bil(alle_biler[3])
#Thor.legg_til_bil(alle_biler[8])
#print(Thor.hent_biler)

#print(alle_biler[7].hent_modell())







#storst = [None, 0]
#for i in range(1,len(alle_biler)):
    #if int(alle_biler[i].hent_pris()) > int(storst[1]):
        #storst = [alle_biler,alle_biler[i].hent_pris()]
#print(storst[0])






  


    





