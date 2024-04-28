class Person:
    # class attribute
    species = "Mammal"

    # Instance attribute
    def __init__(self, name, hairs):
        self.name = name
        self.hairs = hairs
        
    def speak(self):
        print("My name is {}".format(self.name))
    
    def hair(self):
        print("My hair is {}".format(self.hairs))


a = Person("Yash","Long")
a.speak()
a.hair()   

b = Person("XYZ","bald")
b.speak()
b.hair()  