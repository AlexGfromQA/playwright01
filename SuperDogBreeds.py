# Create Parent & Child Classes
# Initialise both classes
# add new functions within the classes e.g. walking
# Use the Super() in the child class and intialise the previous attributes from the parent into the child

class ParentDog:  # super class
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        print("Likes Walks?")
        return True


# CHILD CLASSES
class childDogOne(ParentDog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)  # instead copying the same intilsiation as the parent class


class childDogTwo(ParentDog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


class multipleInheritance(childDogOne, childDogTwo):
    def __init__(self, name, age, friendliness, noleesh):
        super().__init__(name, age, friendliness)
        super().__init__(name, age, friendliness)

        self.noleesh = noleesh


# object instance

showPet = childDogOne("Steve", 23, "happy")
print(showPet.name, showPet.age, showPet.friendliness)

showPet2 = childDogTwo("Larry", 21, "Mardy")
print(showPet2.name, showPet2.age, showPet2.friendliness)
print(showPet.likes_walks())  # referencing the method in the parent class
# print(showPet2.likes_walks()

# multiple instance

ShowMulti = multipleInheritance("Third", 1, "moody", "yes")
print(ShowMulti.name, ShowMulti.age, ShowMulti.friendliness, ShowMulti.noleesh)
