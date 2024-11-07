import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from data import Student, Book, add_book, add_student

class RegistrationWindow:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)  # Create a new top-level window
        self.window.title("Register")

        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()

        # self.window.geometry(f"{width}x{height}")
        self.window.state("zoomed")
        # Load the background image
        self.background_image = Image.open("image/books2.jpg")  # Replace with your image path
        self.background_image = self.background_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.background_label = tk.Label(self.window, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window

        # Welcome label
        self.welcome_label = tk.Label(self.window, text="Welcome To The Universe Of Knowledge",
                                       font=("Arial", 16, "bold"), bg="#FFFFFF", 
                                       borderwidth=2, relief=tk.SOLID)
        self.welcome_label.pack(pady=10, padx=10, fill=tk.X)

        # Create main frame for registration
        self.main_frame = tk.Frame(self.window, bg="#FFFFFF", bd=5, relief=tk.RAISED)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400)  # Center the frame

        # Registration title
        self.registration_title = tk.Label(self.main_frame, text="Register Here", font=("Arial", 20, "bold"), bg="#FFFFFF")
        self.registration_title.pack(pady=10)

        # Create registration form fields
        self.create_form()

    def create_form(self):
        # List of labels and types
        form_fields = [
            ("Username:", "text"),
            ("Email:", "email"),
            ("Phone:", "number"),
            ("Address:", "text"),
            ("Password:", "password"),
            ("Confirm Password:", "password"),
        ]

        self.entries = {}

        # Define consistent spacing values
        label_padding = 5  # Padding below the label
        entry_padding = 5   # Padding above the entry field

        for label_text, field_type in form_fields:
            # Create a frame for each input
            frame = tk.Frame(self.main_frame, bg="#FFFFFF")
            frame.pack(pady=5)  # Frame padding

            # Label
            label = tk.Label(frame, width=15, text=label_text, justify='left', bg="white", fg="#333", font=("Arial", 12, "bold"))
            label.pack(side=tk.LEFT, padx=10, pady=(0, label_padding))  # Consistent bottom padding for labels

            # Entry
            entry = tk.Entry(frame, width=30, borderwidth=2, relief=tk.SUNKEN, font=("Arial", 12))
            if field_type == "password":
                entry.config(show="*")  # Mask password
            entry.pack(side=tk.LEFT, padx=10, pady=(entry_padding, 0))  # Consistent top padding for entries
            self.entries[label_text] = entry

        # Submit button
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit, width=15, bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=20)


    def submit(self):
        # Here you would add your registration logic
        name = self.entries["Username:"].get()
        email = self.entries["Email:"].get()
        phone = self.entries["Phone:"].get()
        address = self.entries["Address:"].get()
        password = self.entries["Password:"].get()
        confirm_password = self.entries["Confirm Password:"].get()

        if password == confirm_password:
            messagebox.showinfo("Registration", f"Registered successfully!\nName: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}")
            # Clear fields after registration
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.window.destroy()  # Close the registration window
            self.master.deiconify()  # Restore the main window
        else:
            messagebox.showwarning("Registration", "Passwords do not match!")


# Run the application
