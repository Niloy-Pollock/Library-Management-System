import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class ArticleDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management Dashboard")
        self.master.geometry("1200x800")

        # Set the main background color
        self.bg_color = "#333"  # Sidebar and entire page color
        self.master.configure(bg=self.bg_color)

        # Top frame for search bar, profile button, and dropdown menu
        self.top_frame = tk.Frame(self.master, bg=self.bg_color, height=50)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create the dropdown menu
        self.create_dropdown_menu()

        # Create search bar and profile button
        self.create_search_bar()

        self.create_profile_button()

        # Left Sidebar for navigation buttons
        self.sidebar = tk.Frame(self.master, bg=self.bg_color, width=200, height=800)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Add navigation buttons to the sidebar
        self.create_sidebar_buttons()

        # Canvas for the main content area with scroll capability for the articles
        self.canvas = tk.Canvas(self.master, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the canvas
        self.scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame inside the canvas to hold article cards
        self.articles_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window((0, 0), window=self.articles_frame, anchor="nw")

        # Load and display articles
        self.articles = self.load_articles()  # Placeholder article data
        self.create_article_grid()

        # Update the canvas scroll region
        self.articles_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Bind mouse scroll and keyboard arrow keys
        self.master.bind("<MouseWheel>", self.on_mouse_wheel)
        self.master.bind("<Up>", self.scroll_up)
        self.master.bind("<Down>", self.scroll_down)

    def create_search_bar(self):
        # Frame for search bar to center it in the top frame
        search_bar_frame = tk.Frame(self.top_frame, bg=self.bg_color)
        search_bar_frame.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)

        # Canvas for rounded search bar background
        search_canvas = tk.Canvas(
            search_bar_frame,
            width=500,
            height=50,  # Increased height for the canvas
            bg=self.bg_color,
            bd=0,
            highlightthickness=0
        )
        search_canvas.pack(side=tk.TOP)

        # Draw rounded rectangle for search bar background
        radius = 20  # Adjusted for rounder corners
        search_canvas.create_oval(0, 0, 2*radius, 2*radius, fill="#444", outline="")
        search_canvas.create_oval(500-2*radius, 0, 500, 2*radius, fill="#444", outline="")
        search_canvas.create_rectangle(radius, 0, 500-radius, 2*radius, fill="#444", outline="")

        # Entry widget for search input
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            search_canvas,
            textvariable=self.search_var,
            font=("Arial", 12),
            width=30,   # Adjusted width for padding space around search button
            relief="flat",
            bg="#444",  # Match rounded background color
            fg="white",
            insertbackground="white"
        )
        # Adjust y position and height for the search entry to fit inside the new rounded rectangle size
        self.search_entry.place(x=radius + 10, y=5, width=400, height=30)  # Adjusted y position and height
        self.search_entry.bind("<Return>", lambda event: self.search_articles())

        # Load the custom search icon
        try:
            search_icon_image = Image.open("image/search.png")
            search_icon_image = search_icon_image.resize((20, 20), Image.LANCZOS)
            self.search_icon = ImageTk.PhotoImage(search_icon_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.search_icon = None

        # Search button inside the search bar at the right edge
        search_button = tk.Button(
            search_canvas,
            image=self.search_icon,
            command=self.search_articles,
            bg="#444",  # Background color
            activebackground="#444",  # Same color for active (clicked) state
            relief="flat",
            cursor="hand2"
        )
        search_button.place(x=460, y=5, width=30, height=30)  # Adjusted position

        # Bind enter and leave events to keep background color consistent
        search_button.bind("<Enter>", lambda e: search_button.config(bg="#444"))
        search_button.bind("<Leave>", lambda e: search_button.config(bg="#444"))


    def search_articles(self):
        query = self.search_var.get()
        if query:
            messagebox.showinfo("Search", f"Searching for: {query}")
        else:
            messagebox.showinfo("Search", "Please enter a search query.")

    def create_dropdown_menu(self):
        # Options for the dropdown menu
        options = ["Option 1", "Option 2", "Option 3"]
        
        # Create a variable to hold the selected option
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])

        # Create the OptionMenu widget (borderless)
        dropdown_menu = ttk.OptionMenu(self.top_frame, self.selected_option, *options)
        
        # Remove the hover effect by setting style and no relief
        style = ttk.Style()
        style.configure("TMenubutton", relief="flat", background=self.bg_color, foreground="white", padding=10)
        style.map("TMenubutton", background=[("active", self.bg_color)])  # Avoid hover effect
        
        dropdown_menu.config(style="TMenubutton", width=15)

        # Access the internal Menu of OptionMenu and change its appearance
        dropdown_menu.option_add('*TMenu*background', self.bg_color)  # Set background color for options
        dropdown_menu.option_add('*TMenu*foreground', 'white')  # Set foreground color for options

        dropdown_menu.pack(side=tk.LEFT, padx=10, pady=10)

    def create_sidebar_buttons(self):

        try:
            logout_icon_image = Image.open("image/logout.png")
            logout_icon_image = logout_icon_image.resize((20, 20), Image.LANCZOS)  # Adjust icon size as needed
            self.logout_icon = ImageTk.PhotoImage(logout_icon_image)
        except Exception as e:
            print(f"Error loading logout image: {e}")
            self.logout_icon = None

        # Add Book Button
        add_book_button = tk.Button(self.sidebar, text="Add Book", command=self.add_book, bg="#444", fg="white", font=("Arial", 12), width=20, height=2)
        add_book_button.pack(pady=10)
        
        # Edit Book Info Button
        edit_book_button = tk.Button(self.sidebar, text="Edit Book Info", command=self.edit_book_info, bg="#444", fg="white", font=("Arial", 12), width=20, height=2)
        edit_book_button.pack(pady=10)
        
        # View All Books Button
        view_books_button = tk.Button(self.sidebar, text="View All Books", command=self.view_all_books, bg="#444", fg="white", font=("Arial", 12), width=20, height=2)
        view_books_button.pack(pady=10)
        
    # Log Out Button with image (placed at the bottom of the sidebar)
    # Canvas for the rounded rectangle logout button
        logout_canvas = tk.Canvas(self.sidebar, width=160, height=50, bg=self.bg_color, bd=0, highlightthickness=0)
        logout_canvas.pack(side=tk.BOTTOM, pady=10)

        # Draw rounded rectangle for logout button background
        radius = 20  # Adjust for roundness of corners
        x0, y0, x1, y1 = 0, 0, 160, 50  # Coordinates for button
        logout_canvas.create_oval(x0, y0, x0 + 2 * radius, y0 + 2 * radius, fill="#444", outline="")
        logout_canvas.create_oval(x1 - 2 * radius, y0, x1, y0 + 2 * radius, fill="#444", outline="")
        logout_canvas.create_oval(x0, y1 - 2 * radius, x0 + 2 * radius, y1, fill="#444", outline="")
        logout_canvas.create_oval(x1 - 2 * radius, y1 - 2 * radius, x1, y1, fill="#444", outline="")
        logout_canvas.create_rectangle(x0 + radius, y0, x1 - radius, y1, fill="#444", outline="")
        logout_canvas.create_rectangle(x0, y0 + radius, x1, y1 - radius, fill="#444", outline="")

        # Place the icon and text on the logout button
        if self.logout_icon:
            logout_canvas.create_image(30, 25, image=self.logout_icon, anchor="center")
        logout_canvas.create_text(90, 25, text="Log Out", fill="white", font=("Arial", 12))

        # Bind the canvas to act as a button
        logout_canvas.bind("<Button-1>", lambda event: self.logout())
            

    def load_articles(self):
        return [
            {"title": "Understanding Python Basics", "description": "Learn the fundamentals of Python programming."},
            {"title": "Advanced Data Science Techniques", "description": "Dive into machine learning and data analysis."},
            {"title": "AI and Machine Learning", "description": "Explore the world of AI and ML."},
            {"title": "Web Development Guide", "description": "Get started with HTML, CSS, and JavaScript."},
            {"title": "Exploring Data Structures", "description": "A deep dive into algorithms and data structures."},
            {"title": "Introduction to Databases", "description": "Learn the basics of databases and SQL."},
            {"title": "Introduction to Linux", "description": "A beginner's guide to using Linux."},
            {"title": "Cloud Computing 101", "description": "An introduction to cloud computing and services."},
            {"title": "Introduction to Git and GitHub", "description": "Learn version control with Git and GitHub."},
            {"title": "Building REST APIs with Python", "description": "Learn how to build and consume REST APIs with Python."},
            {"title": "Introduction to TensorFlow", "description": "Learn the basics of TensorFlow for deep learning."},
            {"title": "Getting Started with Docker", "description": "A beginner's guide to containerization with Docker."},
            {"title": "React for Beginners", "description": "An introduction to React and building UI components."},
            {"title": "Introduction to Kubernetes", "description": "Learn about Kubernetes for container orchestration."},
            {"title": "Machine Learning Algorithms", "description": "A look into the most common machine learning algorithms."},
            {"title": "JavaScript for Web Development", "description": "Learn the fundamentals of JavaScript programming."},
            {"title": "Deep Dive into Python Libraries", "description": "Explore popular Python libraries for data science."},
            {"title": "Introduction to SQL Queries", "description": "Learn how to write SQL queries to interact with databases."},
            {"title": "Building Mobile Apps with Flutter", "description": "A guide to building mobile apps with Flutter."},
            {"title": "Data Visualization with Python", "description": "Learn how to create stunning data visualizations using Python."},
            {"title": "Python for Data Analysis", "description": "Learn to analyze data with Python and popular libraries."},
            {"title": "Advanced Machine Learning", "description": "Explore advanced topics in machine learning and AI."},
            {"title": "Blockchain and Cryptocurrency", "description": "An introduction to blockchain technology and cryptocurrency."},
            {"title": "Cybersecurity Basics", "description": "Learn the fundamentals of cybersecurity and protecting systems."},
            {"title": "Introduction to Virtualization", "description": "A beginner's guide to virtualization technology."},
            {"title": "Data Science with R", "description": "Learn the basics of data science using R programming language."},
            {"title": "Building Web Scrapers with Python", "description": "Learn how to scrape data from the web using Python."},
            {"title": "Artificial Intelligence in Healthcare", "description": "How AI is transforming the healthcare industry."},
            {"title": "Natural Language Processing", "description": "An introduction to NLP and its applications in AI."},
            {"title": "Introduction to NoSQL Databases", "description": "Learn the basics of NoSQL databases like MongoDB."},
            {"title": "Data Cleaning with Python", "description": "Learn how to clean and preprocess data for analysis."},
            {"title": "Introduction to Big Data", "description": "A guide to understanding big data concepts and tools."},
            {"title": "Exploring Data Science Tools", "description": "Overview of popular tools in the data science ecosystem."},
        ]

    def create_article_grid(self):
        # Update the number of columns dynamically based on the window width
        available_width = self.canvas.winfo_width()
        card_width = 330  # Approximate width for each card including padding
        columns = max(1, available_width // card_width)  # At least 1 column
        
        row = 0
        col = 0

        # Remove any existing widgets in the articles_frame
        for widget in self.articles_frame.winfo_children():
            widget.destroy()

        # Loop through each article and create a card
        for article in self.articles:
            # Adjust the card size to fit dynamically in a row
            card = tk.Frame(self.articles_frame, bg="#444", bd=1, relief="solid", width=200, height=200)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            title_label = tk.Label(card, text=article["title"], fg="white", font=("Arial", 12), bg="#444", wraplength=300)
            title_label.pack(pady=5)

            desc_label = tk.Label(card, text=article["description"], fg="white", font=("Arial", 10), bg="#444", wraplength=300)
            desc_label.pack(pady=5)

            col += 1
            if col >= columns:  # Move to the next row after filling the columns
                col = 0
                row += 1

        # Configure column and row stretching
        for i in range(columns):
            self.articles_frame.grid_columnconfigure(i, weight=1, uniform="equal")

        for i in range(row + 1):
            self.articles_frame.grid_rowconfigure(i, weight=1)

        # Update the canvas scroll region after creating the grid
        self.articles_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Bind to window resize event to recalculate layout
        self.canvas.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.create_article_grid()  # Recreate grid on resize

    def create_profile_button(self):
        # Canvas for the round profile button
        profile_canvas = tk.Canvas(self.top_frame, width=50, height=50, bg=self.bg_color, bd=0, highlightthickness=0)
        profile_canvas.pack(side=tk.RIGHT, padx=10, pady=10)

        # Draw a circular button background
        profile_canvas.create_oval(0, 0, 50, 50, fill="#444", outline="")

        # Load and add the profile icon to the center of the button
        try:
            profile_icon_image = Image.open("image/profile.png")
            profile_icon_image = profile_icon_image.resize((30, 30), Image.LANCZOS)
            self.profile_icon = ImageTk.PhotoImage(profile_icon_image)
        # Place the icon image at the center (25, 25)
            profile_canvas.create_image(25, 25, image=self.profile_icon, anchor="center")
        except Exception as e:
            print(f"Error loading profile image: {e}")

        # Bind the click event on the canvas to open the profile
        profile_canvas.bind("<Button-1>", lambda event: self.open_profile())

    def scroll_up(self, event=None):
        self.canvas.yview_scroll(-1, "units")

    def scroll_down(self, event=None):
        self.canvas.yview_scroll(1, "units")

    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        else:
            self.canvas.yview_scroll(1, "units")

    def open_profile(self):
        messagebox.showinfo("Profile", "Opening Profile Page")

    def add_book(self):
        messagebox.showinfo("Add Book", "Opening Add Book Page")

    def edit_book_info(self):
        messagebox.showinfo("Edit Book Info", "Opening Edit Book Info Page")

    def view_all_books(self):
        messagebox.showinfo("View All Books", "Opening All Books Page")

    def logout(self):
        self.master.quit()


# Create the main window and run the application
root = tk.Tk()
app = ArticleDashboard(root)
root.mainloop()
