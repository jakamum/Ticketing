import time
tickets = []
USERS = []

class Ticket():
    id: None
    staff_name: None
    staff_id:None
    email: None
    description: None
    response: None
    status: None
    counter = 2000

    #constructor    
    def __init__(self, id, staff_name, staff_id , email, description, response, status):
        self.id = Ticket.counter
        Ticket.counter += 1
        self.id = id
        self.staff_name = staff_name
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = response
        self.status = status
    

    #display tickets from tickets list retrieved from text file 
    def displayTickets(): 
        for ticket in tickets:
            
            print("\nTicket Number: ", str(ticket.id) + "\nTicket Creator: " + ticket.staff_name + "\nStaff ID: " + str(ticket.staff_id) + "\nEmall Address: " + ticket.email + "\nDescription: " + ticket.description + "\nResponse: " + ticket.response + "\nTicket Status: " + ticket.status + "\n")
            print("_________________________________________________________________________")

        to_menu = input("\nPlease press enter\n")

        
    #display statistics for status of tickets    
    def displayStats():
        count = len([ticket for ticket in tickets])
        to_solve = 0
        closed = 0
        global resolved 
        for ticket in tickets:
            if ticket.status == "Open" or ticket.status == "Reopened": 
                to_solve += 1           

            elif ticket.status == "Closed":
                closed += 1

        print("\n*****Statistics*****\n")    
        print("Tickets Created: ", count)
        print("Tickets To Solve: ", to_solve)
        print("Tickets Resolved: ", closed)

        to_menu = input("\nPlease press enter to return to the Menu")

class User:
    def __init__(self, role, password):
        self.role = role
        self.password = password

    #check email input
    def checkEmail(email, characters, min_length=8):
        while True:
            for character in characters:
                if character not in email:
                    email = input("\nYour email address must have '{}' in it\nPlease write your email address again: \n".format(character))
                    continue
            if len(email) <= min_length:
                email = input("\nYour email address is too short\nPlease write your email address again: \n")
                continue
            return email 


    #submit a new ticket function
    def submitTicket():
        id = Ticket.counter
        staff_name = input("Please enter staff name: ")
        staff_id = input("Please enter the staff ID: ")
        email = User.checkEmail(input("What is their email address? "), "@.")
        description = input("Please enter a brief description: ")
        response = "to be entered"
        print("Response: ", response)
        status = "Open"

        word = "Password Change"
        
        if word in description:
            staff_id1 = staff_id[0:2]
            staff_name1 = staff_name[0:3]

            response = "New password generated: " + staff_id1 + staff_name1 
            status = "Closed"
        
        if staff_id != "" and staff_name != "" and email != "" and description != "":
            aTicket = Ticket(id, staff_name, staff_id, email, description, response, status)
        
            tickets.append(aTicket)
            print("\n")
            print("*****Your ticket has been added*****\n")
            Ticket.displayStats()
        else:
            print("\n*****Please enter all fields*****")
            to_menu = input("\nPlease press enter to return to the Menu")
        

    #select a ticket from ticket list
    def selectTicket():
        global selected_ticket
        found = False
        select_id = input("\nPlease enter the Ticket ID: ")
               
        for ticket in tickets:
            if select_id != "" and select_id.isalpha() == False and select_id.isnumeric() == True:
                if int(select_id) == ticket.id:
                    found = True
                    print("_____________________")
                    print("\n***Ticket Details***\n", "\nTicket Number: " + str(ticket.id), "\nTicket Creator: " + ticket.staff_name, "\nTicket Status: " + ticket.status)
                    print("_____________________")
                    selected_ticket = ticket
                    return selected_ticket
        if found == False:
            found == False
            print("\nNo ticket has that ID number.")
          

    #reopen ticket status function
    def reopenTicket():
        
        selected_ticket = User.selectTicket()
        if selected_ticket:
            if selected_ticket.status == "Closed":
                answer = input("\nDo you want to reopen this ticket? ")
                if answer.lower() == "yes":
                    status = "Reopened"
                    selected_ticket.status = status
                    print("\nThe Ticket has been reopened")
                    time.sleep(1)
                    Ticket.displayTickets()
                    Ticket.displayStats()
                else:
                    print("\nThat input is invalid. Returning to the Main Menu...")
                    
            else:
                print("\nThis ticket is already open")
        else:
            return


    #enter a response and update status    
    def enterResponse():
        selected_ticket = User.selectTicket()
        if selected_ticket:
            if selected_ticket.status != "Closed":
                response = input("Please enter your response: ")
                
                if response != "":
                    selected_ticket.response = response
                    status = "Closed"
                    selected_ticket.status = status
                    print("This ticket has been closed.")
                    Ticket.displayTickets()
                    Ticket.displayStats()
                else:
                    print("Invalid Input")
                
            else:
                print("This ticket is already closed. Please reopen if you wish to add a response.")
                time.sleep(.5)
        else:
            return


class HelpDesk(User):
    user = None

    def __init__(self, role, password, user):
        super().__init__(role, password) 
        self.user = user

class ITtech(User):
    user = None

    def __init__(self, role, password, user):
        super().__init__(role, password)
        self.user = user
