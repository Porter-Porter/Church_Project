import tkinter as tk
from PIL import ImageTk
from PIL import Image

# initialize app
# root = tk.Tk()
# root.title("Church Project")
# root.eval("tk::PlaceWindow . center")

# x = root.winfo_screenmmwidth() // 2
# y = int(root.winfo_screenheight() * 0.1)
# root.geometry('1200x600+' + str(x) + '+' + str(y))


# frame1 = tk.Frame(root, width=1200, height=800, bg="#FFD700")
# frame1.grid(row=0, column=0)


# frame1 widgets
# logo_img = Image.open(file='web-development-html.png')
# logo_img = tk.PhotoImage(frame1, image=logo_img)
# logo_label = tk.Label(frame1, image=logo_img)
# logo_label.image = logo_img
# logo_label.pack()


class MyGUI:

    def __init__ (self):

    self.root = tk.TK()

    self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
    self.label.pack(padx=10, pady=10)

    self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
    self.textbox.pack(padx=10, pady=10)

    sefl.check = tk.Checkbutton(self.root, text="Show Message", font=('Arial', 16))
    self.check.pack(padx=10, pady=10)











# run app
root.mainloop()