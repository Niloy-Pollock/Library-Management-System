Frame(self.profile_window, bg="#FFFFFF", padx=20, pady=10, bd=2, relief="groove")
        user_info_frame.pack(fill=tk.X, padx=20, pady=(20, 10))

        tk.Label(user_info_frame, text="Username: Farhan", font=("Arial", 30), bg="#FFFFFF").grid(row=0, column=0, sticky="w")
        tk.Label(user_info_frame, text="Email: farhan@gmail.com", font=("Arial", 16), bg="#FFFFFF").grid(row=1, column=0, sticky="w")
        tk.Label(user_info_frame, text="Phone: 0192874849", font=("Arial", 16), bg="#FFFFFF").grid(row=2, column=0, sticky="w")
        tk.Label(user_info_frame, text="Address: Mirpur, Dhaka", font=("Arial", 16), bg="#FFFFFF").grid(row=3, column=0, sticky="w")
        tk.Label(user_info_frame, text="