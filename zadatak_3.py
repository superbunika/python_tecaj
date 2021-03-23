datoteka = input("Unesite naziv datoteke: ")
ekstenzija = datoteka[datoteka.rfind("."):]

if ekstenzija == ".py":
    print("Vaša datoteka ima ekstenziju %s i to je Python source kod." % ekstenzija)
elif ekstenzija == ".txt":
    print("Vaša datoteka ima ekstenziju %s i to je tekstualna datoteka." % ekstenzija)
elif ekstenzija == ".php":
    print("Vaša datoteka ima ekstenziju %s i to je PHP source kod." % ekstenzija)
else:
    print("Ne prepoznajem ekstenziju.")

#print(ekstenzija)