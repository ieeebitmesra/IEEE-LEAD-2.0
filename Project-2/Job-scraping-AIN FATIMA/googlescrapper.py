from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image  
import webbrowser
import re
jobscrapper=Tk()
search=StringVar()


frame = LabelFrame(jobscrapper,fg="white", padx=10, pady=10,borderwidth=8 )
frame.pack()
img = ImageTk.PhotoImage(Image.open("google.png"))  
label1=Label(frame,image=img,width=990,height=160)
label1.pack()


def click():
            
        global user_input
        user_input=E1.get()
        google_search=requests.get("https://www.google.com/search?q="+user_input)
        soup=BeautifulSoup(google_search.text,'html.parser')
        search_results=soup.select('.kCrYT a')
        global actual_link
        for link in search_results[0:1]:
           actual_link=link.get('href')
        label2=Label(frame,text="To view the first google search result for your entry ",font=("Goudy old",15,"bold"),bg="blue",fg="white",borderwidth=8)
        label2.pack()
        button2=Button(frame,text="Click here",bg="deeppink",command=lambda:Click2(actual_link),font=10,borderwidth=8)
        button2.pack()
def Click2(self):
        webbrowser.open('https://google.com/'+self)
        
E1 = Entry(frame, bd=5,textvariable=search,font=10,borderwidth=8)
E1.pack()
b1=Button(frame,text="Search",command=click,font=10,borderwidth=8)
b1.pack()

jobscrapper.mainloop()