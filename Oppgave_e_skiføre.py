valgt_år = int(input("Skriv inn et årstall: "))

antall_skidager = 0
fil = open("sinnes_2014_2025.csv", encoding="utf-8")
fil.readline()  # hopp over overskriften

for linje in fil:
    kolonner = linje.strip().split(";")
    if len(kolonner) < 7 or kolonner[1] == "":
        continue  # hopp over lisensteksten nederst

    dag, måned, år = kolonner[2].split(".")
    måned = int(måned)
    år = int(år)
    snødybde = kolonner[6]

    if snødybde == "-":
        continue  # snødybde mangler

    i_skisesong = (år == valgt_år - 1 and måned >= 11) or (år == valgt_år and måned <= 5)
    if i_skisesong and float(snødybde) >= 20:
        antall_skidager += 1

fil.close()
print("Antall dager med skiføre:", antall_skidager)