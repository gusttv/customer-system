import tkinter as tk
import sqlite3
from create_database import create_database

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}"

class RegisterForm(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Customer Management")
        self.geometry("400x400")

        create_database()
        self.conn = sqlite3.connect("customers.db")
        self.cursor = self.conn.cursor()

        self.name_label = tk.Label(self, text="Name")
        self.name_entry = tk.Entry(self)
        self.email_label = tk.Label(self, text="Email")
        self.email_entry = tk.Entry(self)
        self.register_button = tk.Button(self, text="Create", command=self.register)
        self.list_customers_button = tk.Button(self, text="List Customers", command=self.list_customers)

        self.name_label.pack()
        self.name_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.register_button.pack()
        self.list_customers_button.pack()

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()

        self.cursor.execute("""
        INSERT INTO customers (name, email)
        VALUES (?, ?)
        """, (name, email))
        self.conn.commit()

        print("Customer Created Successfully!")

    def list_customers(self):
        self.cursor.execute("""
        SELECT * FROM customers
        """)
        customers = self.cursor.fetchall()

        for customer in customers:
            id, name, email = customer
            print(f"ID: {id}\n{Customer(name, email)}")

app = RegisterForm()
app.mainloop()
