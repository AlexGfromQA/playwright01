# a = [1, 3, 45, 1, 3, 1, 5, 6566, 546, 56, "string"]
# to return a specified list number
# print(a.index(45))
# print(a.reverse())
# print(a.pop(3))
# print(a)


#INPUT FROM A USER AND ENTER INTO A LIST

# Create empty list
def runDrink():
    Sodas = []  # Create empty list

    while True:  # While loop chosen since we don't know how many answers the user will enter
        SodaInput = input("State you're favorite drink\n")
        Sodas.append(SodaInput)

        MoreSodaOption = input("Do you want to enter more? ( y / n ) :")
        if MoreSodaOption.casefold() == "n":                                #casefold used to dimiss case sensitivity
            break  # need to break the infinite loop

        for element in Sodas:
            print("Your fav drinks :" + element)


runDrink()
