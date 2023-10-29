import tkinter as tk
import ttkbootstrap as ttk


class MENU:

    def __init__(self):
        self.email = ""
        self.password = ""
        self.nickname = ""

    
    def show(self, player):
        def login():
            def handle_login():
                self.password = pass_entry.get()
                self.email = email_entry.get()

                #print(f"{self.email}, {self.password}")
                
                if player.login(self.email, self.password) == True:
                    window.destroy()
                else: 
                    error_label['text'] = 'Usuario o contraseña incorrecta'
                

            buttons_frame.destroy()
            
            login_frame = ttk.Frame(master = window)

            email_label = ttk.Label(master = login_frame, text = 'email:' )
            email_label.grid(row = 0, column = 0, pady = 10)

            email_entry = tk.StringVar()
            email_box = ttk.Entry(master = login_frame, textvariable = email_entry)
            email_box.grid(row = 0, column = 1, pady = 10)

            pass_label = ttk.Label(master = login_frame, text = 'password:' )
            pass_label.grid(row = 1, column = 0, pady = 10)

            pass_entry = tk.StringVar()
            pass_box = ttk.Entry(master = login_frame, show = '*', textvariable = pass_entry)
            pass_box.grid(row = 1, column = 1, pady = 10)

            check_login = ttk.Button(master = login_frame, text = 'Login', width = 12, command = handle_login) #pending to check functionality
            check_login.grid( row = 2, column = 1, pady = 20, padx = 5)

            error_label = ttk.Label(master = login_frame, text = "" )
            error_label.grid(row = 3, column = 1, pady=20)

            login_frame.columnconfigure(0, weight = 1)
            login_frame.pack(pady = 20)

            
            

        def register():
            def handle_register():
                self.email = email_entry.get()
                self.password = pass_entry.get()
                self.nickname = nick_entry.get()

                #print(f"{self.email}, {self.password}, {self.nickname}")

                if player.register(self.email, self.password, self.nickname) == True:
                    player.login(self.email, self.password)
                    window.destroy()
                else:
                    error_label['text'] = 'correo o nickname en uso.'
                
            buttons_frame.destroy()

            register_frame = ttk.Frame(master = window)

            email_label = ttk.Label(master = register_frame, text = 'Email:' )
            email_label.grid(row = 0, column = 0, pady = 10)

            email_entry = tk.StringVar()
            email_box = ttk.Entry(master = register_frame, textvariable = email_entry)
            email_box.grid(row = 0, column = 1, pady = 10)

            pass_label = ttk.Label(master = register_frame, text = 'Password:' )
            pass_label.grid(row = 1, column = 0, pady = 10)

            pass_entry = tk.StringVar()
            pass_box = ttk.Entry(master = register_frame,show = '*', textvariable = pass_entry)
            pass_box.grid(row = 1, column = 1, pady = 10)

            nickname_label = ttk.Label(master = register_frame, text = 'Nickname:' )
            nickname_label.grid(row = 2, column = 0, pady = 10)

            nick_entry = tk.StringVar()
            pass_box = ttk.Entry(master = register_frame, textvariable = nick_entry)
            pass_box.grid(row = 2, column = 1, pady = 10)

            check_register = ttk.Button(master = register_frame, text = 'Register', width = 12, command = handle_register) #pending to check functionality
            check_register.grid( row = 3, column = 1, pady = 20, padx = 5)

            error_label = ttk.Label(master = register_frame, text = "" )
            error_label.grid(row = 4, column = 1, pady=20)

            register_frame.pack(pady = 20)

        def guest():
            player.login()
            window.destroy()
            
                
        #main window
        window = ttk.Window(themename = 'darkly')
        window.title('Snake Game')
        window.geometry('500x300')

        #title
        title_label = ttk.Label(
            master = window,
            text = "Welcome to Snake Game!", 
            font = 'Calibri 24 bold')
        title_label.pack()

        #buttons
        buttons_frame = ttk.Frame(master = window)

        login_button = ttk.Button(master = buttons_frame, text = "Login", command = login, width = 12)
        login_button.grid(row = 0, column = 0, pady = 10)

        register_button = ttk.Button(master = buttons_frame, text = 'Register', command = register, width = 12)
        register_button.grid(row = 1, column = 0, pady = 10)

        guest_button = ttk.Button(master = buttons_frame, text= 'Play as Guest', command = guest, width = 12)
        guest_button.grid(row = 2, column = 0, pady = 10)

        buttons_frame.columnconfigure(0, weight = 1)
        buttons_frame.pack(pady = 20)

        #run
        window.mainloop()




