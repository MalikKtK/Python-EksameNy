class Person:
    def __init__(self, name, age, street):
        #Initializer/contructor: Initialisere en ny instans af klassen Person
        #Med private attributer
        self.__name = name     
        self.__age = age       
        self.__street = street

    @property
    def name(self):
        # Getteren for name: Returner private attributen __name
        return self.__name

    @name.setter
    def name(self, new_name):
        # Setteren for name: Setter private attributen __name
        self.__name = new_name

    @property
    def age(self):
        # Getteren for age: Returner private attributen __age
        return self.__age

    @age.setter
    def age(self, new_age):
        # Setteren for age: Settter private attributen __age 
        if new_age > 0:
            self.__age = new_age
        else:
            raise ValueError("Age skal være større end 0")

    @property
    def street(self):
        # Getteren for street: Returner private attributen __street
        return self.__street

    @street.setter
    def street(self, new_street):
        # Setteren for street: Setter private attributen __street
        self.__street = new_street

#Laver en instans af klassen Person
person1 = Person("Malik", 24, "Fyrrelunden 83")


print(person1.name)   #Får adgang til name via getteren og printer det
print(person1.age)    
print(person1.street) 

person1.name = "Malik"     #Updater attributterne via setteren
person1.age = 26              
person1.street = "Ishøj" 

print(person1.name)   #Får adgang til de opdaterede attributer via getteren og printer det
print(person1.age)    
print(person1.street) 
