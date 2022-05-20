# inheritance - receiving

# Parent
class Person:
    def __init__(self, fname, lname, idname):
        self.fname = fname
        self.lname = lname
        self.idname = idname

    def printname(self):
        print(self.fname, self.lname, self.idname)


# Child(ren)
class Student(Person):
    pass

# Add the _init_ function
class Transfer(Person):
    pass


x = Student("Mike", "Olsen", "123")
x.printname()



