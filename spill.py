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
    """Valg av hvilken eier som skal utføre ting

    Args:
        string (string): Spør om hvilken eier man ønsker å jobbe med

    Returns:
        string: Returneren den valgte eieren
    """    
    for i in range(len(eiere)):
            print(f"---{i+1}. {eiere[i][1]} ---") # i starter på 0, da må man legge til en for at tallet ved siden av eieren i terminalen skal være riktig 
    eier_sjekk = int(input(f" {string} (Tall)")) # Skriver string slik at man kan ha ulike spørsmål for hver av handlingene, velger hvilken eier
    valgt_eier = eiere[eier_sjekk-1] # slik at nummeret i terminalen skal stemme med nummer man skriver inn må det trekkes fra en fra inputen fordi man plusset på en i stad. 
    return valgt_eier



eiere = []
svar = 0
while svar != "Nei" or svar != "nei":
    print("------------------------------------------")
    print("----1. Sjekk biler (0-50)             ----")
    print("----2. Legge til eier (navn)          ----")
    print("----3. Kjøpe en bil (0-50)            ----")
    print("----4. Reparere en bil                 ----")
    print("----5. Selg en bil                    ----")
    print("----6. Informasjon om eier            ----")
    print("----7. Kjør et race                   ----")
    a = input("--- Hva ønsker du å gjøre?            ----")

    if a == "1":
        bilen = int(input("Hvilken bil ønsker du å sjekke? (0-50)"))
        print(f" Merke: {alle_biler[bilen].hent_merke()} \n Modell: {alle_biler[bilen].hent_modell()} \n Årsmodell: {alle_biler[bilen].hent_aarsmodell()} \n Kilometer: {alle_biler[bilen].hent_kilometer()} \n Gir: {alle_biler[bilen].hent_gir()} \n Type: {alle_biler[bilen].hent_type()} \n Pris: {alle_biler[bilen].hent_pris()} \n url: {alle_biler[bilen].hent_url()}")
        # printer all informasjon om bilen 
    if a == "2":
        # Lager person 
        navn = input("Hva heter eieren?")
        eiere.append([Eier(navn),navn]) # Lager en eier med navn: navn og legger den til i listen over eiere, legger til en liste inni lista, [0] vil være eieren som et objetk [1] vil være eierens navn
        # Ved å ha en liste inni lista med eiere gjør at man kan bruke navnet til eieren senere ved å skrive valgt_eier[1]
        gjeldende_eier = len(eiere)-1 # gjeldene eier vil være posisjonen til den siste eieren i listen 
        # Legger til to tilfeldige biler til hver nye eier
        eiere[gjeldende_eier][0].legg_til_bil(alle_biler[randint(0,25)])
        eiere[gjeldende_eier][0].legg_til_bil(alle_biler[randint(26,49)])
        print("--- Dette er bilene dine: ---")
        for i in range(2):
            print(f"--- {i+1}. {eiere[gjeldende_eier][0].hent_biler()[i].hent_bil()} ---") # i+1 fordi 1 starter med null, gjeldene_eier[0] for å referere til objektet ikke navnet, navnet ville ha vært gjeldende_eier[1]



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
            valgt_eier[0].kjop_bil(alle_biler[bilen]) # objektet eier kaller på funksjonen kjop_bil(), fra listen av alle biler velger eieren å kjøpe bil nummer (bilen). 
            print(f"Du kjøpte bilen: \n Merke: {alle_biler[bilen].hent_merke()} \n Modell: {alle_biler[bilen].hent_modell()} \n Årsmodell: {alle_biler[bilen].hent_aarsmodell()} \n Kilometer: {alle_biler[bilen].hent_kilometer()} \n Gir: {alle_biler[bilen].hent_gir()} \n Type: {alle_biler[bilen].hent_type()} \n Pris: {alle_biler[bilen].hent_pris()} \n url: {alle_biler[bilen].hent_url()}")
            print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr ----")
        elif bil_onske == "2":
            # Annen bil
            # lager inputer for alle elementene som må med i bilen
            merke = input("Merke: ")
            modell = input("Modell: ")
            aarsmodell = input("Årsmodell: ")
            kilometer = input("Kilometer: ")
            gir = input("Gir: ")
            bil_type = input("Type: ")
            pris = input("Pris: ")
            url = input("URL: ")
            valgt_eier[0].kjop_bil(Bil(merke,modell,aarsmodell,kilometer,gir,bil_type,pris,url))  # lager en bil ut i fra inputene
            print(f"---- Gratulerer med kjøp av ny bil! ----\n---- Saldoen din er nå: {valgt_eier[0].hent_konto}kr ----")


        
    elif a == "4":
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break

        valgt_eier = velg_eier("Hvilken eier ønsker du å oppgradere/reparere bilen for?")
        for i in range(len(valgt_eier[0].hent_biler())): # må ha in range for å bruke i senere, printer alle bilene til eieren
            print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}") # Printer bilene til eieren 
        bil = int(input("Hvilken bil ønsker du å oppgradere/reparere")) -1 # må ha minus en fordi man har tatt i+1 tidligere, nummeret man skriver inn må stemme med det i terminalen
        reparere = input("Det kan koste mellom 5000kr-20000kr, og bilen kan øke i verdi med mellom 15000kr-40000kr. Jo eldre bilen din er, jo farligere er det å reparere den. Er du sikker på at du vil oppgradere/reparere bilen? ")
        if reparere != "nei" or "Nei":  
            valgt_bil = valgt_eier[0].hent_biler()[bil]
            aarstall = valgt_bil.hent_aarsmodell()
            if int(aarstall) < 2000:
                if randint(0,10) == 20: # 10 prosent sjanse for en dårlig reperasjon
                    valgt_eier[0].bad_reparer(valgt_bil)
                    print(f"---- Søren! Reperasjonen gikk dårlig! {valgt_eier[1]} tapte 20 000kr og bilen ble ikke fikset! ----\n---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr   ---- \n---- Bilen er nå verdt: {valgt_bil.hent_pris()}kr  -----")
                else:
                    valgt_eier[0].reparer_bil(valgt_bil)
                    print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr   ---- \n---- Bilen er nå verdt: {valgt_bil.hent_pris()}kr  -----")
            elif int(aarstall) < 2010:
                if randint(0,20) == 100: # 5 prosent sjanse for en dårlig reperasjon
                    valgt_eier[0].bad_reparer(valgt_bil)
                    print(f"---- Søren! Reperasjonen gikk dårlig! {valgt_eier[1]} tapte 20 000kr og bilen ble ikke fikset! ----\n---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr   ---- \n---- Bilen er nå verdt: {valgt_bil.hent_pris()}kr  -----")
                else:
                    valgt_eier[0].reparer_bil(valgt_bil)
                    print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr   ---- \n---- Bilen er nå verdt: {valgt_bil.hent_pris()}kr  -----")
            elif int(aarstall) < 2023:
                if randint(0,100) == 20: # 1 prosent sjanse for en dårlig reperasjon
                    valgt_eier[0].bad_reparer(valgt_bil)
                    print(f"---- Søren! Reperasjonen gikk dårlig! {valgt_eier[1]} tapte 20 000kr og bilen ble ikke fikset! ----\n---- Saldoen din er nå: {valgt_eier[0].hent_konto()}kr   ---- \n---- Bilen er nå verdt: {valgt_bil.hent_pris()}kr  -----")
                else:
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
            print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}") # eieren som et objekt kaller på funksjonen hent_biler[i], for å hente en spesifik bil fra listen av bilene til eieren. så kalles funksjonen hent_bil() for å hente litt informasjon om bilen
        bil = int(input("Hvilken bil ønsker du å selge")) -1
        valgt_bil = valgt_eier[0].hent_biler()[bil]
        vil_du_selge = input(f"Er du sikker på at du vil selge bilen, du tjener {valgt_bil.hent_pris()}kr på salget")
        if vil_du_selge != "nei" or "Nei":  
            valgt_eier[0].selg_bil(valgt_bil) 
            print(f"---- Saldoen din er nå: {valgt_eier[0].hent_konto()} ----\n----Dine biler er nå:----")
            for i in range(len(valgt_eier[0].hent_biler())):
                print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}") # printer alle bilene til eieren of litt informasjon om dem

        else:
            print("---- Bilen ble ikke solgt ---- ")

    elif a == "6":
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break 

        valgt_eier = velg_eier("Hvilken eier ønsker du å få informasjon om?")
        print(f"---- Saldoen til {valgt_eier[1]} er: {valgt_eier[0].hent_konto()} ----\n---- Bilene til {valgt_eier[1]} er: ----") # bruker eieren sitt navn istedenfor eier som objekt ved å skrive [1]
        for i in range(len(valgt_eier[0].hent_biler())):
                print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}") # printer alle bilene til eieren
        print(f"---- Salgshistorikken til {valgt_eier[1]}:")
        for i in range(len(valgt_eier[0].hent_salg())): # for lengden på listen salgshistorikk skal man printe alt i listen
            print(f"{valgt_eier[0].hent_salg()[i][0]}, {valgt_eier[0].hent_salg()[i][1]}") # siden det er en liste med en f-string og en strng må man printe både [0] og [1] for å printe alt
        print(f"---- Kjøpshistorikk til {valgt_eier[1]}:")
        for i in range(len(valgt_eier[0].hent_kjop())):
            print(f"{valgt_eier[0].hent_kjop()[i][0]}, {valgt_eier[0].hent_kjop()[i][1]}")
    
    elif a == "7":
        if len(eiere) == 0:
            print("Du må lage en eier først!") 
            break 
        valgt_eier = velg_eier("Hvilken eier ønsker du å kjøre et race for?")
        for i in range(len(valgt_eier[0].hent_biler())):
            print(f"{i+1}. {valgt_eier[0].hent_biler()[i].hent_bil()}") # eieren som et objekt kaller på funksjonen hent_biler[i], for å hente en spesifik bil fra listen av bilene til eieren. så kalles funksjonen hent_bil() for å hente litt informasjon om bilen
        bil = int(input("Hvilken bil ønsker du å kjøre race med?")) -1
        valgt_bil = valgt_eier[0].hent_biler()[bil]
        valgt_eier[0].race_konto(valgt_bil) 



    svar = input("Vil du fortsette?")
        

