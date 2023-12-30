class Person:
    def __init__(self, navn, alder):
        self._navn = navn  # En privat attribut
        self._alder = alder  # En anden privat attribut

    # Getter for navn
    @property
    def navn(self):
        return self._navn

    # Setter for navn
    @navn.setter
    def navn(self, nyt_navn):
        if isinstance(nyt_navn, str):
            self._navn = nyt_navn
        else:
            raise ValueError("Navn skal være en streng")

    # Getter for alder
    @property
    def alder(self):
        return self._alder

    # Setter for alder
    @alder.setter
    def alder(self, ny_alder):
        if ny_alder > 0:
            self._alder = ny_alder
        else:
            raise ValueError("Alder skal være positiv")

    def vis_info(self):
        return f"Navn: {self.navn}, Alder: {self.alder}"

# Eksempel på brug af klassen
person = Person("Lars", 30)
print(person.vis_info())  # Udsriver: Navn: Lars, Alder: 30

# Opdatering af navn og alder ved brug af settere
person.navn = "Mette"
person.alder = 35
print(person.vis_info())  # Udsriver: Navn: Mette, Alder: 35

# Forsøg på at sætte en ugyldig alder
try:
    person.alder = -5
except ValueError as e:
    print(e)  # Udsriver: Alder skal være positiv
