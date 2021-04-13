"""
Zadatak 6.
Napisati skriptu koja pronalazi najmanji cijeli broj koji je:
1. djeljiv s 13
2. sadrži u sebi broj 189 (primjerice 21893)
3. palindromski broj (isti kad se čita s druge strane)
Dodatno: ekstra bod za rješenje s jednostavnom optimizacijom izvođenja
(nije potrebno iterirati kroz sve cijele brojeve)
"""

i = 0

while 1:
    if "189" in str(i) and str(i) == str(i)[::-1]:
        break
    i += 13

print(i)
