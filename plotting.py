import csv
import matplotlib.pyplot as plt
from datetime import datetime


valgt_dato = input("Skriv inn årstall: ")
try:
    datetime.strptime(valgt_dato, "%Y")
except ValueError:
    print("Ugyldig datoformat. Bruk YYYY")
    exit()


with open("sinnes_2014_2025.csv", encoding="UTF-8") as fil:
    leser = csv.DictReader(fil, delimiter=";")
    valgt_dato = int(valgt_dato)
    
    datoer = []
    temperaturer = []
    a_nedbør = []
    vind = []
    snødybder = []
    
    for rad in leser:
        if rad["Tid(norsk normaltid)"] in ["-", ""]:
          continue
        if rad["Middeltemperatur (døgn)"] in ["-",  ""]:
         middeltemperatur = None
        if rad["Nedbør (døgn)"] in ["-", ""]:
         nedbør = None
        if rad["Høyeste middelvind (døgn)"] in ["-", ""]:
           HMvind = None
        if rad["Snødybde"] in ["-", ""]:
         snødybde = None
        
        dato = datetime.strptime(rad["Tid(norsk normaltid)"], "%d.%m.%Y")

        if dato.year == valgt_dato:
              middeltemperatur = rad["Middeltemperatur (døgn)"]  
              middeltemperatur = middeltemperatur.replace(",",".")
              if middeltemperatur == "-":
                middeltemperatur = None
              else: 
                middeltemperatur = float(middeltemperatur)
                                         
              nedbør = rad["Nedbør (døgn)"]  
              nedbør = nedbør.replace(",",".")
              if nedbør == "-":
                 nedbør = None
              else: 
                 nedbør = float(nedbør)
                                          
              HMvind = rad["Høyeste middelvind (døgn)"]  
              HMvind = HMvind.replace(",",".")
              if HMvind == "-":
                 HMvind = None
              else: 
                 HMvind = float(HMvind)
                                          
              snødybde = rad["Snødybde"] 
              snødybde = snødybde.replace(",",".")
              if snødybde == "-":
                 snødybde = None
              else: 
                 snødybde = float(snødybde)
                            
              datoer.append(dato)
              temperaturer.append(middeltemperatur)
              a_nedbør.append(nedbør)
              vind.append(HMvind)
              snødybder.append(snødybde) 

    plt.plot(datoer, temperaturer, label= "Middeltemperatur (døgn)")
    plt.plot(datoer, a_nedbør, label= "Nedbør (døgn)")
    plt.plot(datoer, vind, label = "Høyeste middelvind (døgn)")
    plt.plot(datoer, snødybder, label = "Snødybe")
    plt.xlabel("Dato")
    plt.ylabel("Verdi") 

    plt.legend()
    plt.show()

            

             
              


        







