# Inheritenc

# create a class
# Set methods of the class
# create classes for specific types of animals - lion, cheeter, bunny
# Implmenting inhertence: 1st we start of by adding the parentClass() into the ChildClass Parameters
# Then create objects in these classes
# Add unique attributes to the children


class Animal:
    alive = True

    # eat
    def eat(self):
        print("Animal is eating")

    # sleep
    def sleep(self):
        print("This animal is sleeping")

    # move
    def moving(self):
        speed = "mph"
        print(speed)


class Lion(Animal):
    def LionAttack(self):
        print("Lion ATTACK")


class Cheetah(Animal):
    def cheetahAttack(self):
        print("Cheetah ATTACK")


class Bunny(Animal):
    def BunnyAttack(self):
        print("Bunny ATTACK")


# Creation of objects

LionObj = Lion()

CheetahObj = Cheetah()

BunnyObj = Bunny()

# Now lets check the attributes for these objects
print(LionObj.alive)
print(CheetahObj.eat())
print(BunnyObj.sleep())

print("Now lets see if we can use both the inherited attributes and the newly created attribute of the child cases")
print(BunnyObj.BunnyAttack())
print(LionObj.LionAttack())
print(CheetahObj.cheetahAttack())