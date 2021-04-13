"""
Učitati vrijednosti iz stupca values iz priložene CSV datoteke
te izračunati aritmetičku sredinu tog stupca zaokruženu na 2. decimalu.
"""

file = open("zadatak_7.csv")
next(file)
lista = [float(row.split(",")[1]) for row in file]
file.close()

average = sum(lista)/len(lista)
print("{:.2f}".format(round(average,2)))
