#--------------------------------------------------------
#Writing files
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location
#----------------------Lists/Imports---------------------
from modules import greeting
from modules import trex
import time
#----------------------Functions-------------------------
greeting.greetings()

def increase():
    increasing = input("Do you want to increase any of the stock? Type yes or no. ")
    if increasing == "yes":
        selection = input("What item do you want to increase the stock of? ")
        amount = float(input("How much do you want to increase it by? "))
        trex.increase_stock(amount, selection)
    else:
        print("Okie Dokie, on to the next selection...")
        
def decrease():
    decreasing = input("Do you want to decrease any of the stock? Type yes or no. ")
    if decreasing == "Yes":
        decselection = input("What item do you want to decrease the stock of? ")
        decamount = float(input("How much do you want to decrease it by? "))
        trex.decrease_stock(decamount, decselection)
    else:
        print("Okie Dokie, We are all done the selection...")
        time.sleep(5)
        print("Closing program. Have a good day!")
        print("Program closing...")
        time.sleep(5)
        
increase()
decrease()
        
    
        
    
