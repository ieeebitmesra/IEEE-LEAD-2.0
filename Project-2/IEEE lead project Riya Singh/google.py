import csv
from datetime import datetime
import requests
import random
from bs4 import BeautifulSoup 
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
import re
root=Tk()
root.geometry('500x500')
root.config(bg="alice blue")
root.title('Google Search')
img = ImageTk.PhotoImage(Image.open("google.png"))
img_label=Label(image=img)
img_label.pack()

name_var=StringVar()
def callback(url):
    webbrowser.open_new(url)
def open():
 

    name=name_var.get()
    url = 'https://google.com/search?q=' + name
    A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93  Safari/537.36",
       )
 
    Agent = A[random.randrange(len(A))]
 
    headers = {'user-agent': Agent}
    r = requests.get(url, headers=headers)

 
    soup = BeautifulSoup(r.text, 'lxml')
    
    i=0
    list= soup.find_all
    for link in list('a', attrs={'href': re.compile("^https://")}):
         i=i+1
         if(i==5):
          variable=link.get('href')
          break 
    name_var.set("")
    link1 = Label(root, text="Click here to view google first search result", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback(variable))

E1=Entry(root,textvariable=name_var, bg="white" ,fg="black" ,font = ('calibre',10))
E1.pack()
myButton=Button(root,text="SEARCH",padx=50, command=open)
myButton.pack()



button_quit=Button(root,text="EXIT",command=root.quit)
button_quit.pack()



root.mainloop()