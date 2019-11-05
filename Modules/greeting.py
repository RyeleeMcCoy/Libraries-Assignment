#--------------------------------------------------------
#Module:greeting
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location
#----------------------Lists------------------------------
stock = {"Bread": 40, "Bananas": 150, "Milk": 75}

#----------------------Functions-------------------------
def greetings():
    name = input("Whats your name friend? ")
    print("Greetings", name)
    question = input("Hows your day been? ")
    if question == "good":
        print("Oh thats good!")
        print(":)")
    elif question == "bad":
        print("Oh thats not to good.")
        print(":(")
    else:
        print("Im sorry im a computer I dont know what that means.")
    print("Well I need to tell you the stock of todays products")
    print(stock)