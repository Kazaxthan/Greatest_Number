import tkinter as tk
import customtkinter as ctk

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

window = ctk.CTk()
window.title("PLD ASSIGNMENT 3")
window.geometry('1200x1000')
frame = ctk.CTkFrame(window)
frame.pack(expand = True)

#front end
entry1 = ctk.CTkEntry(frame, placeholder_text="Enter data")
entry1.pack(padx= 30, pady= 30)
entry2 = ctk.CTkEntry(frame, )
entry2.pack(padx= 30, pady= 30)
entry3 = ctk.CTkEntry(frame, )
entry3.pack(padx= 30, pady= 30)
entry = ctk.CTkFrame





window.mainloop()
