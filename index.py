import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from registration import RegistrationWindow
from data import Authenticate
from Profile_window import Profile

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")

        # User credentials
        self.user_name = "farhan"
        self.pass_code = "1234"

        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()

        # self.master.geometry("800x600")
        # self.master.geometry(f"{width}x{height}")
        self.master.state("zoomed")

        # Load the background image
        self.background_image = Image.open("image/books2.jpg")  # Replace with your image path
        self.background_image = self.background_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.background_label = tk.Label(self.master, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window

        # Create a main frame for the content
        self.main_frame = tk.Frame(self.master, bg="#FFFFFF", bd=5, relief=tk.RAISED)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400)  # Center the frame

        # Welcome label
        self.welcome_label = tk.Label(self.master, text="Welcome To The Universe Of Knowledge",
                                       font=("Arial", 16, "bold"), bg="white", fg="black", 
                                       borderwidth=2, relief=tk.SOLID)
        self.welcome_label.pack(pady=10, padx=10, fill=tk.X)

        # Create a login title
        self.login_title = tk.Label(self.main_frame, text="Log In", font=("Arial", 20, "bold"), bg="#FFFFFF")
        self.login_title.pack(pady=10)

        # Create login frame
        self.login_frame = tk.Frame(self.main_frame, bg="white", bd=5, pady=10, relief=tk.RAISED)
        self.login_frame.pack(pady=20, padx=20, fill=tk.BOTH)

        # Username frame
        self.username_frame = tk.Frame(self.login_frame, bg="#FFFFFF")
        self.username_frame.pack(pady=5)  # Add some vertical padding

        self.username_label = tk.Label(self.username_frame, text="Username:", bg="#FFFFFF")
        self.username_label.pack(side=tk.LEFT, padx=10)  # Align label to the left
        self.username_entry = tk.Entry(self.username_frame, width=30, borderwidth=2, relief=tk.SUNKEN)
        self.username_entry.pack(side=tk.LEFT, padx=10)  # Align entry to the left

        # Password frame
        self.password_frame = tk.Frame(self.login_frame, bg="#FFFFFF")
        self.password_frame.pack(pady=5)  # Add some vertical padding

        self.password_label = tk.Label(self.password_frame, text="Password:", bg="#FFFFFF")
        self.password_label.pack(side=tk.LEFT, padx=10)  # Align label to the left
        self.password_entry = tk.Entry(self.password_frame, show="*", width=30, borderwidth=2, relief=tk.SUNKEN)
        self.password_entry.pack(side=tk.LEFT, padx=10)  # Align entry to the left

        # Button frame for Login and Register buttons
        self.button_frame = tk.Frame(self.login_frame, bg="white")
        self.button_frame.pack(pady=20)  # Add some vertical padding

        # Login button
        self.login_button = tk.Button(self.button_frame, text="Login", command=self.login, width=15, bg="#4CAF50", fg="white")
        self.login_button.pack(side=tk.LEFT, padx=5)  # Align button to the left

        # Register button
        self.register_button = tk.Button(self.button_frame, text="Register", command=self.open_registration_window, width=15, bg="#4CAF50", fg="white")
        self.register_button.pack(side=tk.LEFT, padx=5)  # Align button to the left

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check credentials
        # if (username == self.user_name) and (password == self.pass_code):
        #     messagebox.showinfo("Login", f"Logged in as {username}!")
        if Authenticate(username, password):
            # messagebox.showinfo("Login", f"Logged in as {username}!")
            self.open_profile()
        else:
            messagebox.showwarning("Login", "Invalid username or password.")
        # Clear input fields after login attempt
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def open_registration_window(self):
        self.master.withdraw()  # Minimize the main window
        RegistrationWindow(self.master)

    def open_profile(self):
        # Minimize the main login window and open the Profile window
        self.master.withdraw()
        Profile(self.master)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()