# create a tuple
# use a tuple
# use for when creating a set of data that we dont want to be modiified
# not immutable, no appending


# We need to type cast a list into a tuple

def runTuple():
    carMakeTuple = []

    while True:
        carMakeInput = input("What's your make? \n")
        carMakeTuple.append(carMakeInput)

        EndOfMake = input("Do you want to finish (y or no) ?")
        if EndOfMake.casefold() == "N":
            break

        for element in carMakeTuple:
            print(element)


runTuple()
