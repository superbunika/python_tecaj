datoteka = input("Unesite naziv datoteke: ")
ekstenzija = datoteka[datoteka.rfind("."):]

ekstenzije = {
    ".py": "Python source kod",
    ".txt": "tekstualna datoteka",
    ".php": "PHP source kod"
}

"""
if ekstenzija == ".py":
    print("Vaša datoteka ima ekstenziju %s i to je Python source kod." % ekstenzija)
elif ekstenzija == ".txt":
    print("Vaša datoteka ima ekstenziju %s i to je tekstualna datoteka." % ekstenzija)
elif ekstenzija == ".php":
    print("Vaša datoteka ima ekstenziju %s i to je PHP source kod." % ekstenzija)
else:
    print("Ne prepoznajem ekstenziju.")
"""

if ekstenzija in ekstenzije:
    print("Vaša datoteka ima ekstenziju {} i to je {}.".format(ekstenzija, ekstenzije[ekstenzija]))
else:
    print("Ne prepoznajem ekstenziju.")