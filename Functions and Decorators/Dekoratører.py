def min_dekorator(func):
    # Wrapper funktion, der tilføjer ekstra funktionalitet
    def wrapper():
        print("Noget sker før funktionen kaldes.")  # Før den originale funktion
        func()  # Kalder den originale funktion
        print("Noget sker efter funktionen er kaldt.")  # Efter den originale funktion
    return wrapper

# Anvender dekoratøren på denne funktion
@min_dekorator
def siger_hej():
    print("Hej!") 

# Kald af den dekorerede funktion
siger_hej()

def log_dekorator(func):
    def wrapper(*args, **kwargs):
        print(f"Kald til funktionen {func.__name__} med argumenter {args} og {kwargs}")
        result = func(*args, **kwargs)
        print(f"Resultat: {result}")
        return result
    return wrapper

@log_dekorator
def adder(a, b):
    return a + b

# Brug af dekoreret funktion
adder(5, 3)  # Logger kald og resultat

import time

def timing_dekorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Funktionen {func.__name__} tog {end - start} sekunder at udføre.")
        return result
    return wrapper

@timing_dekorator
def langsom_funktion():
    time.sleep(2)  # Simulerer en langsom funktion

# Brug af dekoreret funktion
langsom_funktion()
