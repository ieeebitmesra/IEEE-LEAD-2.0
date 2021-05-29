import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
from PIL import ImageTk, Image


root = Tk()
root.geometry("1200x600")
root.configure(background="white")
root.resizable(FALSE,FALSE)
root.title("   Google Search")
root.wm_iconbitmap("google_icon.ico")

global keyword


def click(event):
    keyword=screen.get()
    res = requests.get("https://www.google.com/search?q="+str(keyword))
    soup=BeautifulSoup(res.text,"html.parser")
    link_elements=soup.select('.kCrYT a')
    link_length=min(1,len(link_elements))
    for i in range(link_length):
       link=link_elements[i].get('href')
    text = event.widget.cget("text")
    if text == "Search":
         webbrowser.open('https://google.com/'+link)


image = Image.open("google.jpg")
photo = ImageTk.PhotoImage(image)
lab1= Label(image= photo)
lab1.pack()

keyword=StringVar()
keyword.set(" ")
screen = Entry(root, textvar=keyword, font="Angsana 30 " )
screen.configure( background="white smoke")
screen.pack(fill=X, ipadx=8, padx=100, pady=5)



f = Frame(root, bg="light gray")
b = Button(f,text="Search",font="Helvetica 25 ", padx=27,pady=5)
b.pack(side= LEFT, padx=2, pady=2)
b.bind("<Button-1>",click)
b.configure( background="silver")
f.pack()

root.mainloop()