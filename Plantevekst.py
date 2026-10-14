import csv

Valgt_Årstall = input("Skriv inn et årstall: ")

Minimums_Temperatur = 5
Årlig_vekst = 0
Vekst_Dag = 0

with open("Data/Oppgaver/Innlevering7/Del1/sinnes_2014_2025.csv","r",encoding="utf-8") as fil:

    leser = csv.reader(fil, delimiter=";")
    next(leser)

    for rad in leser:
        Dato = rad[2]
        År_fra_fil = Dato[-4:]

        if År_fra_fil == Valgt_Årstall:
            if rad[3] != "-" and rad[3] != "":
                Temperatur = float(rad[3].replace(",", "."))

                if Temperatur >= 5:

                    Vekst_Dag = Temperatur - Minimums_Temperatur
                    Årlig_vekst += Vekst_Dag

    print(f"Planten har vokst {Årlig_vekst} i året {Valgt_Årstall}")



