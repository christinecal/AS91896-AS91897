#Date: Wednesday 8 June
#Name: Christine Calantog

'''This program is to keep track of Julie's party hire '''

from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()
    
#print details of customers' inputs 
def print_hire_details():
    pass
    
#create the buttons and labels
def setup_buttons():
    pass

#delete a row from the list
def delete_row():
    pass

#add the next customer to the list
def append_details():
    pass

#validity checker
#cannot be blank and specific to data input
def check_inputs():
    pass

#start the program running
def main():
    global main_window 
    global hire_details, entry_name, receipt_number, item_hired, number_hired, total_entries
    hire_details = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()
main()
