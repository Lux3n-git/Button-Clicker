import tkinter as tk
counter = 0
 
def clickcounter():
    global counter
    counter = counter + 1
    if counter == 1:
        clicknumber.config(text = str(counter) + " Click")
    else:
        clicknumber.config(text = str(counter) + " Clicks")
    
 
 
 
window = tk.Tk()
window.title("Button Clicker")
window.geometry("500x500")
frame = tk.Frame(window)
buttonimg = tk.PhotoImage(file="Red_Button.png")
window.iconphoto(False, buttonimg)
 
 
label = tk.Label(frame, text='Button Clicker').pack(padx=20, pady=10)
label = tk.Button(frame, text='Click', width= 10, height= 5, command=clickcounter).pack(padx=20, pady=10)
clicknumber = tk.Label(frame, text="0 Clicks",)
clicknumber.pack(padx=20, pady=10)
 
frame.pack(padx = 5, pady = 5)
window.mainloop()

