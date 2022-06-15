#Date: Wednesday 8 June
#Name: Christine Calantog

'''This program is to keep track of Julie's party hire'''

from tkinter import *
from tkinter import ttk

'''----------------------------------------- Set up GUI -----------------------------------------
Create all the default buttons, labels, and entry boxes. Put them in the correct grid location.'''

#create the buttons
    #update(append),print,delete(row),quit

def setup_buttons():
    Button(main_window, text="Update",command=check_inputs) .grid(column=0,row=1)
    Button(main_window, text="Print",command=print_hire_details) .grid(column=1,row=1)
    Button(main_window, text="Quit",command=quit) .grid(column=2,row=1,sticky=W)
    Button(main_window, text="Delete",command=delete_row) .grid(column=3,row=6,sticky=E)

#creating the labels (entries)
           #these are the global variables that are used, accessible throughout the program
    global hire_details, entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries, delete_item
    #customer name
    Label(main_window, text="Customer Name") .grid(column=0,row=2)
    entry_name = Entry(main_window)
    entry_name.grid(column=1,row=2)
    #receipt number
    Label(main_window, text="Receipt Number") .grid(column=0,row=3)
    entry_receiptnumber = Entry(main_window)
    entry_receiptnumber.grid(column=1,row=3)
    #item hired (combobox)
    item_hired = StringVar()
    Label(main_window, text="Item Hired") .grid(column=0,row=4)
    entry_item = ttk.Combobox(main_window, textvariable=item_hired, values=('Cutlery Set', 'Glassware Set','Chairs', 'Tables', 'Pack of Balloons', 'Backdrop Hire',
                                                                            'Prop Hire','Jukebox','LED Party lights', 'Dance floor'), state='readonly')
    entry_item.grid(column=1,row=4)                                                 
    #number hired
    Label(main_window, text="Number Hired") .grid(column=0,row=5)
    entry_numberhired = Entry(main_window)
    entry_numberhired.grid(column=1,row=5)
    #row number (for when item is returned)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)

'''----------------- Attach a function to the buttons -----------------'''

#PRINT button
    #print the customers' details into a table

def print_hire_details():
    global hire_details, total_entries, name_count, frame
    name_count = 0
    #column headings
    Label(frame, font='Helvetica 10 bold',text="Row").grid(column=0,row=7)
    Label(frame, font='Helvetica 10 bold',text="Customer Name").grid(column=1,row=7)
    Label(frame, font='Helvetica 10 bold',text="Receipt Number").grid(column=2,row=7)
    Label(frame, font='Helvetica 10 bold',text="Item Hired").grid(column=3,row=7)
    Label(frame, font='Helvetica 10 bold',text="Number Hired").grid(column=4,row=7)
    frame.grid(column =1, row=7)
    #each item on the list as a separate row
    while name_count < total_entries :
        Label(frame, text=name_count).grid(column=0,row=name_count+8) 
        Label(frame, text=(hire_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(frame, text=(hire_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(frame, text=(hire_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(frame, text=(hire_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1

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
    #clear the boxes
    entry_name.delete(0,'end')
    entry_receiptnumber.delete(0,'end')
    entry_item.delete(0,'end')
    entry_numberhired.delete(0,'end')
    delete_item.delete(0, 'end')
    total_entries +=1
    
#DELETE button
    #delete a row when an item is returned
def delete_row ():
    global hire_details, delete_item, total_entries, name_count
    try:
    #which row to delete
        del hire_details[int(delete_item.get())]
        total_entries = - 1
        delete_item.delete(0,'end')
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
    #print item to own area of list
        print_hire_details()
    #checking if delete_item is an integer
    except IndexError:
        Label(main_window, fg='red', text="(Numbers only)").grid(column=2,row=6,sticky=W)
    except ValueError:
        Label(main_window, fg='red', text="(Numbers only)").grid(column=2,row=6,sticky=W)

#QUIT button
    #subroutine to exit the program
def quit():
    main_window.destroy()

'''------------------------- Check for validity -------------------------
Set up red error text messages
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
    #correct data type (string)
    if (entry_name.get().isalpha() or (hasSpace and hasAlpha)):  
        Label(main_window, text="                   ").grid(column=2,row=2, sticky=W)
        Label(main_window, text="                   ").grid(column=2,row=2, sticky=W)
        entry_check = 0
    else:
        Label(main_window, fg='red', text="Required (Letters)").grid(column=2,row=2, sticky=W)
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
        Label(main_window, fg='red', text="Required (6 Digits)").grid(column=2,row=3,sticky=W)
        entry_check = 1

#item hired
    #cannot be blank (fill the combobox)
    if len(entry_item.get()) == 0:
        Label(main_window,fg='red',text="Required (Select item)").grid(column=2,row=4,sticky=W)
        entry_check=1

#number hired
    #cannot be blank, correct data type (integer), 1-500 boundary values
    if (entry_numberhired.get().isdigit()):
        if 0 < int(entry_numberhired.get()) <= 500:
            Label(main_window, text="                  ").grid(column=2,row=5,sticky=W)
            Label(main_window, text="                  ").grid(column=2,row=5,sticky=W)
            entry_check = 0
        else:
            Label(main_window, fg='red', text="Required (Numbers 1-500").grid(column=1,row=5,sticky=W)
            Label(main_window, fg='red', text="Required (Numbers 1-500)").grid(column=1,row=5,sticky=W)
            entry_check = 1  
    else:
        Label(main_window, fg='red', text="Required (Numbers 1-500)").grid(column=2,row=5,sticky=W)
        Label(main_window, fg='red', text="Required (Numbers 1-500)").grid(column=2,row=5,sticky=W)
        entry_check = 1

#if all inputs are valid, append to allow for printing
    if entry_check == 0:
        append_details()

'''--------------------- Start the program running ---------------------'''

def main():
    global main_window 
    global hire_details, total_entries,entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries, frame
    #empty list for the details
    hire_details = []
    total_entries = 0
    #GUI
    main_window = Tk()
    main_window.title("Julie's Party Hire")
    frame = Frame(main_window)
    setup_buttons()
    main_window.mainloop()
main()





