#Creating a class MyPet
class MyPet:
    #Initialising the class
    #Self means the member is referring to the current class
    def __init__(self, n="Kutta"):
        self.name = n
        self.breed = "Labra"

    #Making a function of the class (aka method of the class)
    #Overwriting the original name
    def changeName(self, x):
        self.name = x 

    def __str__(self):
        return "The dog's name is: " + self.name

#Child class
class PetToys(MyPet):
    def __init__(self):
        MyPet.__init__(self, n="Kutta")
        self.favToy = "Chew Toy"


print("Original names:")
#Creating an object of class MyPet
myPetDog = MyPet("Tommy")
#Printing out the name of the dog from myPetDog
print(myPetDog.name)

#Creating another object of MyPet
myPetDog2 = MyPet("Rocky")
print(myPetDog2.name)

#Changing the name of myPetDog2 object
print("After changing names:")
myPetDog2.changeName("Browny")
print(myPetDog.name)
print(myPetDog2.name)

#Creating an object of the child class
myPetToys = PetToys()
print(myPetToys.name) #Prints out the default value of name
print(myPetToys.favToy) #Prints out the favToy 
myPetToys.changeName("Sprite")
print(myPetToys.name) #Prints out the new name

#Printing out the objects
print(myPetDog)
print(myPetDog2)
