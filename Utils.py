import time

#initialise variable list
tickets = []
help = []
tech = []
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

from Ticket import *

#fun welcome function
def welcome():
    print("""
                                                    ***Welcome to the***
                    
                                ___ ___          .__               ________                    __     
                                /   |   \   ____  |  |  ______      \______ \    ____    ______|  | __ 
                                /    ~    \_/ __ \ |  |  \____ \      |    |  \ _/ __ \  /  ___/|  |/ / 
                                \    Y    /\  ___/ |  |__|  |_> >     |    `   \\  ___/  \___ \ |    <  
                                \___|_  /  \___  >|____/|   __/     /_______  / \___  >/____  >|__|_ \ 
                                    \/       \/       |__|                \/      \/      \/      \/ 
                                                                        
                                                                        
\n                                                   ***Ticketing System***
"""
)
    time.sleep(.5)


#login as helpdesk or ittech
def login():
    
    role = input("Please enter your role:(" + GREEN + "HD " + RESET + "or " +  RED + "IT) " + RESET)
    password = input("Please enter your password:(" + GREEN + "HD123 " + RESET + "or " +  RED + "IT123) " + RESET)    
    global aUser

   
    if role == "HD" and password == "HD123":            
        aUser = HelpDesk(role, password, "HelpDesk")        
        help.append(aUser)
        return aUser
            
    elif role == "IT" and password == "IT123": 
        aUser = ITtech(role, password, "ITTech")
        tech.append(aUser)
        return aUser
            
    else:
       print("Sorry, you don't have access.")
           

#load tickets from external text file
def loadTickets():
    exists = True
    try:
        text_file = open("tickets.txt", "r")
    except FileNotFoundError:
        exists = False
    if exists == True:
        ticketText = text_file.readline()
        while ticketText:
            ticketText = ticketText.strip()
            ticket = ticketText.split(",")
            aTicket = Ticket(int(ticket[0]), ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6]) 
            tickets.append(aTicket)
            ticketText = text_file.readline()
        text_file.close()


#display menu function
def menu():
    time.sleep(.5)
    print(
    """
    Please select from the following:
    0 - Exit
    1 - Submit a Ticket
    2 - Display Tickets
    3 - Provide a Response
    4 - Reopen a Ticket
    5 - Display Statistics
    6 - Print Tickets
    """
    )


#process the menu choices and direct to the appropriate function or exit
def processChoice(userChoice):
    #exit
    if userChoice == "0":
        print("\nThank you for your time")

    # submit a ticket
    elif userChoice == "1":
        if tech:
            print("Sorry you don't have access to this feature. Please make another selection")
        else:
            print("\n*****Submit a Ticket***** ")
            User.submitTicket()
    
    # display all tickets
    elif userChoice == "2":
        Ticket.displayTickets()

    # provide response        
    elif userChoice == "3":
        if help:
            print("Sorry you don't have access to this feature. Please make another selection")
        else:
            print("\n*****Enter a response*****")
            User.enterResponse()
    
    # reopen ticket case        
    elif userChoice == "4":
        if help:
            print("Sorry you don't have access to this feature. Please make another selection")
        else:
            print("\n*****Reopen a Ticket*****")
            User.reopenTicket()
        
    # display statistics
    elif userChoice == "5":
        Ticket.displayStats()

    #print tickets
    elif userChoice == "6":
        Ticket.displayTickets()

#save the tickets to an external text file
def saveTickets():
    text_file = open("tickets.txt", "w")
    for ticket in tickets:
        text_file.write(str(ticket.id) + "," + ticket.staff_name + "," + str(ticket.staff_id) + "," + str(ticket.email) + "," + ticket.description + "," + ticket.response + "," + ticket.status + "\n")
    text_file.close()

