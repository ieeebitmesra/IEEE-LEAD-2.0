from tkinter import *
from PIL import ImageTk
import PIL.Image
import os 

root = Tk()
root.title("Main GUI")
root.geometry("800x550")
root.configure(background='white')

def google_search():
    os.system('python google_search.py')

def job_search():
    os.system("python job_scrapper_gui.py")

def job_compare():
    os.system("python job_compare.py")

option_frame = LabelFrame(root,bg="white",borderwidth=0,highlightthickness=0)

google_frame = LabelFrame(option_frame,bg="white",borderwidth=0,highlightthickness=0)
google_img = ImageTk.PhotoImage(PIL.Image.open("./Images\google.png"))
google_img_label = Label(google_frame,image = google_img,bg='white')
google_button = Button(google_frame,text="Google search",bg="white",fg="#135EC2",font=('Bahnschrift Light', 13, 'bold'),command=google_search)

job_search_frame = LabelFrame(option_frame,bg="white",borderwidth=0,highlightthickness=0)
job_search_img = ImageTk.PhotoImage(PIL.Image.open("./Images\logo.png"))
job_search_img_label = Label(job_search_frame,image = job_search_img,bg='white')
job_search_button = Button(job_search_frame,text="Job Search",bg="white",fg="#135EC2",font=('Bahnschrift Light', 13, 'bold'),command=job_search)

job_compare_frame = LabelFrame(option_frame,bg="white",borderwidth=0,highlightthickness=0)
job_compare_img = ImageTk.PhotoImage(PIL.Image.open("./Images\compare1.png"))
job_compare_img_label=Label(job_compare_frame,image = job_compare_img,bg='white')
job_compare_button = Button(job_compare_frame,text="Compare",bg="white",fg="#135EC2",font=('Bahnschrift Light', 13, 'bold'),command=job_compare)

option_frame.pack(pady=50,padx=50)

google_frame.pack(pady=10,padx=10)
google_img_label.pack(side=LEFT,padx=10)
google_button.pack(pady=25)

job_search_frame.pack(pady=25,padx=5)
job_search_img_label.pack(side=LEFT,padx=10)
job_search_button.pack(padx=5,pady=10)

job_compare_frame.pack(pady=30,padx=2)
job_compare_img_label.pack(side=LEFT,padx=10)
job_compare_button.pack(padx=5,pady=5)




root.mainloop()
