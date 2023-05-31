import csv
from bil import Bil

fil = open("biler.csv")
data = fil.read()
linjer = data.split("\n")

alle_biler = []

for linje in linjer[1:-1]:
    splittet_linje = linje.split(";")
    bil = Bil(splittet_linje[0],splittet_linje[1],splittet_linje[2],splittet_linje[3],splittet_linje[4],splittet_linje[5],splittet_linje[6],splittet_linje[7])
    alle_bilerbiler.append(bil)

print(alle_biler[7].return_modell())


storst = [None, 0]


for i in range(1,len(biler)):
    if int(biler[i].return_pris()) > int(storst[1]):
        storst = [biler,biler[i].return_pris()]
#print(storst[0])

Bil.legg_til_bil(self)





  


    





