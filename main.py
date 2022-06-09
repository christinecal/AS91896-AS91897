#Date: Wednesday 8 June
#Name: Christine Calantog

'''This program is to keep track of Julie's party hire '''

from tkinter import *
from tkinter import ttk

#quit subroutine
def quit():
    main_window.destroy()

#create the buttons
def setup_buttons():
    Button(main_window, text="Update",command=append_details) .grid(column=0,row=1)
    Button(main_window, text="Print",command=print_hire_details) .grid(column=1,row=1)
    Button(main_window, text="Quit",command=quit) .grid(column=4, row=1)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)

#create the labels (entries)
    global hire_details, entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries, _item
 #customer name
    Label(main_window, text="Customer Name") .grid(column=0,row=2)
    entry_name = Entry(main_window)
    entry_name.grid(column=1,row=2)
 #receipt number
    Label(main_window, text="Receipt Number") .grid(column=0,row=3)
    entry_receiptnumber = Entry(main_window)
    entry_receiptnumber.grid(column=1,row=3)
 #item hired
    Label(main_window, text="Item Hired") .grid(column=0,row=4)
    item_hired = StringVar()
    entry_item = ttk.Combobox(main_window, textvariable=item_hired, values=('Cutlery Set', 'Glassware Set','Chairs', 'Tables', 'Pack of Balloons', 'Backdrop Hire',
                                                                            'Prop Hire','Jukebox','LED Party lights', 'Dance floor'), state='readonly')
    entry_item.grid(column=1,row=4)                                                 
 #number hired
    Label(main_window, text="Number Hired") .grid(column=0,row=5)
    entry_numberhired = Entry(main_window)
    entry_numberhired.grid(column=1,row=5)
 #row number
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)

#table
#print details of customers' inputs 
def print_hire_details():
    name_count = 0
    #column headings
    Label(main_window, font='Helvetica 10 bold',text="Row").grid(column=0,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Customer Name").grid(column=1,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Item Hired").grid(column=3,row=7)
    Label(main_window, font='Helvetica 10 bold',text="Number Hired").grid(column=4,row=7)
    #each row is the item on the list
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1

#add the next customer to the list
def append_details():
    global hire_details, entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries
    if len(entry_name.get()) != 0 :
        hire_details.append([entry_name.get(),entry_receiptnumber.get(),entry_item.get(),entry_numberhired.get()])
        entry_name.delete(0,'end')
        entry_receiptnumber.delete(0,'end')
        entry_item.delete(0,'end')
        entry_numberhired.delete(0,'end')
        total_entries +=  1
    
#delete a row from the list
def delete_row ():
    pass

#validity checker
#cannot be blank and specific to data input
def check_inputs():
    pass

#start the program running
def main():
    global main_window 
    global hire_details, total_entries
    hire_details = []
    total_entries = 0
    main_window = Tk()
    main_window.title("Julie's Party Hire")
    setup_buttons()
    main_window.mainloop()
main()
