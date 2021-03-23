userinput = input("Choose a Random Number")
print("User Entered:", userinput)

randomNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, int(userinput)]

if type(userinput) == int:
    print("Please enter a valid integer")
else:
    print(sum(randomNumbers))