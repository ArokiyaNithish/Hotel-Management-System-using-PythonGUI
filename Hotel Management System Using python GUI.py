from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector

# Connecting to MySQL database
try:
    con = mysql.connector.connect(host="localhost", user="User Name", password="Password", database="Database Name")
    print("Database is Connected")
except mysql.connector.Error as err:
    print("Database connection failed:", err)
    exit()

# Insert data into users table
def insert_data():
    GuestID = guest_id_entry.get()
    Name = name_entry.get()
    Number = number_entry.get()
    City = city_entry.get()
    Room = room_entry.get()

    if GuestID and Name:
        try:
            cur = con.cursor()
            sql = "INSERT INTO users (GuestID, Name, Number, City, Room) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, (GuestID, Name, Number, City, Room))
            con.commit()
            messagebox.showinfo("Success", "Data Inserted Successfully")
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "GuestID and Name are required")

# Update user data
def update_data():
    GuestID = guest_id_entry.get()
    Name = name_entry.get()
    Number = number_entry.get()
    City = city_entry.get()
    Room = room_entry.get()

    if GuestID:
        try:
            cur = con.cursor()
            sql = "UPDATE users SET Name=%s, Number=%s, City=%s, Room=%s WHERE GuestID=%s"
            cur.execute(sql, (Name, Number, City, Room, GuestID))
            con.commit()
            messagebox.showinfo("Success", "Data Updated Successfully")
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "GuestID is required for update")

# Delete user data
def delete_data():
    GuestID = guest_id_entry.get()

    if GuestID:
        try:
            cur = con.cursor()
            sql = "DELETE FROM users WHERE GuestID=%s"
            cur.execute(sql, (GuestID,))
            con.commit()
            messagebox.showinfo("Success", "Data Deleted Successfully")
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "GuestID is required to delete")

# Select and display data
def select_data():
    try:
        cur = con.cursor()
        cur.execute("SELECT GuestID, Name, Number, City, Room FROM users")
        rows = cur.fetchall()

        if rows:
            top = Toplevel(root)
            top.title("Guest Data")

            tree = ttk.Treeview(top, columns=("GuestID", "Name", "Number", "City", "Room"), show='headings')
            tree.heading("GuestID", text="GuestID")
            tree.heading("Name", text="Name")
            tree.heading("Number", text="Number")
            tree.heading("City", text="City")
            tree.heading("Room", text="Room")

            for row in rows:
                tree.insert("", END, values=row)

            tree.pack(expand=True, fill=BOTH)
        else:
            messagebox.showinfo("No Data", "No data found in the table.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Clear entry fields
def clear_fields():
    guest_id_entry.delete(0, END)
    name_entry.delete(0, END)
    number_entry.delete(0, END)
    city_entry.delete(0, END)
    room_entry.delete(0, END)

# GUI setup
root = Tk()
root.title("Hotel Management System")
root.geometry("500x300")
root.resizable(False, False)

# Labels & Entry fields
Label(root, text="GuestID").grid(row=0, column=0, padx=10, pady=5, sticky=W)
guest_id_entry = Entry(root)
guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5, sticky=W)
name_entry = Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Number").grid(row=2, column=0, padx=10, pady=5, sticky=W)
number_entry = Entry(root)
number_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="City").grid(row=3, column=0, padx=10, pady=5, sticky=W)
city_entry = Entry(root)
city_entry.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Room").grid(row=4, column=0, padx=10, pady=5, sticky=W)
room_entry = Entry(root)
room_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
Button(root, text="Insert Data", command=insert_data).grid(row=5, column=0, pady=10)
Button(root, text="Update Data", command=update_data).grid(row=5, column=1)
Button(root, text="Select Data", command=select_data).grid(row=5, column=2)
Button(root, text="Delete Data", command=delete_data).grid(row=6, column=0, pady=5)
Button(root, text="Clear Fields", command=clear_fields).grid(row=6, column=1)

root.mainloop()

