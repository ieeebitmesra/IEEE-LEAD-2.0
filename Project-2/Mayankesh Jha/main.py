from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("840x450")
root.configure(background="white")
root.resizable(FALSE,FALSE)
root.title("   JOB SCRAPPER")
root.wm_iconbitmap("icon.ico")

image = Image.open("main_img.jpg")
photo = ImageTk.PhotoImage(image)
lab1= Label(image= photo)
lab1.pack()

def naukri_sehwag(event):
    os.system('python naukri.py')
    root.quit()

def google_sehwag(event):
    os.system('python google_search.py ')
    root.quit()

def times_kob_opener(event):
    os.system('python times_job.py')
    root.quit()

f = Frame(root, bg="light gray")
b = Button(f,text="NAUKRI.COM",font="Helvetica 25 ", padx=16,pady=5)
b.pack(side= LEFT, padx=2, pady=2)
b.bind("<Button-1>",naukri_sehwag)
b.configure( background="silver")
b = Button(f,text="GOOGLE SEARCH",font="Helvetica 25 ", padx=16,pady=5)
b.pack(side= LEFT, padx=2, pady=2)
b.bind("<Button-1>",google_sehwag)
b.configure( background="silver")
b = Button(f,text="TIMES JOB",font="Helvetica 25 ", padx=16,pady=5)
b.pack(side= LEFT, padx=2, pady=2)
b.bind("<Button-1>",times_kob_opener)
b.configure( background="silver")
f.pack()

mainloop()