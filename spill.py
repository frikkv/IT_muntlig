import csv
from eier import Eier
from bil import Bil
from random import randint


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


def velg_eier(string):
    for i in range(len(eiere)):
            print(f"---{i+1}. {eiere[i][1]} ---")
    eier_sjekk = int(input(f" {string} (Tall)"))
    valgt_eier = eiere[eier_sjekk-1]
    return valgt_eier



eiere = []
svar = 0
while svar != "Nei" or svar != "nei":
    print("------------------------------------------")
    print("----1. Sjekk biler (0-50)             ----")
    print("----2. Legge til eier (navn)          ----")
    print("----3. Kjøpe en bil (0-50)            ----")
    print("----4. Reparer en bil                 ----")
    print("----5. Selg en bil                    ----")
    print("----6. Informasjon om eier            ----")
    a = input("--- Hva ønsker du å gjøre?            ----")

    if a == "1":
        bilen = int(input("Hvilken bil ønsker du å sjekke? (0-50)"))
        print(f" Merke: {alle_biler[bilen].hent_merke()} \n Modell: {alle_biler[bilen].hent_modell()} \n Årsmodell: {alle_biler[bilen].hent_aarsmodell()} \n Kilometer: {alle_biler[bilen].hent_kilometer()} \n Gir: {alle_biler[bilen].hent_gir()} \n Type: {alle_biler[bilen].hent_type()} \n Pris: {alle_biler[bilen].hent_pris()} \n url: {alle_biler[bilen].hent_url()}")

    if a == "2":
        # Lager person 
        navn = input("Hva heter eieren?")
        eiere.append([Eier(navn),navn])
        gjeldende_eier = len(eiere)-1
        # Legger til to tilfeldige biler til hver nye eier
        eiere[gjeldende_eier][0].legg_til_bil(alle_biler[randint(0,25)])
        eiere[gjeldende_eier][0].legg_til_bil(alle_biler[randint(26,49)])
        print("--- Dette er bilene dine: ---")
        for i in range(2):
            print(f"--- {i+1}. {eiere[gjeldende_eier][0].hent_biler()[i].hent_bil()} ---")



    elif a == "3":  
        # Kjøp bil  
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break
        
        valgt_eier = velg_eier("Hvilken eier ønsker du å kjøpe bil for?")

        bil_onske = input("Ønsker du å kjøpe en bil fra sortimentet vårt (1), eller en annen, egen bil? (2)") 
        if bil_onske == "1":
            # Fra sortimentet 
            bilen = int(input("Hvilken bil vil du kjøpe? (0-50)"))
            valgt_eier[0].kjop_bil(alle_biler[bilen])
            print(f"Du kjøpte bilen: \n Merke: {alle_biler[bilen].hent_merke()} \n Modell: {alle_biler[bilen].hent_modell()} \n Årsmodell: {alle_biler[bilen].hent_aarsmodell()} \n Kilometer: {alle_biler[bilen].hent_kilometer()} \n Gir: {alle_biler[bilen].hent_gir()} \n Type: {alle_biler[bilen].hent_type()} \n Pris: {alle_biler[bilen].hent_pris()} \n url: {alle_biler[bilen].hent_url()}")
            print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr ----")
        elif bil_onske == "2":
            # Annen bil
            merke = input("Merke: ")
            modell = input("Modell: ")
            aarsmodell = input("Årsmodell: ")
            kilometer = input("Kilometer: ")
            gir = input("Gir: ")
            bil_type = input("Type: ")
            pris = input("Pris: ")
            url = input("URL: ")
            valgt_eier[0].kjop_bil(Bil(merke,modell,aarsmodell,kilometer,gir,bil_type,pris,url))
            print(f"---- Gratulerer med kjøp av ny bil! ----\n---- Saldoen din er nå: {valgt_eier[0].hent_konto}kr ----")


        
    elif a == "4":
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break

        valgt_eier = velg_eier("Hvilken eier ønsker du å oppgradere/reparere bilen for?")
        for i in range(len(valgt_eier[0].hent_biler())):
            print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}") # Printer bilene til eieren 
        bil = int(input("Hvilken bil ønsker du å oppgradere/reparere")) -1
        reparere = input("Det vil koste mellom 5000kr-20000kr, og bilen vil øke i verdi med mellom 15000kr-40000kr. Er du sikker på at du vil oppgradere/reparere bilen? ")
        if reparere != "nei" or "Nei":  
            valgt_bil = valgt_eier[0].hent_biler()[bil]
            valgt_eier[0].reparer_bil(valgt_bil)
            print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr   ---- \n---- Bilen er nå verdt: {valgt_bil.hent_pris()}kr  -----")
        else:
            print("---- Bilen ble ikke reparert ----")
     
    elif a == "5":
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break
        valgt_eier = velg_eier("Hvilken eier ønsker du å selge bilen for?")
        for i in range(len(valgt_eier[0].hent_biler())):
            print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}")
        bil = int(input("Hvilken bil ønsker du å selge")) -1
        valgt_bil = valgt_eier[0].hent_biler()[bil]
        vil_du_selge = input(f"Er du sikker på at du vil selge bilen, du tjener {valgt_bil.hent_pris()}kr på salget")
        if vil_du_selge != "nei" or "Nei":  
            valgt_eier[0].selg_bil(valgt_bil) 
            print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()} ----\n----Dine biler er nå:----")
            for i in range(len(valgt_eier[0].hent_biler())):
                print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}")

        else:
            print("---- Bilen ble ikke solgt ---- ")

    elif a == "6":
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break 

        valgt_eier = velg_eier("Hvilken eier ønsker du å få informasjon om?")
        print(f"---- Saldoen til {valgt_eier[1]} er: {valgt_eier[0].hent_konto()} ----\n---- Bilene til {valgt_eier[1]} er: ----")
        print(f"---- Salgshistorikken til {valgt_eier[1]}:")
        for i in range(len(valgt_eier[0].hent_salg())):
            print(f"{valgt_eier[0].hent_salg()[i][0]}, {valgt_eier[0].hent_salg()[i][1]}")
        print(f"---- Kjøpshistorikk til {valgt_eier[1]}:")
        for i in range(len(valgt_eier[0].hent_kjop())):
            print(f"{valgt_eier[0].hent_kjop()[i][0]}, {valgt_eier[0].hent_kjop()[i][1]}")
        for i in range(len(valgt_eier[0].hent_biler())):
                print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}")
        

    svar = input("Vil du fortsette?")
        

