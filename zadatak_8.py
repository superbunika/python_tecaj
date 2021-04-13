"""
Učitati vrijednosti iz priložene tekstualne datoteke.
Valjani entry, odnosno red u datoteci predstavlja par vrijednosti odvojenih kosom crtom, sve ostalo odbaciti.
Pronaći par vrijednosti koji ima najveći omjer (prva/druga).
"""

file = open("zadatak_8.txt")

lista = []
omjer = 0
indeks = 0
for row in file:
    if "/" in row:
        prvi = float(row.split("/")[0])
        drugi = float(row.split("/")[1])
        lista.append([prvi,drugi])
file.close()

for i, parovi in enumerate(lista):
    prvi = parovi[0]
    drugi = parovi[1]
    if prvi/drugi > omjer:
        omjer = prvi/drugi
        indeks = i

print(lista[indeks])