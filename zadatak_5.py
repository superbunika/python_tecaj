"""Napisati funkciju koja će uzeti string kao argument i svaku drugu riječ
   u tom stringu preokrenuti (te vratiti takav, modificirani string)."""

def funkcija(recenica):
    """Funkcija"""

    rijeci_list = recenica.split(" ")
    recenica = ""

    for i, rijec in enumerate(rijeci_list):
        if i % 2 == 1:
            rijec = rijec[::-1]
        recenica += rijec + " "
    return recenica.strip()

recenica_in = "the quick brown fox jumps over the lazy dog"
print(funkcija(recenica_in))
