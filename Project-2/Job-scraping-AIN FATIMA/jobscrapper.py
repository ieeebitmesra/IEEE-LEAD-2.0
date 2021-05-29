from bs4 import BeautifulSoup
import requests
from tkinter import *
from PIL import ImageTk,Image  
import webbrowser
import re
from tkinter import messagebox



jobscrapper=Tk()
jobscrapper.config(background="plum")
frame = LabelFrame(jobscrapper, bg="snow",
                    fg="white", borderwidth=10)
frame.pack()
def popupmsg():
    
    
    
    response=messagebox.showerror("Warning", "Sorry! Invalid Search. Try Again!")

    
    popup_label =Label(text=response)
    popup_label.pack()

def click():
    frame2 = LabelFrame(jobscrapper, bg="pink",fg="white", borderwidth=10)
    frame2.pack()
    url="https://www.freshersworld.com/jobs/jobsearch/"+E1.get()+"-jobs-in-"+E2.get()

    html_text=requests.get(url)
    soup = BeautifulSoup(html_text.text,'lxml')
    soup.prettify()
    try:
        compname=soup.find('h3',class_='latest-jobs-title font-16 margin-none inline-block').text
    except:
        popupmsg()
    compname=soup.find('h3',class_='latest-jobs-title font-16 margin-none inline-block').text
    job=soup.find('div',class_='col-md-12 col-xs-12 col-lg-12 padding-none left_move_up')
    jobtitle=job.find('div').text
    qualification=job.find('span',class_='bold_elig').text
    description=soup.find('span',class_='desc').text
    experience=soup.find('span',class_='experience').text
    lastDate=soup.find('span',class_='padding-left-4').text
    def callback(url):
        webbrowser.open_new_tab(url)
    Lab=Label(frame2,text="Company Name="+compname,font=('Helvetica bold', 13), fg="Black",bg="pink")
    Lab.pack()
    Lab2=Label(frame2,text="Job Title="+jobtitle,font=('Helvetica bold', 13), fg="Black",bg="pink")
    Lab2.pack()
    Lab3=Label(frame2,text="Qualifications="+qualification,font=('Helvetica bold', 13), fg="Black",bg="pink")
    Lab3.pack()
    Lab4=Label(frame2,text="Job Description="+description,font=('Helvetica bold', 13), fg="Black",bg="pink")
    Lab4.pack()
    Lab5=Label(frame2,text="Experience="+experience,font=('Helvetica bold', 13), fg="Black",bg="pink")
    Lab5.pack()
    Lab6=Label(frame2,text="Last Date to Apply="+lastDate,font=('Helvetica bold', 13), fg="Black",bg="pink")
    Lab6.pack()
    link = Label(frame2, text="To Know More,click here",font=('Helvetica bold', 13), fg="blue", cursor="hand2",bg="pink")
    link.pack()
    link.bind("<Button-1>", lambda e:callback(url))


    
    
    
job=StringVar()
city=StringVar() 


 
img = ImageTk.PhotoImage(Image.open("freshersword.png"))  
label1=Label(frame,image=img,width=990,height=160,borderwidth=10)
label1.pack()
L1 = Label(frame, text="Enter Job/Skill",font=('Helvetica bold', 13),borderwidth=8)
L1.pack()
E1 = Entry(frame, bd=5,textvariable=job,borderwidth=8)
E1.pack()
L2 = Label(frame, text="Enter City",font=('Helvetica bold', 13),borderwidth=8)
L2.pack()
E2 = Entry(frame, bd=5,textvariable=city,borderwidth=8)
E2.pack()
b1=Button(frame,text="search",command=click,borderwidth=8)
b1.pack()

jobscrapper.mainloop()