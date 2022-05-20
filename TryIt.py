# Create a parent
# create a child
# Set attributes for the parent + initalise
# Set attributes for the child + initialise
# Within the child, refer to the Parent ()
# Within the child inherit the parent via _innit_, adding parent attributes to the child attributes self list
# Within the child, inhert via super().__innit__(self, parent attributes

# Add the the super().
class TheDealership:

    def __init__(self, Dealership, Petrol, Hybrid, Diesel):
        self.Dealership = Dealership
        self.Petrol = Petrol
        self.Hybrid = Hybrid
        self.Diesel = Diesel

    # characteristics
    def Online_availability(self):
        print("Online Service Available")

    def Non_Online_availability(self):
        return True
        # print("Online Service Available")


class LondonShowroom(TheDealership):
    def __init__(self, name, location, Dealership, Petrol, Hybrid, Diesel):
        super().__init__(Dealership, Petrol, Hybrid, Diesel)
        self.name = name
        self.location = location

    def LondonShopFloor(self):
        print(self.name, " ", self.location, " ", self.Dealership, " ", self.Petrol, " ", self.Hybrid, " ", self.Diesel)


print("Welceome to the LONDON dealership")
a = input("Please enter your name? \n")
b = input("Whats your surname? \n")
print("Thank up {} , {}".format(a, b))
objtoprint = LondonShowroom("name value", "LONDON", "LDN Dealership", "Petrol", "Hybrid", "Diesel")
objtoprint.LondonShopFloor()

objtoprint.Online_availability()
objtoprint.Non_Online_availability()

# Obj = LondonShowroom("Alexander Dealership", "London", "Petrol", "Not Hybrid", "Not Diesel", "no value")
# print(LondonShowroom)
