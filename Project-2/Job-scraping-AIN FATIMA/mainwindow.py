from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
#defining functions to open various windows

def openGSR():
    os.system('python googlescrapper.py')

def openFSR():
    os.system('python jobscrapper.py')

def openPC():
    os.system('python jobcomparer.py')

#adding images to the label 
GSRLogo = ImageTk.PhotoImage(Image.open("google.png"))
FSRLogo = ImageTk.PhotoImage(Image.open("jobfresher.png"))
PCLogo = ImageTk.PhotoImage(Image.open("compare3.png"))

LabelGSRLogo = Label(image=GSRLogo,height=400,width=500)
LabelFSRLogo = Label(image=FSRLogo,height=400,width=400)
LabelPCLogo = Label(image=PCLogo,height=400,width=400)

LabelGSRLogo.grid(column=0, row=0)
LabelFSRLogo.grid(column=1, row=0)
LabelPCLogo.grid(column=2, row=0)


#adding&configuring command buttons of the windows
GSRButton = Button(root, text="Google Search Results", command=openGSR, bg='#333', fg='white', borderwidth=5)
GSRButton.config(font=(15))
GSRButton.grid(column=0, row=1, pady=10)

FSRButton = Button(root, text="Freshersworld Search Results", command=openFSR, bg='#333', fg='white', borderwidth=5)
FSRButton.config(font=(15))
FSRButton.grid(column=1, row=1, pady=10)

PCButton = Button(root, text="Job Comparator", command=openPC, bg='#333', fg='white', borderwidth=5)
PCButton.config(font=(15))
PCButton.grid(column=2, row=1, pady=10)

exitButton = Button(root, text="Exit", command=root.quit, padx=20, bg='#333', fg='white', borderwidth=2)
exitButton.config(font=(14))
exitButton.grid(column=1, row=6, pady=10, columnspan=3)


root.mainloop()
