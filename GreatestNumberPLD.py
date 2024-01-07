import tkinter as tk
import customtkinter as ctk

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

window = ctk.CTk()
window.title("PLD ASSIGNMENT 3")
window.geometry('1200x1000')
frame = ctk.CTkFrame(window)
frame.pack(expand=True, ipadx=50, ipady=10)


#Back end
def done():
    
    input1 = entry1.get().strip()
    input2 = entry2.get().strip()
    input3 = entry3.get().strip()

   
    try:
        #Pag mali
        if not input1 or not input2 or not input3:
            raise ValueError("No special characters")

        digit1 = float(input1)
        digit2 = float(input2)
        digit3 = float(input3)

        #Pag tama
        if digit1 > digit2 and digit1 > digit3:
            highest_digit = digit1
        elif digit2 > digit1 and digit2 > digit3:
            highest_digit = digit2
        else:
            highest_digit = digit3

        # Result Window
        app = ctk.CTk()
        app.title("RESULT")
        app.geometry('500x500')
        result_frame = ctk.CTkFrame(app)
        result_frame.pack(expand=True)
        
        
        result_label = ctk.CTkLabel(result_frame, text=f"Highest Digit: {highest_digit:.2f}", text_color="#FFE5B4",
                                    font=("Helvetica", 35))
        result_label.pack()

        app.mainloop()
        
        # Error code
    except ValueError as e:
    
        error_message = ctk.CTkLabel(frame, text=str(e), text_color="red", font=("Helvetica", 15))
        error_message.pack()


# Front end
Label_entry1 = ctk.CTkLabel(frame, text="Input any number in each box.")
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
