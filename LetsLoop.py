# undersrtanding loops
# for loop is a way to make the code efficient and elegant
#

# for item in "hello":
#    print(item)

# Python will go over or iliterate over every item in the string word

# for item in range(5):  # for every item in 5. Start with 0 and end at 4
#    print(item)
#   print("this will print over 5 time")

# Python will go over or iliterate 5 times,

# Lets do a for loop for a list
# each loop will mention the name
# And it will greet the menitoned user via a f string

# names = ["ALEX", "MEG", "LARRY", "PETER"]
# for names in names:
#   print(f'Hello {names} how are you? ')


# Let try to implement conditional statements in a FOR Loop
# We can combine for and if statentbs

cars = ["Merc", "Audi", "Lambo", "BMW", "Citron"]
for car in cars:
    print(f'This is your vehicle : {car}')
    if car == "Merc":
        print(f'Great choice on the {car}')
        # another clause could be here
    else:
        print("its not the merc")
