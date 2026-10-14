import csv
import matplotlib.pyplot as plt
from datetime import datetime


valgt_dato = input("Skriv inn årstall: ")
try:
    datetime.strptime(valgt_dato, "%Y")
except ValueError:
    print("Ugyldig datoformat. Bruk YYYY")
    exit()


with open("DAT120/Øving 7/sinnes_2014_2025_med_makstemperatur.csv", encoding="UTF-8") as fil:
    leser = csv.DictReader(fil, delimiter=";")
    valgt_dato = int(valgt_dato)

    sommerdag = 0
    HøySdag = 0
    tropedag = 0

    
    for rad in leser:
        if rad["Tid(norsk normaltid)"] in ["-", ""]:
         continue
        maks_temp = rad["Maksimumstemperatur (døgn)"]
        maks_temp = maks_temp.replace(",", ".")
        if maks_temp in ["-", ""]:
         maks_temp = 0

        dato = datetime.strptime(rad["Tid(norsk normaltid)"], "%d.%m.%Y")
        
        if dato.year == valgt_dato:
            maks_temp = float(maks_temp)

            if maks_temp >= 20:
                sommerdag += 1

            if maks_temp >= 25:
                HøySdag += 1

            if maks_temp >= 30:
                tropedag += 1

    print(sommerdag)
    print(HøySdag)
    print(tropedag)