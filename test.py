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

# with open("logs.txt",'r') as f:
#     lines = f.readlines()
#     print(lines[0].strip())  # Print the first line without the newline character
#     if len(lines) > 1:
#         print(lines[1].strip()[2])  # Print the third character of the second line without the newline character
#     else:
#         print("File has less than two lines.")

# from tkinter import Radiobutton, Tk, IntVar, W

# r = Tk()
# radio = IntVar(value=1)  # Set the default value to 1 for "Male"
# Radiobutton(r, text="Male", variable=radio, value=1).pack(anchor=W)
# Radiobutton(r, text="Female", variable=radio, value=2).pack(anchor=W)
# r.mainloop()

from  tkinter import Tk,Canvas
# from tkinter import ttk
# from customtkinter import *
# root = Tk()
# root.geometry("1350x700")

# style = ttk.Style()
# style.configure('Rounded.TEntry',padding=45)
# ttk.Label(text="Regi No:112123/075/076",font=("Arial",8),foreground="black").place(x=930,y=5)

# label=ttk.Label(text="HUB IT GROUP PVT.LTD.",font=("Arial",30,"bold"),foreground="green")
# label.place(x=460,y=20)
# canvas=Canvas(root,width=90,height=120)
# canvas.place(x=350,y=9)
# circle=canvas.create_oval(2,2,80,80)
# circle1=canvas.create_oval(70,9,62,16,fill="green")
# circle2=canvas.create_oval(61,2,54,10,fill="green")

# circle3=canvas.create_oval(7,60,15,70,fill="green")
# circle4=canvas.create_oval(70,67,60,76,fill="green")
# label=ttk.Label(text="IT",font=("Arial",12,"bold"),foreground="green",width=2).place(x=405,y=37)
# label2=ttk.Label(text="Butwal-09 (Ganesh Path) Milanchowk",font=("Arial",13,"bold"),foreground="black")
# ttk.Label(text="ph: 071-532805, 9827494116, 9827494119",font=("Arial",13,"bold"),foreground="black").place(x=535,y=95)
# label2.place(x=550,y=70)
# head=CTkLabel(root,text="STUDENT ENROLLMENT REGISTRATION FORM",
#               font=("Arial",25,"bold"),
#               text_color="white",
#               fg_color="green",
#               anchor="center",
#               width=800,
#               corner_radius=5)
# head.place(x=245,y=125)
# headl=CTkLabel(root,text="FULL NAME:",
#               font=("Arial",18),
#               text_color="Black",
#               fg_color="#80ffff",
#               corner_radius=5)
# headl.place(x=245,y=167)
# headle=ttk.Entry(root,justify="center",style="Rounded.TButton",width=55,font=("Arial",13)).place(x=363,y=167)
# frame=CTkFrame(root,width=170,height=151,fg_color="white").place(x=875,y=167)
# CTkLabel(root,text="ADDRESS:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=245,y=205)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=56,font=("Arial",13)).place(x=354,y=205)
# CTkLabel(root,text="CELL NO:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=245,y=250)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=25,font=("Arial",13)).place(x=350,y=250)
# CTkLabel(root,text="Date:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=595,y=250)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=23,font=("Arial",13)).place(x=650,y=250)
# CTkLabel(root,text="GUARDIAN's NAME:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=245,y=290)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=48,font=("Arial",13)).place(x=427,y=290)

# CTkLabel(root,text="PHONE NO:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=245,y=325)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=75,font=("Arial",13)).place(x=362,y=325)
# CTkLabel(root,text="GENDER:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=245,y=360)
# gen=["Male","Female"]
# ttk.Combobox(root,values=gen,font=("Arial",13)).place(x=342,y=360)
# CTkLabel(root,text="DATE OF BIRTH:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=560,y=360)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=35,font=("Arial",13)).place(x=720,y=360)
# CTkLabel(root,text="EMAIL:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#             corner_radius=5).place(x=245,y=400)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=79,font=("Arial",13)).place(x=325,y=400)
# CTkLabel(root,text="LEVEL OF EDUCATION:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#         corner_radius=5).place(x=245,y=440)
# lvl=["see",+2,"Bachelor","Masters"]
# ttk.Combobox(root,values=lvl,font=("Arial",13),width=62).place(x=465,y=440)
# CTkLabel(root,text="NAME OF THE SCHOOL/COLLEGE:",
#             font=("Arial",18),
#             text_color="Black",
#             fg_color="#80ffff",
#         corner_radius=5).place(x=245,y=480)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=52,font=("Arial",13)).place(x=568,y=480)
# CTkLabel(root,text="NAME OF COURSE/S TO ENROLL",
#               font=("Arial",25,"bold"),
#               text_color="white",
#               fg_color="green",
#               anchor="center",
#               width=800,
#               corner_radius=5).place(x=245,y=520)

# ttk.Entry(root,justify="center",style="Rounded.TButton",width=48,font=("Arial",13)).place(x=262,y=560)
# CTkLabel(root,text="1",
#               font=("Arial",25,"bold"),
#               text_color="white",
#               fg_color="#80ffff",
#               anchor="center",
#               corner_radius=5).place(x=245,y=560)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=48,font=("Arial",13)).place(x=262,y=600)
# CTkLabel(root,text="2",
#               font=("Arial",25,"bold"),
#               text_color="white",
#               fg_color="#80ffff",
#               anchor="center",
#               corner_radius=5).place(x=245,y=600)
# ttk.Entry(root,justify="center",style="Rounded.TButton",width=48,font=("Arial",13)).place(x=262,y=640)
# CTkLabel(root,text="3",
#               font=("Arial",25,"bold"),
#               text_color="white",
#               fg_color="#80ffff",
#               anchor="center",
#               corner_radius=5).place(x=245,y=640)

# ttk.Entry(root,justify="center",style="Rounded.TButton",width=48,font=("Arial",13)).place(x=262,y=640)
# CTkLabel(root,text="OTHER COURSE PREVIOUSLY TAKEN",
#               font=("Arial",18,"bold"),
#               text_color="white",
#               fg_color="#80ffff",
#               anchor="center",
#               corner_radius=5).place(x=705,y=560)
# a=ttk.Entry(root,justify="center",style="Rounded.TEntry",font=("Arial",13)).place(x=710,y=590)
# root.mainloop()

# from tkinter import Text, Tk, Canvas, Scrollbar, ttk
# from customtkinter import CTkFrame

# def on_mousewheel(event):
#     canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# root = Tk()
# root.geometry("1350x700")


# # Create a scrollable frame
# canvas = Canvas(root, bg="#cdfefe", width=1350, height=700, scrollregion=(0, 0, 900, 100))
# canvas.pack(side="left", expand=True, fill="both")

# scrollbar = Scrollbar(root, command=canvas.yview)
# scrollbar.pack(side="right", fill="y")
# canvas.configure(yscrollcommand=scrollbar.set)

# frame1 = ttk.Frame(canvas,width=1200, height=1200, style='TFrame')
# canvas.create_window((70, 600), window=frame1, anchor="sw")

# # Bind mouse wheel event to canvas
# canvas.bind_all("<MouseWheel>", on_mousewheel)

# style = ttk.Style()
# style.configure('Rounded.TEntry')


# ttk.Label(frame1, text="Regi No:112123/075/076", font=("Arial", 8), foreground="black").place(x=930, y=5)

# label = ttk.Label(frame1, text="HUB IT GROUP PVT.LTD.", font=("Arial", 30, "bold"), foreground="green")
# label.place(x=460, y=20)
# canvas_logo = Canvas(frame1, width=90, height=120, bd=0)
# canvas_logo.place(x=350, y=9)
# circle = canvas_logo.create_oval(2, 2, 80, 80)
# circle1 = canvas_logo.create_oval(70, 9, 62, 16, fill="green")
# circle2 = canvas_logo.create_oval(61, 2, 54, 10, fill="green")

# circle3 = canvas_logo.create_oval(7, 60, 15, 70, fill="green")
# circle4 = canvas_logo.create_oval(70, 67, 60, 76, fill="green")


# label2 = ttk.Label(frame1, text="Butwal-09 (Ganesh Path) Milanchowk", font=("Arial", 13, "bold"), foreground="black")
# ttk.Label(frame1, text="ph: 071-532805, 9827494116, 9827494119", font=("Arial", 13, "bold"), foreground="black").place(x=535, y=95)
# label2.place(x=550, y=70)
# head = ttk.Label(frame1, text="STUDENT ENROLLMENT REGISTRATION FORM",
#                 font=("Arial", 25, "bold"),
#                 background="green",
#                 width=45,
#                 anchor="center",
#                 foreground="white")
# head.place(x=245, y=125)
# headl = ttk.Label(frame1, text="FULL NAME:",
#                  font=("Arial", 18),
#                  background="#609f9f",
#                  foreground="#80ffff")
# headl.place(x=245, y=167)
# headle = ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13))
# headle.place(x=390, y=167)
# frame2 = ttk.Frame(frame1, width=170, height=151, style='TFrame')
# frame2.place(x=875, y=167)
# ttk.Label(frame1, text="ADDRESS:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=205)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13)).place(x=370, y=205)
# ttk.Label(frame1, text="CELL NO:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=250)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=25, font=("Arial", 13)).place(x=360, y=250)
# ttk.Label(frame1, text="Date:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=595, y=250)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=23, font=("Arial", 13)).place(x=657, y=250)
# ttk.Label(frame1, text="GUARDIAN's NAME:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=290)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=44, font=("Arial", 13)).place(x=469, y=290)

# ttk.Label(frame1, text="PHONE NO:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=325)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=73, font=("Arial", 13)).place(x=382, y=325)
# ttk.Label(frame1, text="GENDER:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=360)
# gen = ["Male", "Female"]
# ttk.Combobox(frame1, values=gen,width=18, font=("Arial", 13)).place(x=360, y=360)
# ttk.Label(frame1, text="DATE OF BIRTH:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=560, y=360)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=32, font=("Arial", 13)).place(x=754, y=360)
# ttk.Label(frame1, text="EMAIL:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=400)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=79, font=("Arial", 13)).place(x=326, y=400)
# ttk.Label(frame1, text="LEVEL OF EDUCATION:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=440)
# lvl = ["see", +2, "Bachelor", "Masters"]
# ttk.Combobox(frame1, values=lvl, font=("Arial", 13), width=56).place(x=520, y=440)
# ttk.Label(frame1, text="NAME OF THE SCHOOL/COLLEGE:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=480)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=44, font=("Arial", 13)).place(x=648, y=480)
# ttk.Label(frame1, text="NAME OF COURSE/S TO ENROLL",
#           font=("Arial", 25, "bold"),
#          anchor="center",
#          background="green",
#          width=45,
#          foreground="white").place(x=245, y=515)

# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13)).place(x=268, y=560)
# ttk.Label(frame1, text="1",
#           font=("Arial", 25, "bold"),
#           background="#609f9f",
#           foreground="#80ffff").place(x=245, y=560)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=262, y=600)
# ttk.Label(frame1, text="2",
#           font=("Arial", 25, "bold"),
#           background="#609f9f",
#           foreground="#80ffff").place(x=245, y=600)

# ttk.Label(frame1, text="3",
#           font=("Arial", 25, "bold"),
#           background="#609f9f",
#           foreground="#80ffff").place(x=245, y=640)

# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13)).place(x=268, y=640)
# ttk.Label(frame1, text="OTHER COURSE PREVIOUSLY TAKEN",
#           font=("Arial", 14, "bold"),
#           background="#609f9f",
#           foreground="#80ffff").place(x=705, y=560)

# frame = CTkFrame(frame1, width=170, height=151, fg_color="white")
# frame.place(x=878, y=170)
# ttk.Label(frame1, text="shift time",
#           font=("Arial", 14, "bold"),
#           background="#609f9f",
#           foreground="#80ffff").place(x=708, y=640)
# Text(frame1,width=39,height=2,font=("Arial", 13)).place(x=705, y=590)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=33, font=("Arial", 13)).place(x=754, y=640)
# ttk.Label(frame1, text="RULES & REGULATIONS",
#           font=("Arial", 25, "bold"),
#          anchor="center",
#          background="green",
#          width=45,
#          foreground="white").place(x=245,y=690)
# ttk.Label(frame1,  wraplength=1200, justify="left",text="1.He/she should will be resposible for any damage done to the property owned by the institution and will be charged accordily\n2.Half of the fee should be paid within first week and remaing should be paid by the end scond week.Fees are not refundable\n3.Student should inform the institution if he/she will not be able to attend any class\n4.it is compulsory to attend any extra classes,seminars,field visits and internships and other programs that institution sees fit to\n deploy any student with respective to their course & field of the interest.\n5.certificate wil not be provided for incomplete courses.\nBy signing below, I hereby agree on all the terms and conditions mentioned above.  "
#           ,
#           font=("Arial", 10),
#          width=150,

#          foreground="black").place(x=245,y=730)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13)).place(x=255, y=850)
# ttk.Label(frame1, text="COORDINATOR",
#           font=("Arial", 15,"bold"),
#           foreground="black").place(x=255,y=880)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13)).place(x=865, y=850)
# ttk.Label(frame1, text="STUDENT",
#           font=("Arial", 15,"bold"),
#           foreground="black").place(x=955,y=880)

# ttk.Label(frame1, text="FOR OFFICE USE ONLY",
#           font=("Arial", 25, "bold"),
#          anchor="center",
#          background="green",
#          width=45,
#          foreground="white").place(x=245,y=920)
# headl = ttk.Label(frame1, text="FULL NAME:",
#                  font=("Arial", 18),
#                  background="#609f9f",
#                  foreground="#80ffff")
# headl.place(x=245, y=980)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=73, font=("Arial", 13)).place(x=390, y=980)
# ttk.Label(frame1, text="ADDRESS:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=1020)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=35, font=("Arial", 13)).place(x=370, y=1020)
# ttk.Label(frame1, text="DATE OF BIRTH:",
#          font=("Arial", 15),
#          background="#609f9f",
#          foreground="#80ffff").place(x=698, y=1020)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13)).place(x=865, y=1020)
# ttk.Label(frame1, text="REFERRED BY:",
#          font=("Arial", 16),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=1060)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=24, font=("Arial", 13)).place(x=406, y=1060)
# ttk.Label(frame1, text="REFFERAL CONTACT NO:",
#          font=("Arial", 15),
#          background="#609f9f",
#          foreground="#80ffff").place(x=630, y=1060)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=19, font=("Arial", 13)).place(x=875, y=1060)
# ttk.Label(frame1, text="DISCOUNT:",
#          font=("Arial", 18),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=1100)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=74, font=("Arial", 13)).place(x=380, y=1100)
# ttk.Label(frame1, text="SOURCES OF INFORMATION:",
#          font=("Arial", 15),
#          background="#609f9f",
#          foreground="#80ffff").place(x=245, y=1140)
# ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=57, font=("Arial", 13)).place(x=530, y=1140)
# ttk.Label(frame1, text="HUB\n    IT", font=("Arial", 12, "bold"), foreground="green", width=4).place(x=370, y=37)
# root.mainloop()


a=[1,4,7]
b=[3,5,8]
c=[6,2,1]
print(list(zip(a,b,c)))
