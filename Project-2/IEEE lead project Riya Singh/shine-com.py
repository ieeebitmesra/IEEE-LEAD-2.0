import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import *
from PIL import ImageTk,Image
import re
root=Tk()
root.geometry('700x700')
root.config(bg="light green")
root.title('site scrapped')
job=StringVar()
city=StringVar()
def click():
 url="https://www.shine.com/job-search/"+E1.get()+"-jobs-in-"+E2.get()
 html_text=requests.get(url)
 soup= BeautifulSoup(html_text.text,'lxml')
 soup.prettify()
 jobtitle=soup.find('a',class_="job_title_anchor").text
 lab=Label(root,text="job title="+jobtitle)
 lab.pack()
 companyname=soup.find('span',class_="result-display__profile__company-name").text.strip()
 lab1=Label(root,text="company name="+companyname)
 lab1.pack()
 experience=soup.find('li',class_="w-30 mr-10 result-display__profile__years").text.strip()
 lab2=Label(root,text="experience="+experience)
 lab2.pack()
img = ImageTk.PhotoImage(Image.open("shine.png"))
img_label=Label(image=img,padx=150 , pady=20)
img_label.pack()
L1 = Label(root, text="Enter Job/Skill",font=('Helvetica bold', 13),borderwidth=4)
L1.pack()
E1 = Entry(root, bd=5,textvariable=job,borderwidth=4)
E1.pack()
L2 = Label(root, text="Enter City",font=('Helvetica bold', 13),borderwidth=4)
L2.pack()
E2 = Entry(root, bd=5,textvariable=city)
E2.pack()
b1=Button(root,text="search",command=click,borderwidth=4)
b1.pack()
root.mainloop()