class ParentClass:  # parent class& the original attributes
    def __init__(self, fname, lname, JobName, city):
        self.firstname = fname
        self.lastname = lname
        self.JobName = JobName
        self.city = city

    # parent function that relates to the parent attributes
    def parentFunction(self):
        print(self.firstname, self.lastname, self.JobName, self.city)


class ChildClass(ParentClass):
    def __init__(self, fname, lname, year, JobName, city, school): #notice we intialise original attributes AND the newly created ones
        super().__init__(fname, lname, JobName, city)  # the original parent class
        # new child class attribute we want to include
        self.graduationyear = year
        self.school = school

    def childFunction(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear,
              " and your future Job is ",
              self.JobName, " in the city of: ", self.city, "and the school :", self.school)

x = ChildClass("Mike", "Olsen", 2019, "Engineer", "London", "London School") # corresponding to the child class
x.childFunction()
