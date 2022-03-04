from cgitb import text
from distutils.command.config import config
from itertools import count
from logging import root
from operator import index
from optparse import Values
from tkinter import *
from tkinter import ttk
from turtle import width
from tkinter import messagebox
import sqlite3
from click import command, option
from numpy import append
from tkinter import colorchooser

########################## GUI SetUp ############################################

app = Tk()
app.title('CRM')
app.geometry("1600x600")
"""
def primary_color():
    pass

def secondary_color():
    pass

def highlite_color():
    pass

# Add Menu
my_menu = Menu(app)
app.config(menu=my_menu)

# config Menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(Label="Options", menu = option_menu)

option_menu.add_command(Label="Change Primary Color", command=primary_color)
option_menu.add_command(Label="Change Secondary Color", command=secondary_color)
option_menu.add_command(Label="Change Higlight Color", command=highlite_color)
option_menu.add_separator()
option_menu.add_command(Label="Exit", command=app.quit)
"""

######################### DB Setup ##############################################

######### Label QueryCommands ###########
#def search_record():

# DB Datas

# FakeData example lists
"""
data = [[1,"vorname", "nachname", 34, "strasse", 10, "stadt", "PLZ", "Dario"], 
        [2,"vorname", "nachname", 34, "strasse", 20, "stadt", "PLZ", "Dieu"],
        [3,"vorname", "nachname", 34, "strasse", 20, "stadt", "PLZ", "Muhannad"],
        [4,"vorname", "nachname", 34, "strasse", 20, "stadt", "PLZ", "David"],
        [5,"vorname", "nachname", 34, "strasse", 20, "stadt", "PLZ", "Ehab"]]
"""

# Create/Connect to a database 
conn = sqlite3.connect('crm.db')
# Create Cursor Instance 
c = conn.cursor()

# Create Table Base (Pivot)
c.execute("""CREATE TABLE IF NOT EXISTS base(
    id integer,
    vorname text, 
    nachname text, 
    alt integer,
    strasse text,
    h_nummer integer, 
    stadt text,
    plz text,
    person text
    )""")
   
# Add Dummy Data
"""
for record in data:
    c.execute("INSERT INTO base VALUES(:id, :vorname, :nachname, :alter, :strasse, :hausnummer, :stadt, :plz, :person)",
       {
        "id": record[0],
        "vorname": record[1],
        "nachname": record[2],
        "alter": record[3],
        "strasse": record[4],
        "hausnummer": record[5],
        "stadt": record[6],
        "plz": record[7],
        "person": record[8]

       } 
    )
"""

# Commit Changes
conn.commit()

# Close Connection
conn.close()

# Query DB
def query_database():
    # Create/Connect to a database 
    conn = sqlite3.connect('crm.db')
    # Create Cursor Instance 
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM base")
    records = c.fetchall()
    #print(records) # Controll Table

    # Add Data to the Screen
    global count
    count = 0

    for record in records:
        print(record) # Controll Records

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9] ), tags=('evenrow', ))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=('oddrow', ))
        # increment counter
        count += 1
    
    
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


########################## GUI Graphic Style SetUp ##############################
# Style
style = ttk.Style()

# Style Theme
style.theme_use('default')

# Configuring Treeview Colors
style.configure("Treeview",
    background="white",
    foreground="black",
    rowheight=25,
    fieldbackground="white"
    )

# Change selected Color
style.map("Treeview",
    background=[('selected', 'blue')]
    )

# Create Treeview Frame
tree_frame = Frame(app)
tree_frame.pack(pady=10)

# Create Treeview ScrollBar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand= tree_scroll.set, selectmode= "extended" )
my_tree.pack()

# Configure ScrollBar
tree_scroll.config(command=my_tree.yview)

# Define Columns Table
my_tree['columns'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

# Formate Columns Table
my_tree.column("#0", width=0, stretch=NO) #Ghost

my_tree.column("1", anchor=CENTER, width=140, stretch=NO)
my_tree.column("2", anchor=CENTER, width=140, stretch=NO)
my_tree.column("3", anchor=CENTER, width=140, stretch=NO)
my_tree.column("4", anchor=CENTER, width=140, stretch=NO)
my_tree.column("5", anchor=CENTER, width=140, stretch=NO)
my_tree.column("6", anchor=CENTER, width=140, stretch=NO)
my_tree.column("7", anchor=CENTER, width=140, stretch=NO)
my_tree.column("8", anchor=CENTER, width=140, stretch=NO)
my_tree.column("9", anchor=CENTER, width=140, stretch=NO)

# Create Heading
my_tree.heading("#0", text="", anchor=W) #Ghost

my_tree.heading("1", text="ID", anchor=CENTER)
my_tree.heading("2",text="Vorname",anchor=CENTER)
my_tree.heading("3",text="Nachname",anchor=CENTER)
my_tree.heading("4",text="Alter",anchor=CENTER)
my_tree.heading("5",text="Strasse", anchor=CENTER)
my_tree.heading("6",text="Hausnummer",anchor=CENTER)
my_tree.heading("7",text="Stadt",anchor=CENTER)
my_tree.heading("8",text="PLZ", anchor=CENTER)
my_tree.heading("9",text="Person", anchor=CENTER)

########################## Label/Entries GUI SetUp #################################

# Adding Record Entry Boxes Frame
data_frame = LabelFrame(app, text="Record")
data_frame.pack(fill="x", expand="yes", pady=20)

id_l = Label(data_frame, text="ID")
id_l.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10) 

vorname_l = Label(data_frame, text="Vorname")
vorname_l.grid(row=1, column=0, padx=10, pady=10)
vorname_entry = Entry(data_frame)
vorname_entry.grid(row=1, column=1, padx=10, pady=10)

nachname_l = Label(data_frame, text="Nachname")
nachname_l.grid(row=1, column=2, padx=10, pady=10)
nachname_entry = Entry(data_frame)
nachname_entry.grid(row=1, column=3, padx=10, pady=10)

alter_l = Label(data_frame, text="Alter")
alter_l.grid(row=1, column=4, padx=10, pady=10)
alter_entry = Entry(data_frame)
alter_entry.grid(row=1, column=5, padx=10, pady=10)

strasse_l = Label(data_frame, text="Strasse")
strasse_l.grid(row=1, column=6, padx=10, pady=10)
strasse_entry = Entry(data_frame)
strasse_entry.grid(row=1, column=7, padx=10, pady=10)

hausnummer_l = Label(data_frame, text="Hausnummer")
hausnummer_l.grid(row=1, column=8, padx=10, pady=10)
hausnummer_entry = Entry(data_frame)
hausnummer_entry.grid(row=1, column=9, padx=10, pady=10)

stadt_l = Label(data_frame, text="Stadt")
stadt_l.grid(row=1, column=10, padx=10, pady=10)
stadt_entry = Entry(data_frame)
stadt_entry.grid(row=1, column=11, padx=10, pady=10)

plz_l = Label(data_frame, text="PLZ")
plz_l.grid(row=1, column=12, padx=10, pady=10)
plz_entry = Entry(data_frame)
plz_entry.grid(row=1, column=13, padx=10, pady=10)

person_l = Label(data_frame, text="Person")
person_l.grid(row=1, column=14, padx=10, pady=10)
person_entry = Entry(data_frame)
person_entry.grid(row=1, column=15, padx=10, pady=10)


######### Button Commands ###########

# Remove One Records
def remove_one():
    x = my_tree.selection()
    my_tree.delete(x)

    # Create/Connect to a database 
    conn = sqlite3.connect('crm.db')
    # Create Cursor Instance 
    c = conn.cursor()
    
    # Delete from DB
    c.execute("DELETE from base where oid=" + id_entry.get())

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear entry Boxes
    clear_entries()

    # Message Box
    messagebox.showinfo("Record Deleted!", "The selected Record has been Deleted")

# Remove Many Selected Records
def remove_many():
    # Message Boxe Are you shure to delete
    response = messagebox.askyesno("Hey YOU!", "Are you shure you wanna delete the selected Records from the Table?")
    # Add Logic for messagebox
    if response == 1:
        # Designate Selections
        x = my_tree.selection()
        
        # Create list of Ids
        ids_to_delete = []
        
        #add Selections to ids_to_delete List
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[0])
        # Delete from Treeview
        for record in x:
            my_tree.delete(record)

        # Create/Connect to a database 
        conn = sqlite3.connect('crm.db')
        # Create Cursor Instance 
        c = conn.cursor()

        # Delete Everything from the table
        c.executemany("DELETE FROM base WHERE oid = ?",[(a,) for a in ids_to_delete])

        # Close Connection
        conn.close()

        # Clear entry Boxes
        clear_entries()

# Remove Many Selected Records
def remove_all():
    # Message Boxe Are you shure to delete
    response = messagebox.askyesno("Hey!", "Are you shure you wanna delete all Records from the Table???!!!")
    # Add Logic for messagebox
    if response == 1:

        for record in my_tree.get_children():
            my_tree.delete(record)

        # Create/Connect to a database 
        conn = sqlite3.connect('crm.db')
        # Create Cursor Instance 
        c = conn.cursor()

        # Delete Everything from the table
        c.execute("DROP TABLE base")

        # Close Connection
        conn.close()

        # Clear entry Boxes
        clear_entries()

        # Recreate Table
        create_table_base_again()

# Move Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Clear Entries
def clear_entries():
    id_entry.delete(0, END)
    vorname_entry.delete(0, END)
    nachname_entry.delete(0, END)
    alter_entry.delete(0, END)
    strasse_entry.delete(0, END)
    hausnummer_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)
    person_entry.delete(0, END)

# Select Records
def select_record(e):
    # Clear entry Boxes
    id_entry.delete(0, END)
    vorname_entry.delete(0, END)
    nachname_entry.delete(0, END)
    alter_entry.delete(0, END)
    strasse_entry.delete(0, END)
    hausnummer_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)
    person_entry.delete(0, END)

    # Grab Record Number
    selected = my_tree.focus()
    # Grab Record Values
    values = my_tree.item(selected, 'values')

    # Output Entry Boxes
    id_entry.insert(0, values[0])
    vorname_entry.insert(0, values[1])
    nachname_entry.insert(0, values[2])
    alter_entry.insert(0, values[3])
    strasse_entry.insert(0, values[4])
    hausnummer_entry.insert(0, values[5])
    stadt_entry.insert(0, values[6])
    plz_entry.insert(0, values[7])
    person_entry.insert(0, values[8])

# Update Record
def update_record():
    # Grab the Record Number
    selected = my_tree.focus()
    # Update Record
    my_tree.item(selected, text="", values= (id_entry.get(), vorname_entry.get(), nachname_entry.get(), alter_entry.get(), strasse_entry.get(), hausnummer_entry.get(), stadt_entry.get(), plz_entry.get(), person_entry.get()))

    # Update the DB

    # Create/Connect to a database 
    conn = sqlite3.connect('crm.db')
    # Create Cursor Instance 
    c = conn.cursor()

    c.execute("""UPDATE base SET
        
        vorname = :vorname,
        nachname = :nachname,
        alt = :alter,
        strasse = :strasse,
        h_nummer =  :hausnummer,
        stadt = :stadt,
        plz = :plz,
        person = :person

        WHERE oid = :oid""",
        {
            'vorname' : vorname_entry.get(),
            'nachname' : nachname_entry.get(), 
            'alter' : alter_entry.get(), 
            'strasse' : strasse_entry.get(), 
            'hausnummer' : hausnummer_entry.get(),
            'stadt' : stadt_entry.get(), 
            'plz' : plz_entry.get(), 
            'person' : person_entry.get(),
            'oid': id_entry.get(),    
        })

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear entry Boxes
    id_entry.delete(0, END)
    vorname_entry.delete(0, END)
    nachname_entry.delete(0, END)
    alter_entry.delete(0, END)
    strasse_entry.delete(0, END)
    hausnummer_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)
    person_entry.delete(0, END)

# add new record to DB
def add_record():
    # Create/Connect to a database 
    conn = sqlite3.connect('crm.db')
    # Create Cursor Instance 
    c = conn.cursor()

    c.execute("INSERT INTO base Values (:id, :vorname, :nachname, :alter, :strasse, :hausnummer, :stadt, :plz, :person)",
        {
            'id': id_entry.get(), 
            'vorname' : vorname_entry.get(),
            'nachname' : nachname_entry.get(), 
            'alter' : alter_entry.get(), 
            'strasse' : strasse_entry.get(), 
            'hausnummer' : hausnummer_entry.get(),
            'stadt' : stadt_entry.get(), 
            'plz' : plz_entry.get(), 
            'person' : person_entry.get(),
                
        }
    )
    
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear entry Boxes
    id_entry.delete(0, END)
    vorname_entry.delete(0, END)
    nachname_entry.delete(0, END)
    alter_entry.delete(0, END)
    strasse_entry.delete(0, END)
    hausnummer_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)
    person_entry.delete(0, END)

    # Clear the GUI Table
    my_tree.delete(*my_tree.get_children())

    # Run to pull data from DB on start
    query_database()

# Create Table Base again
def create_table_base_again():
    # Create/Connect to a database 
    conn = sqlite3.connect('crm.db')
    # Create Cursor Instance 
    c = conn.cursor()

    # Create Table Base (Pivot)
    c.execute("""CREATE TABLE IF NOT EXISTS base(
        id integer,
        vorname text, 
        nachname text, 
        alt integer,
        strasse text,
        h_nummer integer, 
        stadt text,
        plz text,
        person text
        )""")

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    

############## Buttons ####################

# Add Buttons
button_frame = LabelFrame(app, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=3, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=5, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=7, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=9, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=11, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=13, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Boxes", command= clear_entries)
select_record_button.grid(row=0, column=15, padx=10, pady=10)

########################## Events Bindings ################################

# Bind the Treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()

app.mainloop()
