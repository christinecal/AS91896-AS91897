#Christine Naomi Calantog

'''This program is to keep track of Julie's party hire'''

#import tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
'''----------------------------------------- Set up GUI -----------------------------------------
Create the title, default buttons, labels, and entry boxes. Put them in the correct grid location.'''

#create the buttons and title
    #buttons: update(append),print,delete(row),quit

def setup_buttons():
    Button(main_window, text="Update",font="Helvetica 15",command=check_inputs) .grid(column=0,row=1,sticky=E,ipadx=20,ipady=5,pady=5)
    Button(main_window, text="Print",font="Helvetica 15",command=print_hire_details) .grid(column=1,row=1,ipadx=20,ipady=5,pady=5)
    Button(main_window, text="Quit",font="Helvetica 15",command=quit,width=5) .grid(column=2,row=1,sticky=W,ipadx=20,ipady=5,pady=5)
    Button(main_window, text="Delete",font="Helvetica 15",command=delete_row) .grid(column=2,row=6,sticky=W,ipadx=20,ipady=3)
    #title
    Label(main_window, text = "Party Hire Tracker", font="Arial 25").grid(column=1,row=0,pady=(30,10))

#creating the labels (entries)
           #these are the global variables that are used, accessible throughout the program
    global hire_details, entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries, delete_item
    #customer name
    Label(main_window, text="Customer Full Name",font='Arial 18') .grid(column=0,row=2,padx=20)
    entry_name = Entry(main_window,font='Helvetica 16')
    entry_name.grid(column=1,row=2,padx=10,pady=5)
    #receipt number
    Label(main_window, text="Receipt Number",font='Arial 18') .grid(column=0,row=3)
    entry_receiptnumber = Entry(main_window,font='Helvetica 16')
    entry_receiptnumber.grid(column=1,row=3,padx=10,pady=5)
    #item hired (combobox)
    item_hired = StringVar()
    Label(main_window, text="Item Hired",font='Arial 18') .grid(column=0,row=4)
    entry_item = ttk.Combobox(main_window,font='Helvetica 16', textvariable=item_hired, values=('Cutlery Set', 'Glassware','Chairs', 'Tables', 'Balloons', 'Booth hire',
                                                                            'Prop hire','Jukebox','Party lights', 'Dance floor'), state='readonly')
    entry_item.grid(column=1,row=4,padx=10,pady=5)                                                 
    #number hired
    Label(main_window, text="Number Hired",font='Arial 18') .grid(column=0,row=5)
    entry_numberhired = Entry(main_window,font='Helvetica 16')
    entry_numberhired.grid(column=1,row=5,padx=10,pady=5)
    #row number (for when item is returned)
    Label(main_window, text="Row #",font='Arial 18') .grid(column=0,row=6)
    delete_item = Entry(main_window,font='Helvetica 16')
    delete_item .grid(column=1,row=6,padx=10,pady=5)

'''----------------- Attach a function to the buttons -----------------'''

#PRINT button
    #print the customers' details into a table after appending

def print_hire_details():
    global hire_details, total_entries, item_count,root_count,frame
    item_count = 0
    while root_count <= 1:
        root_count += 1
        #column headings
        Label(frame, font='Helvetica 15 bold',text="Row").grid(column=0,row=0,ipadx=20,pady=15)
        Label(frame, font='Helvetica 15 bold',text="Customer Name").grid(column=1,row=0,ipadx=20)
        Label(frame, font='Helvetica 15 bold',text="Receipt Number").grid(column=2,row=0,ipadx=20)
        Label(frame, font='Helvetica 15 bold',text="Item(s) Hired").grid(column=3,row=0,ipadx=10)
        Label(frame, font='Helvetica 15 bold',text="Number Hired").grid(column=4,row=0,ipadx=20)
        Label(main_window, text = " ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font="Arial 10").grid(column=0,row=7,pady=(20,0),columnspan=10)
        Label(main_window, text = " ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font="Arial 10").grid(column=0,row=8,columnspan=10,ipady=0.005)
        '''Label(main_window, text="Customer Details",font="Arial 20").grid(column=1,sticky=E,row=9,columnspan=2)'''
        frame.grid(column=0,row=10,columnspan=50)
    #multi-dimensional list - each item on the list as a separate row 
    while item_count < total_entries :
        Label(frame,font="Arial 15", text=item_count).grid(column=0,row=item_count+8) 
        Label(frame,font="Arial 15", text=(hire_details[item_count][0])).grid(column=1,columnspan=1,row=item_count+8)
        Label(frame,font="Arial 15", text=(hire_details[item_count][1])).grid(column=2,columnspan=1,row=item_count+8)
        Label(frame,font="Arial 15", text=(hire_details[item_count][2])).grid(column=3,columnspan=1,row=item_count+8)
        Label(frame,font="Arial 15", text=(hire_details[item_count][3])).grid(column=4,columnspan=1,row=item_count+8)
        item_count +=  1

#UPDATE (append) button
    #clear previous inputs to add the next customer to the list
        
def append_details():
    global hire_details, entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries
    #append each item to its own area of the list
    hire_details.append([entry_name.get(),
                         entry_receiptnumber.get(),
                         entry_item.get(),
                         entry_numberhired.get(),
                         delete_item.get()])
    #clear the entry boxes
    entry_name.delete(0,'end')
    entry_receiptnumber.delete(0,'end')
    #clear the combobox 
    entry_item.set('')
    entry_numberhired.delete(0,'end')
    delete_item.delete(0, 'end')
    total_entries +=1
    
#DELETE button
    #delete a row when an item is returned
def delete_row ():
    global hire_details, delete_item, total_entries, item_count, frame
    try:
    #which row to delete
        del hire_details[int(delete_item.get())]
        total_entries = total_entries - 1
        delete_item.delete(0,'end')
        Label(frame, text="                       ").grid(column=0,row=item_count+7)
        Label(frame, text="                       ").grid(column=1,row=item_count+7)
        Label(frame, text="                       ").grid(column=2,row=item_count+7)
        Label(frame, text="                       ").grid(column=3,row=item_count+7)
        Label(frame, text="                       ").grid(column=4,row=item_count+7)
    #print item to own area of list
        print_hire_details()
    #checking if input for row number is valid and is an integer
    except IndexError:
        messagebox.showerror('error', "Row does not exist.")
    except ValueError:
        messagebox.showerror('error', "Row number must be an integer.")

#QUIT button
    #subroutine to exit the program

def quit():
        main_window.destroy()

'''------------------------- Check for validity -------------------------
Set up red error text messages and error message box
Requirements:
1. Input cannot be blank
2. Specific to data type 
'''

def check_inputs():
    global hire_details, total_entries,entry_name,entry_receiptnumber,entry_item,entry_numberhired
    entry_check=0
    Label(main_window, text="                                                       ") .grid(column=2, row=2)
    Label(main_window, text="                                                       ") .grid(column=2, row=3)
    Label(main_window, text="                                                       ") .grid(column=2, row=4)
    Label(main_window, text="                                                       ") .grid(column=2, row=5)

#customer name 
    #cannot be blank
    hasAlpha = False
    hasSpace = False
    for x in entry_name.get():
        if x.isalpha():
            hasAlpha = True
        elif x.isspace():
            hasSpace = True
    #correct data type (string) and at least 4 characters (full name)
    if (entry_name.get().isalpha() or (hasSpace and hasAlpha)) and len (entry_name.get()) > 4:  
        Label(main_window, text="                   ").grid(column=2,row=2, sticky=W)
        Label(main_window, text="                   ").grid(column=2,row=2, sticky=W)
        entry_check = 0
    else:
        Label(main_window, fg='red', text="Required (Letters)",font='Arial 14').grid(column=2,row=2, sticky=W)
        entry_check = 1

#receipt number
    #cannot be blank
    hasAlpha2 = False
    hasSpace2 = False
    for y in entry_receiptnumber.get():
        if y.isalpha():
            hasAlpha2 = True
        elif y.isspace():
            hasSpace2 = True
    #correct data type (integer), must be 6 digits
    if entry_receiptnumber.get().isdigit() and len(entry_receiptnumber.get()) == 6:
        Label(main_window, text="                  ").grid(column=2,row=3,sticky=W)
        Label(main_window, text="                  ").grid(column=2,row=3,sticky=W)
        entry_check = 0
    else:
        Label(main_window, fg='red', text="Required (6 Digits)",font='Arial 14').grid(column=2,row=3,sticky=W)
        entry_check = 1

#item hired
    #cannot be blank (fill the combobox)
    if len(entry_item.get()) == 0:
        Label(main_window,fg='red',text="Required (Select item)",font='Arial 14').grid(column=2,row=4,sticky=W)
        entry_check=1

#number hired
    #cannot be blank, correct data type (integer), 1-500 boundary values
    if (entry_numberhired.get().isdigit()):
        if 0 < int(entry_numberhired.get()) <= 500:
            Label(main_window, text="                  ").grid(column=2,row=5,sticky=W)
            Label(main_window, text="                  ").grid(column=2,row=5,sticky=W)
            entry_check = 0
        else:
            Label(main_window, fg='red', text="Required (Numbers 1-500",font='Arial 14').grid(column=2,row=5,sticky=W)
            Label(main_window, fg='red', text="Required (Numbers 1-500)",font='Arial 14').grid(column=2,row=5,sticky=W)
            entry_check = 1  
    else:
        Label(main_window, fg='red', text="Required (Numbers 1-500)",font='Arial 14').grid(column=2,row=5,sticky=W)
        Label(main_window, fg='red', text="Required (Numbers 1-500)",font='Arial 14').grid(column=2,row=5,sticky=W)
        entry_check = 1

#if all inputs are valid, append to allow for printing
    if entry_check == 0:
        append_details()

'''--------------------- Start the program running ---------------------'''

def main():
    global main_window,frame,root_count, hire_details, total_entries,entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries
    #empty list for the details
    hire_details = []
    total_entries = 0
    #GUI and setup
    main_window = Tk()
    main_window.title("Registry and Database")
    #geometry of main_window frame
    main_window.geometry("660x530")
    root_count = 1
    setup_buttons()
    frame = Frame(main_window)
    main_window.mainloop()
#function called to start up the GUI
main()




