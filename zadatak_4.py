"""Napisati funkciju koja prima kao argument neki cijeli broj,
   računa zbroj njegovih znamenki i vraća taj zbroj."""

def zbroji_znamenke(broj, zbroj=0):
    """Rekurzivna funkcija koja zbraja ostatak"""
    """zbroj += broj%10
    broj /= 10
    if broj == 0:
        return zbroj
    return zbroji_znamenke(int(broj), zbroj)"""

    if broj == 0:
        return 0
    return broj % 10 + zbroji_znamenke(int(broj / 10))

uneseni_broj = int(input("Upiši neki cijeli broj: "))
print(zbroji_znamenke(uneseni_broj))
