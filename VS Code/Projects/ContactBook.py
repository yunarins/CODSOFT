import tkinter as tk
from tkinter import ttk


# Create the main window
window = tk.Tk()
window.title("Contact Book")

contacts =[]
# Create labels and entry widgets
nameL = tk.Label(window, text="NAME:")
nameL.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
nameI = tk.Entry(window)
nameI.grid(row=0, column=1, padx=5, pady=5)

phoneL = tk.Label(window, text="PHONE:")
phoneL.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
phoneI = tk.Entry(window)
phoneI.grid(row=1, column=1, padx=5, pady=5)

emailL = tk.Label(window, text="EMAIL:")
emailL.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
emailI = tk.Entry(window)
emailI.grid(row=2, column=1, padx=5, pady=5)

addressL = tk.Label(window, text="ADDRESS:")
addressL.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
addressI = tk.Entry(window)
addressI.grid(row=3, column=1, padx=5, pady=5)

searchI = tk.Entry(window) 
searchI.grid(row=4, column=0, padx=5, pady=5)


# Create the Treeview to display contacts
tree = ttk.Treeview(window, columns=("Name", "Phone", "Email", "Address"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.grid(row=9, column=0, columnspan=2, padx=5, pady=5)


# Function to add contact
def AddContact():
    name = nameI.get()
    phone = phoneI.get()
    email = emailI.get()
    address = addressI.get()
    contactID =len(contacts)+1
    contacts.append((name, phone, email, address))
    tree.insert('','end', values=(contactID, name,phone,email,address))
    # Clear input fields after adding contact
    nameI.delete(0, tk.END)
    phoneI.delete(0, tk.END)
    emailI.delete(0, tk.END)
    addressI.delete(0, tk.END)

# Function to view contacts
def ViewContacts():
    # Clear existing entries in the treeview
    for row in tree.get_children():
        tree.delete(row)
    # Insert contacts into treeview
    for i, contact in enumerate(contacts, start=1):
        tree.insert('', 'end', values=contact)

# Function to search contact
def SearchContact():
    query = searchI.get().lower()
    results = [contact for contact in contacts if query in ' '.join(contact).lower()]
    clear_treeview()
    for i, contact in enumerate(results):
        tree.insert('', 'end', text=str(i+1), values=contact)

# Function to clear the treeview
def clear_treeview():
    for item in tree.get_children():
        tree.delete(item)

# Function to update contact
def UpadateContact():
    selected_item = tree.selection()
    if selected_item:
        index = int(tree.item(selected_item)['text']) - 1
        new_name = nameI.get()
        new_phone = phoneI.get()
        new_email = emailI.get()
        new_address = addressI.get()
        contacts[index] = (new_name, new_phone, new_email, new_address)
        ViewContacts()
def DeleteContact():
    selected_item = tree.selection()
    if selected_item:
        index = int(tree.item(selected_item)['values'][0]) - 1
        del contacts[index]
        clear_treeview()
        ViewContacts()


# Create buttons
AddButton = tk.Button(window, text="Add Contact", command=AddContact)
AddButton.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)


ViewButton = tk.Button(window, text="View Contacts", command=ViewContacts)
ViewButton.grid(row=5, column= 1,padx=5, pady=5)

SearchButton = tk.Button(window, text="Search", command=SearchContact)
SearchButton.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

UpdateButton = tk.Button(window, text="Update Contact", command= UpadateContact)
UpdateButton.grid(row=5, column=2, padx=5, pady=5)

DeleteButton = tk.Button(window, text="Delete Contact", command=DeleteContact)
DeleteButton.grid(row=5, column=3, padx=5, pady=5)

window.mainloop()
