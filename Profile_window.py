import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Profile:
    def __init__(self, master):
        # Create a new Toplevel window for the Profile page
        self.master = master
        self.profile_window = tk.Toplevel(master)
        self.profile_window.title("Profile Dashboard")
        self.profile_window.state("zoomed")

        # Handle the close event like a logout
        self.profile_window.protocol("WM_DELETE_WINDOW", self.logout)

        # Load and set the background image for the whole window
        self.background_image = Image.open("image/books6.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.bg_label = tk.Label(self.profile_window, image=self.background_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Header Section
        header_frame = tk.Frame(self.profile_window, bg="#3A6EA5", height=50, bd=0)
        header_frame.pack(fill=tk.X)
        header_label = tk.Label(header_frame, text="DASHBOARD", font=("Arial", 24, "bold"), fg="white", bg="#3A6EA5")
        header_label.pack(pady=10)

        # Date Label in the topmost right corner
        date_label = tk.Label(self.profile_window, text="Date: 23/12/2024", font=("Arial", 16), bg="#FFFFFF")
        date_label.pack(side=tk.TOP, anchor="ne", padx=20, pady=10)  # Positioned to the top right

        # User Info Section
        user_info_frame = tk.Frame(self.profile_window, bg="#FFFFFF", padx=20, pady=10, bd=2, relief="groove")
        user_info_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        tk.Label(user_info_frame, text="Username: Farhan", font=("Arial", 30), bg="#FFFFFF").grid(row=0, column=0, sticky="w")
        tk.Label(user_info_frame, text="Email: farhan@gmail.com", font=("Arial", 16), bg="#FFFFFF").grid(row=1, column=0, sticky="w")
        tk.Label(user_info_frame, text="Phone: 0192874849", font=("Arial", 16), bg="#FFFFFF").grid(row=2, column=0, sticky="w")
        tk.Label(user_info_frame, text="Address: Mirpur, Dhaka", font=("Arial", 16), bg="#FFFFFF").grid(row=3, column=0, sticky="w")

        # Load and resize images
        self.button_images = {
            "Donate Book": self.load_image("image/add_book.png"),
            "Edit Book": self.load_image("image/edit_book.png"),
            "Return Book": self.load_image("image/return_book1.png"),
            "Show Book": self.load_image("image/book_icon1.png"),
            "Log Out": self.load_image("image/log_out.png")
        }

        # Buttons Section
        buttons_frame = tk.Frame(self.profile_window, bg="#E7DEB6", bd=0)  # Set the background to a matching color
        buttons_frame.pack(side=tk.LEFT, padx=20, pady=(10, 20))

        buttons = [
            ("Donate Book", self.button_images["Donate Book"]),
            ("Edit Book", self.button_images["Edit Book"]),
            ("Return Book", self.button_images["Return Book"]),
            ("Show Book", self.button_images["Show Book"]),
            ("Log Out", self.button_images["Log Out"])
        ]

        for text, img in buttons:
            button = tk.Button(
                buttons_frame,
                text=text,
                image=img,
                compound=tk.LEFT,
                font=("Arial", 14),
                width=150,
                bg="#D7C2A8",  # Button background color
                activebackground="#D7C2A8",
                relief="sunken",
                command=lambda t=text: self.on_button_click(t)
            )
            button.pack(pady=10)  # Added padding for spacing between buttons

        # Table Section
        table_frame = tk.Frame(self.profile_window, bg="white")
        table_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=(0, 20))

        columns = ("date", "book", "operation", "submission_date", "submitted_date")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)

        # Define headings and add sample data
        for col in columns:
            self.table.heading(col, text=col.title())
            self.table.column(col, anchor="center")

        sample_data = [
            ("1/2/23", "Book 1", "Donate", "1/3/23", "1/3/23"),
            ("2/2/23", "Book 2", "Edit", "1/4/23", "1/4/23"),
            ("3/2/23", "Book 3", "Return", "1/5/23", "1/5/23")
        ]

        for row in sample_data:
            self.table.insert("", "end", values=row)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_x = ttk.Scrollbar(table_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscroll=scrollbar_x)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.table.pack(expand=True, fill=tk.BOTH)

    def load_image(self, path):
        """Loads and resizes an image to fit within the button."""
        img = Image.open(path)
        img = img.resize((24, 24), Image.LANCZOS)  # Resize to smaller dimensions
        return ImageTk.PhotoImage(img)

    def on_button_click(self, text):
        if text == "Donate Book":
            self.open_add_book_window()
        elif text == "Log Out":
            self.logout()

    def open_add_book_window(self):
        """Opens a new window for adding a book's information."""
        add_book_window = tk.Toplevel(self.profile_window)
        add_book_window.title("Add New Book")
        add_book_window.geometry("400x400")

        fields = ["Name", "Writer", "Publisher", "Language", "Genre", "Quantity"]
        entries = {}

        # Generate input fields
        for i, field in enumerate(fields):
            label = tk.Label(add_book_window, text=f"{field}:", font=("Arial", 14))
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = tk.Entry(add_book_window, font=("Arial", 14))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[field] = entry

        # Save button to capture data
        save_button = tk.Button(
            add_book_window,
            text="Save",
            font=("Arial", 14),
            command=lambda: self.save_book_info(entries)
        )
        save_button.grid(row=len(fields), column=0, columnspan=2, pady=20)

    def save_book_info(self, entries):
        """Extracts and prints the data from the entry fields."""
        book_info = {field: entry.get() for field, entry in entries.items()}
        print("Book Information:", book_info)  # Placeholder for actual save logic

    def logout(self):
        """Handles logout: close profile window and show login window."""
        self.profile_window.destroy()
        self.master.deiconify()  # Show the login window again

# To run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Profile(root)
    root.mainloop()
