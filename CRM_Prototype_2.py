from cgitb import text
from distutils.command.config import config
from itertools import count
from logging import root
from operator import index
from optparse import Values
from tkinter import *
from tkinter import ttk
from turtle import width
#from matplotlib import pyplot as plt
import sqlite3

########################## GUI SetUp ############################################

app = Tk()
app.title('CRM')
app.geometry("1050x600")

######################### DB Setup ##############################################

# DB Datas
"""
data = [[1,"example", "example", "example", "example", "example", 1], 
        [2,"example", "example", "example", "example", "example", 1],
        [3,"example", "example", "example", "example", "example", 1],
        [4,"example", "example", "example", "example", "example", 1],
        [5,"example", "example", "example", "example", "example", 1],
        [6,"example", "example", "example", "example", "example", 1],
        [7,"example", "example", "example", "example", "example", 1], 
        [8,"example", "example", "example", "example", "example", 1],
        [9,"example", "example", "example", "example", "example", 1],
        [10,"example", "example", "example", "example", "example", 1],
        [11,"example", "example", "example", "example", "example", 1],
        [12,"example", "example", "example", "example", "example", 1],
        [13,"example", "example", "example", "example", "example", 1], 
        [14,"example", "example", "example", "example", "example", 1],
        [15,"example", "example", "example", "example", "example", 1],
        [16,"example", "example", "example", "example", "example", 1],
        [17,"example", "example", "example", "example", "example", 1],
        [18,"example", "example", "example", "example", "example", 1],
        [19,"example", "example", "example", "example", "example", 1], 
        [20,"example", "example", "example", "example", "example", 1],
        [21,"example", "example", "example", "example", "example", 1],
        [22,"example", "example", "example", "example", "example", 1],
        [23,"example", "example", "example", "example", "example", 1],
        [24,"example", "example", "example", "example", "example", 1]]
"""

# Create/Connect to a database 
conn = sqlite3.connect('crm.db')

# Create Cursor Instance 
c = conn.cursor()

# Tables


# Create Table Kinder

#PRAGMA foreign_keys;

c.execute("""CREATE TABLE IF NOT EXISTS kinder (
    id_k integer PRIMARY KEY, 
    vorname text, 
    nachname text, 
    alt integer,
    geschlecht text, 
    strasse text,
    h_nummer integer, 
    stadt text,
    plz text,
    kontaktperson text,
    gruppe_id integer,

    FOREIGN KEY(id_g) 
        REFERENCES gruppe (id_g),
    FOREIGN KEY(id_p) 
        REFERENCES person_k (id_p)

    )""")
  


# Create Table person_k
c.execute("""CREATE TABLE IF NOT EXISTS person_k (
    id_p integer PRIMARY KEY,
    vornname text, 
    nachname text, 
    alt integer,
    strasse text,
    h_nummer integer, 
    stadt text,
    plz text,
    verwandschaft text
    )""")
   
'''
# Create Table erzieher
c.execute("""CREATE TABLE IF NOT EXISTS erzieher (
    id_e integer, PK
    vornname text, 
    nachname text, 
    alt integer,
    strasse text,
    h_nummer integer, 
    stadt text,
    plz text,
    id_k integer FK 1.. to 1..many
    id_g integer FK 1..many to 1..many
    )""")
'''    
'''
# Create Table gruppe
c.execute("""CREATE TABLE IF NOT EXISTS gruppe (
    id_g integer, PK
    gruppenname text, 
    id_k integer FK, 1..many to 1
    id_e integer FK
    )""")
'''     

# Add Dummy Data
"""
for record in data:
    c.execute("INSERT INTO kinder VALUES(:id, :rolle, :name, :nachname, :addresse, :stadt, :plz)",
        {
        'id': record[0],     
        'rolle': record[1],
        'name': record[2],
        'nachname': record[3],
        'addresse': record[4],
        'stadt': record[5],
        'plz': record[6]
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

    c.execute("SELECT * FROM kinder")
    records = c.fetchall()

    # Add Data to the Screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow', ))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow', ))
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
style.map("Treview",
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
my_tree['columns'] = ("1", "2", "3", "4", "5", "6", "7")

# Formate Columns Table
my_tree.column("#0", width=0, stretch=NO) #Ghost

my_tree.column("1", anchor=CENTER, width=140, stretch=NO)
my_tree.column("2", anchor=CENTER, width=140, stretch=NO)
my_tree.column("3", anchor=CENTER, width=140, stretch=NO)
my_tree.column("4", anchor=CENTER, width=140, stretch=NO)
my_tree.column("5", anchor=CENTER, width=140, stretch=NO)
my_tree.column("6", anchor=CENTER, width=140, stretch=NO)
my_tree.column("7", anchor=CENTER, width=140, stretch=NO)

# Create Heading
my_tree.heading("#0", text="", anchor=W) #Ghost

my_tree.heading("1", text="ID", anchor=CENTER)
my_tree.heading("2",text="Name",anchor=CENTER)
my_tree.heading("3",text="Nachname",anchor=CENTER)
my_tree.heading("4",text="Addresse", anchor=CENTER)
my_tree.heading("5",text="Stadt",anchor=CENTER)
my_tree.heading("6",text="PLZ", anchor=CENTER)
my_tree.heading("7",text="Rolle", anchor=CENTER)

########################## Label/Entries GUI SetUp #################################

# Adding Record Entry Boxes Frame
data_frame = LabelFrame(app, text="Record")
data_frame.pack(fill="x", expand="yes", pady=20)

id_l = Label(data_frame, text="ID")
id_l.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10) 

rolle_l = Label(data_frame, text="Rolle")
rolle_l.grid(row=0, column=2, padx=10, pady=10)
rolle_entry = Entry(data_frame)
rolle_entry.grid(row=0, column=3, padx=10, pady=10)

name_l = Label(data_frame, text="Name")
name_l.grid(row=1, column=0, padx=10, pady=10)
name_entry = Entry(data_frame)
name_entry.grid(row=1, column=1, padx=10, pady=10)

nachname_l = Label(data_frame, text="Nachname")
nachname_l.grid(row=1, column=2, padx=10, pady=10)
nachname_entry = Entry(data_frame)
nachname_entry.grid(row=1, column=3, padx=10, pady=10)

addresse_l = Label(data_frame, text="Addresse")
addresse_l.grid(row=1, column=4, padx=10, pady=10)
addresse_entry = Entry(data_frame)
addresse_entry.grid(row=1, column=5, padx=10, pady=10)

stadt_l = Label(data_frame, text="Stadt")
stadt_l.grid(row=1, column=8, padx=10, pady=10)
stadt_entry = Entry(data_frame)
stadt_entry.grid(row=1, column=9, padx=10, pady=10)

plz_l = Label(data_frame, text="PLZ")
plz_l.grid(row=1, column=10, padx=10, pady=10)
plz_entry = Entry(data_frame)
plz_entry.grid(row=1, column=11, padx=10, pady=10)

######### Label QueryCommands ###########
# Here implement functions to filter search

######### Button Commands ###########

# Remove One Records
def remove_one():
    x = my_tree.selection()
    my_tree.delete(x)

# Remove Many Selected Records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

# Remove Many Selected Records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

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
    rolle_entry.delete(0, END)
    name_entry.delete(0, END)
    nachname_entry.delete(0, END)
    addresse_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)

# Select Records
def select_record(e):
    # Clear entry Boxes
    id_entry.delete(0, END)
    rolle_entry.delete(0, END)
    name_entry.delete(0, END)
    nachname_entry.delete(0, END)
    addresse_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)

    # Grab Record Number
    selected = my_tree.focus()
    # Grab Record Values
    values = my_tree.item(selected, 'values')

    # Output Entry Boxes
    id_entry.insert(0, values[0])
    rolle_entry.insert(0, values[1])
    name_entry.insert(0, values[2])
    nachname_entry.insert(0, values[3])
    addresse_entry.insert(0, values[4])
    stadt_entry.insert(0, values[5])
    plz_entry.insert(0, values[6])

# Update Record
def update_record():
    # Grab the Record Number
    selected = my_tree.focus()
    # Update Record
    my_tree.item(selected, text="", values= (id_entry.get(), rolle_entry.get(), name_entry.get(), nachname_entry.get(), addresse_entry.get(), stadt_entry.get(), plz_entry.get(),))

    # Clear entry Boxes
    id_entry.delete(0, END)
    rolle_entry.delete(0, END)
    name_entry.delete(0, END)
    nachname_entry.delete(0, END)
    addresse_entry.delete(0, END)
    stadt_entry.delete(0, END)
    plz_entry.delete(0, END)

############## Buttons ####################

# Add Buttons
button_frame = LabelFrame(app, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Boxes", command= clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

########################## Events Bindings ################################

# Bind the Treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Plot The Datas 

"""
plot_x = [1,2,3,4,5,6]

plot_y = [10,20,30,40,50,60]

plt.plot(plot_x, plot_y)
plt.show()

"""

# Run to pull data from database on start

query_database()

app.mainloop()
