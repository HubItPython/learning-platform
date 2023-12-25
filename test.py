'''
This Tkinter code creates a simple graphical window with a label using Python's Tkinter library. Let's break it down step by step:

Importing Tkinter:
import tkinter as tk imports the Tkinter library and allows you to use its functions and classes using the tk alias.

Creating a Root Window:
root = tk.Tk() creates the main window object. This window is often referred to as the "root" window and serves as the base for all other widgets.

Setting Window Title:
root.title("Hello, Tkinter!") sets the title of the root window to "Hello, Tkinter!".

Adding a Label:
label = tk.Label(root, text="Hello, Tkinter!") creates a label widget. It is added to the root window (root) and displays the text "Hello, Tkinter!".

Packing the Label:
label.pack() places the label within the root window. The pack() method is used to organize widgets within their parent container (in this case, the root window). It adjusts the size of the widgets based on their content and the available space.

Starting the Main Loop:
root.mainloop() starts the Tkinter event loop. This method listens for events such as button clicks, mouse movements, and keyboard inputs. It keeps the window running and responsive to user interactions until the window is closed.

During the execution of mainloop(), the window will be displayed, showing the label "Hello, Tkinter!". The window remains open and responsive to user actions (like clicking, typing, etc.) until it is closed by the user.'''
# import tkinter
# print(dir(tkinter))

# from tkinter import Tk,Button

# def on_button_click():
#     print("Button clicked!")


# root = Tk()
# root.title("Button Example")

# button = Button(root, text="Click Me", command=on_button_click)
# button.pack()

# root.mainloop()


# Sure, here's an example demonstrating the use of each module in Tkinter:

# import tkinter as tk

# root = tk.Tk()
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()

# root.mainloop()

# tkinter.colorchooser

# import tkinter as tk
# import tkinter.colorchooser as cc

# def choose_color():
#     color = cc.askcolor(title="Choose Color")
#     print("Selected color:", color)

# root = tk.Tk()
# button = tk.Button(root, text="Choose Color", command=choose_color)
# button.pack()

# root.mainloop()

# tkinter.commondialog
# This module doesn't have a specific usage example since it serves as a base class for dialogs in other modules.

# tkinter.filedialog

# import tkinter as tk
# import tkinter.filedialog as fd

# def open_file():
#     file_path = fd.askopenfilename(title="Select File")
#     print("Selected file:", file_path)

# root = tk.Tk()
# button = tk.Button(root, text="Open File", command=open_file)
# button.pack()

# root.mainloop()

# tkinter.font

# import tkinter as tk
# import tkinter.font as font

# root = tk.Tk()
# custom_font = font.Font(family="Helvetica", size=12, weight="bold")
# label = tk.Label(root, text="Custom Font", font=custom_font)
# label.pack()

# root.mainloop()

# tkinter.messagebox

# import tkinter as tk
# import tkinter.messagebox as mb

# def show_message():
#     mb.showinfo(title="Info", message="This is an informational message.")

# root = tk.Tk()
# button = tk.Button(root, text="Show Message", command=show_message)
# button.pack()

# root.mainloop()

# tkinter.scrolledtext

# import tkinter as tk
# from tkinter import scrolledtext

# root = tk.Tk()
# scroll_text = scrolledtext.ScrolledText(root, width=30, height=10)
# scroll_text.pack()

# scroll_text.insert(tk.END, "This is a scrolled text widget.")

# root.mainloop()

# tkinter.simpledialog

# import tkinter as tk
# import tkinter.simpledialog as sd

# def ask_user():
#     result = sd.askstring(title="Input", prompt="Enter your name:")
#     print("User entered:", result)

# root = tk.Tk()
# button = tk.Button(root, text="Ask", command=ask_user)
# button.pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# def button_clicked():
#     print("Button clicked")

# root = tk.Tk()
# style = ttk.Style()
# style.configure('TButton', foreground='red')  # Configuring the style of the button

# button = ttk.Button(root, text="Click Me", command=button_clicked, style='TButton')
# button.pack()

# root.mainloop()



# Themed Button

# import tkinter as tk
# from tkinter import ttk

# def button_clicked():
#     print("Button clicked")

# root = tk.Tk()
# style = ttk.Style()
# style.configure('TButton', foreground='blue', font=('Arial', 12))  # Configuring button style

# button = ttk.Button(root, text="Click Me", command=button_clicked, style='TButton')
# button.pack()

# root.mainloop()

# Themed Checkbutton

# import tkinter as tk
# from tkinter import ttk

# def show_selection():
#     print("Selected:", check_var.get())

# root = tk.Tk()
# style = ttk.Style()
# style.configure('TCheckbutton', font=('Arial', 12))  # Configuring checkbutton style

# check_var = tk.BooleanVar()
# checkbutton = ttk.Checkbutton(root, text="Check Me", variable=check_var, command=show_selection, style='TCheckbutton')
# checkbutton.pack()

# root.mainloop()

# Themed Combobox

# import tkinter as tk
# from tkinter import ttk

# def selection_changed(event):
#     print("Selected:", combobox.get())

# root = tk.Tk()
# style = ttk.Style()
# style.configure('TCombobox', font=('Arial', 12))  # Configuring combobox style

# values = ("Option 1", "Option 2", "Option 3")
# combobox = ttk.Combobox(root, values=values, style='TCombobox')
# combobox.pack()
# combobox.bind("<<ComboboxSelected>>", selection_changed)

# root.mainloop()

# Themed Progressbar

# import tkinter as tk
# from tkinter import ttk

# def start_progress():
#     progress.start()

# def stop_progress():
#     progress.stop()

# root = tk.Tk()
# style = ttk.Style()
# style.configure('Horizontal.TProgressbar', background='blue')  # Configuring progressbar style

# progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='indeterminate', style='Horizontal.TProgressbar')
# progress.pack()

# start_button = ttk.Button(root, text="Start", command=start_progress)
# start_button.pack()

# stop_button = ttk.Button(root, text="Stop", command=stop_progress)
# stop_button.pack()

# root.mainloop()

# from tkinter import Tk, Label, Frame, Entry,Button

# fb = Tk()
# fb.title("Facebook - log in or sign up")
# fb.geometry("1366x768")
# fb.config(bg="#00ffff")

# Label(fb, bg="#00ffff", fg="#0040ff", text="facebook", font=('Helvetica', 60, 'bold')).place(x=50, y=230)
# Label(fb, bg="#00ffff", fg="black", text="Connect with friends and the ", font=('Helvetica', 25)).place(x=50, y=330)
# Label(fb, bg="#00ffff", fg="black", text="world around you on facebook. ", font=('Helvetica', 25)).place(x=50, y=370)

# frame = Frame(fb, width=510, height=450, bg='white')
# frame.place(x=760, y=110)
# usr = Entry(fb,width=25, border=2, fg='black', font=('Helvetica', 25))
# usr.place(x=790, y=140)
# usr.insert(0,'Email or phone number')
# passw =Entry(fb,width=25, border=2, fg='black', font=('Helvetica', 25))
# passw.place(x=790,y=220)
# passw.insert(0,'password')
# Button(fb,width=26,text="Log in",fg='white',bg="#0040ff",border=5,font=('Helvetica', 20,'bold')).place(x=790,y=300)
# Button(frame,text="Forget passwrod?",fg='#0040ff',bg="white",border=0,font=('Helvetica', 18)).place(x=160,y=270)
# Button(frame,text="Create new account",fg='white',bg="#00d500",border=5,font=('Helvetica', 20,'bold')).place(x=120,y=350)
# fb.mainloop()

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry("300x200")

# style = ttk.Style()
# style.configure(
#     'Rounded.TButton',
#     borderwidth=5,
#     relief="flat",
#     foreground="black",
#     background="blue",
#     width=150,  # Set the width
#     height=50   # Set the height
# )

# button = ttk.Button(root, text="Rounded Button", style='Rounded.TButton')
# button.pack(padx=20, pady=20)

# root.mainloop()


# import tkinter as tk

# def round_rectangle(canvas, x1, y1, x2, y2, radius=20, **kwargs):
#     points = [x1+radius, y1,
#               x1+radius, y1,
#               x2-radius, y1,
#               x2-radius, y1,
#               x2, y1,
#               x2, y1+radius,
#               x2, y1+radius,
#               x2, y2-radius,
#               x2, y2-radius,
#               x2, y2,
#               x2-radius, y2,
#               x2-radius, y2,
#               x1+radius, y2,
#               x1+radius, y2,
#               x1, y2,
#               x1, y2-radius,
#               x1, y2-radius,
#               x1, y1+radius,
#               x1, y1+radius,
#               x1, y1]

#     return canvas.create_polygon(points, **kwargs, smooth=True)

# root = tk.Tk()
# root.geometry("300x200")

# canvas = tk.Canvas(root, width=150, height=50, highlightthickness=0)
# canvas.pack(padx=20, pady=20)

# round_rectangle(canvas, 0, 0, 150, 50, radius=20, fill="light gray")

# button = tk.Button(root, text="Rounded Button", bd=0, highlightthickness=0)
# button.place(x=20, y=20)

# root.mainloop()

# from tkinter import ttk
# import tkinter

# root = tkinter.Tk()

# style = ttk.Style()
# style.theme_use("default")

# ttk.Combobox().pack()
# tkinter.Button(root, text="press me", height=10).pack()
# ttk.Button(root, text="not me", padding=50).pack(pady=10, padx=10)

# root.mainloop()


# import tkinter
# from tkinter import ttk

# root = tkinter.Tk()

# style = ttk.Style()
# style.map("C.TButton",
#     foreground=[('pressed', 'red'), ('active', 'blue')],
#     background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#     )

# colored_btn = ttk.Entry(text="Test", style="C.TButton").pack()

# root.mainloop()

# from tkinter import ttk
# import tkinter

# root = tkinter.Tk()

# style = ttk.Style()
# style.theme_settings("default", {
#    "TCombobox": {
#        "configure": {"padding": 5},
#        "map": {
#            "background": [("active", "green2"),
#                           ("!disabled", "green4")],
#            "fieldbackground": [("!disabled", "green3")],
#            "foreground": [("focus", "OliveDrab1"),
#                           ("!disabled", "OliveDrab2")]
#        }
#    }
# })

# combo = ttk.Combobox().pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# def change_entry_style():
#     style.configure('CustomEntry.TEntry', foreground='blue', font=('Arial', 12))

# root = tk.Tk()

# # Creating a ttk Style object
# style = ttk.Style()

# # Configuring a custom style for Entry
# style.configure('CustomEntry.TEntry', foreground='red', font=('Helvetica', 10))

# # Creating an Entry widget with the custom style
# entry = ttk.Entry(root, style='CustomEntry.TEntry')
# entry.pack()

# # Button to change the Entry widget's style
# change_style_button = tk.Button(root, text="Change Style", command=change_entry_style)
# change_style_button.pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# # Creating a ttk Style object
# style = ttk.Style()

# # Configuring a custom style for Button with width and height
# style.configure('Custom.TButton', width=200, height=200)

# # Creating a Button with the custom style
# button = ttk.Button(root, text="Custom Size Button", style='Custom.TButton')
# button.pack()

# root.mainloop()


# admin_user="admin"
# admin_pass="adminpass"
# print("Enter username and password for admin or guest access")
# inp_user=input("Username: ")
# inp_pass=input("Password: ")
# username=''
# password=''
# with open("logs.txt",'r') as f:
#     username =f.readline()
#     password = f.readline() 
#     print(username + password) 
# if inp_user==admin_user and inp_pass==admin_pass:
#     inp_guest_user=input("Set Username:")
#     inp_guest_pass=input("Set Passwprd:")
#     with open("logs.txt",'w') as f:
#         f.write(f"{inp_guest_user}\n{inp_guest_pass}")
#         print("Guest Created Successfully")

# elif inp_user==username and inp_pass ==password:
#     print(f"Welcome {username} ")


