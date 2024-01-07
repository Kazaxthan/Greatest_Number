import tkinter as tk
import customtkinter as ctk

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

window = ctk.CTk()
window.title("PLD ASSIGNMENT 3")
window.geometry('1200x1000')
frame = ctk.CTkFrame(window)
frame.pack(expand=True, ipadx=50, ipady=10)


# Back end
def done():
    # Get the input values using get() method
    digit1 = int(entry1.get())
    digit2 = int(entry2.get())
    digit3 = int(entry3.get())

    if digit1 > digit2 and digit1 > digit3:
        highest_digit = digit1
    elif digit2 > digit1 and digit2 > digit3:
        highest_digit = digit2
    else:
        highest_digit = digit3

    # Create a new window for the result
    app = ctk.CTk()
    app.title("RESULT")
    app.geometry('500x500')
    result_frame = ctk.CTkFrame(app)
    result_frame.pack(expand=True)

    # Display the result using a label
    result_label = ctk.CTkLabel(result_frame, text=f"Highest Digit: {highest_digit}", text_color="#FFE5B4",
                                font=("Helvetica", 19))
    result_label.pack()

    app.mainloop()


# Front end
Label_entry1 = ctk.CTkLabel(frame, text="Input One number on each box.")
Label_entry1.pack()

entry1 = ctk.CTkEntry(frame, placeholder_text="INPUT 1")
entry1.pack(padx=30, pady=30)

entry2 = ctk.CTkEntry(frame, placeholder_text="INPUT 2")
entry2.pack(padx=30, pady=30)

entry3 = ctk.CTkEntry(frame, placeholder_text="INPUT 3")
entry3.pack(padx=30, pady=30)

Enter_button = ctk.CTkButton(frame, text="DONE", command=done)
Enter_button.pack()

window.mainloop()
