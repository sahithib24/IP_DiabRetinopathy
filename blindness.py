# Importing all packages
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image
import os

import mysql.connector
from tkinter.filedialog import askopenfilename, asksaveasfilename
import mysql.connector as sk
from model import *
#from send_sms import *
print('GUI SYSTEM STARTED...')
#---------------------------------------------------------------------------------

def OpenFile():
        try:
            a = askopenfilename()
            if a:
             print(a)
             value, classes = main(a)
             messagebox.showinfo("your report", ("Predicted Label is ", value, "\nPredicted Class is ", classes))

             image = Image.open(a)
            # plotting image
             file = image.convert('RGB')
             plt.imshow(np.array(file))
             plt.title(f'your report is label : {value} class : {classes}')
             plt.show()
            #print(image)
             print('Thanks for using the system !')
            #fn, text = os.path.splitext(a) #fn stands for filename
        except Exception as error:
            print("File not selected ! Exiting..., Please try again")

#-----------------------------------------------------------------------------------------


root = Tk()

root.geometry('700x400')
root.title("Blindness Detection System (Demo)")
root.configure(bg='pale turquoise')

label1 = Label(root, text="Blindness Detection System", font=('Arial', 30))
label1.grid(padx=30, pady=30, row=0, column=0, sticky='W')

button2 = Button(root, text="Upload Image", command=OpenFile)
button2.grid(padx=10, pady=20, row=1, column=1)

root.mainloop()