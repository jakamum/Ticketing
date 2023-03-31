# Help Desk Ticketing system

Help Desk Ticketing System is an application to enable help desk staff and IT technician to submit tickets and/or update ticket information It was created using Python version 3.9.

## Functionality

The system allows for users to input ticket information, display tickets, display statistics, allocate password, enter a response, reopen a ticket, print tickets and store tickets by way of the external text file.

## Modules and External Text File

In addition to the main file [Help_Desk_Ticket](Help_Desk_Ticket.py), this program package includes two modules [Ticket](Ticket.py)and [Utils](Utils.py) which contain multiple classes and functions. The external text file [tickets](tickets.txt) is accessed from within the program. Details are updated and then saved to the text file on exit from the program.

## Classes

The following classes are included:

Ticket
User
HelpDesk
ITtech

## Methods

Some methods are contained within the classes found in the Ticket file and others are found in the Utils file. See below:

### Ticket Class

displayTickets - all tickets are displayed.

displayStats - displays the total number of tickets created, the number of tickets to resolve, and the number of closed tickets.

### User Class

submitTicket - Enter a new ticket instance to be stored in a list. This will include the generation of a new password using index to select and compbine specific fragments of staff_id and staff_name if a Password Change string is detected.

checkEmail - includes validation rules for email syntax.

selectTicket - searches the list for a selected ticket using the Ticket ID. This method is utilised  within other methods. 

reopenTicket - calls selectTicket method and confirms a reopen request for the selected ticket. This will change the status to “Reopened” and consequently subtract from the statistic “Resolved” and add to the “To Solve” result. It will also call displayTickets and displayStats methods.

enterResponse - calls selectTicket method for a selected ticket. If the ticket is not already closed, a response will be entered. The response will be stored in the list and the status will be amended to “Closed”. Consequently 1 will be subtracted from the statistic “To Solve” and added to the “Resolved” result. It will also call displayTickets and displayStats methods.

### Utils File

welcome - includes ascii word art on the opening of the program

loadTickets - Stored data will be retrieved from the external text document and placed in the tickets list.

login - user login to control initial access to the application and to customise permissions for each  user.

menu - display menu choices.

processChoice - navigates based on menu choice.

saveTickets - saves the information from the tickets list and rewrites the text file to update it with new ticket submissions and amendments.


## Bon appetit!
