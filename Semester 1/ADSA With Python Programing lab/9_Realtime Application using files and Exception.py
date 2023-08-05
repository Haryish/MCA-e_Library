from tkinter import *
from tkinter.filedialog import askopenfilename

# Create a root window
r = Tk()

# Create a menubar
mb = Menu(r)


def newfile():
    print("Creating new file")


def openfile():
    name = askopenfilename()
    print(name)


def create_menu1():
    # Create the "File" menu
    fl = Menu(mb)
    
    # Create menu items for "File" menu
    fl.add_command(label="New", command=newfile)
    fl.add_separator()
    fl.add_command(label="Open", command=openfile)
    fl.add_separator()
    fl.add_command(label="Exit")

    # Add "File" menu to the menubar
    mb.add_cascade(label="File", menu=fl)


def create_menu2():
    # Create the "Edit" menu
    m2 = Menu(mb)
    
    # Create menu items for "Edit" menu
    m2.add_command(label="Copy")
    m2.add_separator()
    m2.add_command(label="Paste")

    # Add "Edit" menu to the menubar
    mb.add_cascade(label="Edit", menu=m2)


# Calling functions to create menus
create_menu1()
create_menu2()

# Attach menubar to the root window
r.config(menu=mb)

# Set the title of the root window
r.title("Python Menubar Example")

# Set the size of the root window
r.geometry("310x350")

# Show the root window
r.mainloop()
