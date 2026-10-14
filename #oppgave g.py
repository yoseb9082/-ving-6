import csv
import os
from datetime import datetime, timedelta

script_mappe = os.path.dirname(os.path.abspath(__file__))
filnavn = os.path.join(script_mappe, "sinnes_2014_2025 2.csv")

datoer = []
nedbor = []

with open(filnavn, newline="", encoding="utf-8-sig") as fil:
    leser = csv.reader(fil, delimiter=";")
    next(leser)

    for rad in leser:
        if len(rad) < 5:
            continue

        try:
            dato = datetime.strptime(rad[2], "%d.%m.%Y").date()
        except ValueError:
            continue

        nedbor_tekst = rad[4].replace(",", ".")
        try:
            verdi = float(nedbor_tekst)
        except ValueError:
            verdi = None

        datoer.append(dato)
        nedbor.append(verdi)

antall = len(datoer)
for i in range(antall):
    for j in range(antall - 1 - i):
        if datoer[j] > datoer[j + 1]:
            temp = datoer[j]
            datoer[j] = datoer[j + 1]
            datoer[j + 1] = temp
            temp = nedbor[j]
            nedbor[j] = nedbor[j + 1]
            nedbor[j + 1] = temp

lengste_lengde = 0
lengste_start = None
lengste_slutt = None

gjeldende_lengde = 0
gjeldende_start = None
forrige_dato = None

for i in range(antall):
    dato = datoer[i]
    verdi = nedbor[i]

    er_tørr_dag = (verdi is not None and verdi == 0.0)
    er_påfølgende_dag = (forrige_dato is not None and dato == forrige_dato + timedelta(days=1))

    if er_tørr_dag and gjeldende_lengde > 0 and er_påfølgende_dag:
        gjeldende_lengde = gjeldende_lengde + 1
    elif er_tørr_dag:
        gjeldende_lengde = 1
        gjeldende_start = dato
    else:
        gjeldende_lengde = 0
        gjeldende_start = None

    if gjeldende_lengde > lengste_lengde:
        lengste_lengde = gjeldende_lengde
        lengste_start = gjeldende_start
        lengste_slutt = dato

    forrige_dato = dato

print("Lengste sammenhengende periode uten nedbør:", lengste_lengde, "dager")
print("Startdato:", lengste_start.strftime("%d.%m.%Y"))
print("Sluttdato:", lengste_slutt.strftime("%d.%m.%Y"))