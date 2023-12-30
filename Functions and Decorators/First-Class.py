def ekstern(x):
    def intern(y):
        return x + y
    return intern

min_funktion = ekstern(10)
print(min_funktion(5))  # Output: 15

def multiplikator(multiplikator):
    def indre_funktion(x):
        return x * multiplikator
    return indre_funktion

fordobler = multiplikator(2)
tredobler = multiplikator(3)

print(fordobler(5))  # Output: 10
print(tredobler(5))  # Output: 15
