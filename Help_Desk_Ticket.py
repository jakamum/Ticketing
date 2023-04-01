#initialise variable list
tickets = []
help = []
tech = []
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


#main process
from Ticket import *
from Utils import *
if __name__=="__main__":

    #main code
    choice = None
    welcome()
    loadTickets()
    login()
    if help or tech:
        while not choice == "0":
            menu()
            choice = input("Choice: ")
            processChoice(choice)
            print() # prints an empty line for fun
        saveTickets()
        print("Your details have been saved")
    exit = input("\nPress enter to exit") # exits the program


