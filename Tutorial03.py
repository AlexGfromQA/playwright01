class AttributesPractice:
    # Car Object - Car Properties
    def __init__(self, model, colour, year, reg):
        self.model = model
        self.colour = colour
        self.year = year
        self.reg = reg

    # Print Car
    def car(self):
        print("The car {}, {}, {}, {}".format(self.model, self.colour, self.year, self.reg))


UserCar = AttributesPractice("Mazda", "red", "2022", "71 Plate")  # Creation of an object instance
print(UserCar.model, UserCar.colour, UserCar.year, UserCar.reg)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Passport:
    def __init__(self, fname, lname, PassportID):
        self.fName = fname
        self.lNameName = lname
        self.PassportID = PassportID

    # a function for the Passport
    def passport(self):
        print("This is the passport: {}, {}, {}".format(self.fName, self.lNameName, self.PassportID))


PassportObj = Passport("value 1", "value 2", "value 3")
print(PassportObj.fName, PassportObj.lNameName, PassportObj.PassportID)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Book:

    def __init__(self, bookName, author, year):
        self.bookName = bookName
        self.author = author
        self.year = year

    def showBook(self):
        print("These are your books {}, {}, {}".format(self.bookName, self.author, self.year))

        bookobj = Book("Car Manual", "Tyson Furry", "2022")
        print(bookobj.bookName, bookobj.author, bookobj.year)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class FishNChipsBar:
    def __init__(self, main_option, drink, sauce, size):
        self.main_option = main_option
        self.drink = drink
        self.sauce = sauce
        self.size = size

    def showBar(self):
        print("Your order {}, {}, {}, {}".format(self.main_option, self.drink, self.sauce, self.size))

        ShowBarObj = FishNChipsBar("curry chips", "coke", "curry", "large")
        print(ShowBarObj.main_option, ShowBarObj.drink, ShowBarObj.sauce, ShowBarObj.size)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class House:
    def __init__(self, house_type, address, bedroom):
        self.house_type = house_type
        self.address = address
        self.bedroom = bedroom


houseOb = House("value", "value2", "value3")


def printHouse(self):
    print("This is what you see in a house {}, {}. {}".format(self.house_type))

# create an instanc e variable, which will allow us to pass in positional argument values.
