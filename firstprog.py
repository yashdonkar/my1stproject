name = "yash_donkar"
age = 22
print(name)
print(age)
num=3
num+=4
print(num)

def art(n):
    print(n + " did art!!!")

art(n = "Jeetada")


# object oriented nahi ahe

class Person:
    # class attribute
    species = "Mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is {}".format(self.name))


        