# Eksempel på brug af len()
frugter = ["æble", "banan", "kirsebær"]
print("Antal frugter:", len(frugter))  # Udsriver antallet af elementer i listen

# Eksempel på brug af max()
tal = [4, 1, 17, 5, 6]
print("Højeste tal i listen:", max(tal))  # Finder det største tal i listen

# Eksempel på brug af map()
def kvadrer(tal):
    return tal * tal

tal = [1, 2, 3, 4, 5]
kvadrerede_tal = map(kvadrer, tal)  # Anvender funktionen kvadrer på hvert element i listen
print("Kvadrerede tal:", list(kvadrerede_tal))

# Sammenligning med list comprehension (et eksempel på funktionelt paradigme)
kvadrerede_tal_comprehension = [x * x for x in tal]
print("Kvadrerede tal (comprehension):", kvadrerede_tal_comprehension)
