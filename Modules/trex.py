#--------------------------------------------------------
#Module:Return
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location
#Module for LibrariesAssignment in Modules Folder
#----------------------Lists------------------------------
stock = {"Bread": 40, "Bananas": 150, "Milk": 75}

#----------------------Functions-------------------------
def increase_stock(amount, selection):
    v = stock[selection]
    stock[selection] = v + amount
    print(stock)
    return stock
    
def decrease_stock(amount, selection):
    val = stock[selection]
    stock[selection] = val - amount
    print(stock)
    return stock