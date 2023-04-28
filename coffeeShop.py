#Let's build a coffee shop robot.

print("Welcome to Junior's Cafe!\n")

#Assigning a variable with an equal sign.

name = input("What is your name?")

#If statement for error handling is a great step here.

if name == "" :
    print("Sorry I didn't catch your name, Can you tell me again?")
    exit()

#Using concatenation to combine strings and variables together. 

print("\nHello " + name + ", thank you for coming to Junior Cafe!\n")

menu = "Cold Brew, Vanillia Latte, Mocha, Cappucino, Black Coffee"

print("\nSo " + name + ", what would like today? Here is our menu!\n" + menu)

#Try to write an if statement here if the user inputs a item that isn't on the menu print "Sorry we don't have that on our menu."

order = input()

price = 5

quantity = input("\nHow many would you like? ")

total = price * int(quantity)

print("\nSounds good " + name + "! " + "I will have your " + quantity + " " + order + "s" + " ready in a few moments.")

print("\nYour total is: $" + str(total))