import csv
from datetime import datetime
import requests
import random
from bs4 import BeautifulSoup 
from tkinter import *
import webbrowser
from PIL import ImageTk,Image
root=Tk()
root.geometry('500x500')
root.title('google Job Scraping')
root.config(bg='white')

# img=Image.open('google.png')
# img=img.resize((450,350),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(img)

# img_label=Label(image=img,padx=800 , pady=800)

# img_label.pack()
img = ImageTk.PhotoImage(Image.open("google.png"))
img_label=Label(image=img)
img_label.pack()

root.iconbitmap('./Users/ajaykumarsingh/Desktop/gui/indeed.ico')
name_var=StringVar()
def callback(url):
    webbrowser.open_new(url)
def open():
 

    name=name_var.get()
    # text = input("enter your query for search")
    url = 'https://google.com/search?q=' + name
    A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93  Safari/537.36",
       )
 
    Agent = A[random.randrange(len(A))]
 
    headers = {'user-agent': Agent}
    r = requests.get(url, headers=headers)

 
    soup = BeautifulSoup(r.text, 'lxml')
    # soup.prettify()
    #printing all the header text
    count=0
    for info in soup.find_all('h3'):
        header=info.text
        print("Headings of the top search")
        print(header)
        
        print("-------")

    #printing either the first or the second link of the searched query
    i=0
    list= soup.find_all
    for link in list('a', attrs={'href': re.compile("^https://")}):
    #  print(link.get('href'))
         i=i+1
         if(i==5):
        #    print('Required Url For The First Link')
        #    print(link.get('href'))
           links=link.get('href')
           break 

    # print("The link of the required gsearch : " )

    name_var.set("")
    link1 = Label(root, text="Click Here: To View Scraped link for the First Website of the Google Search ", fg="midnight blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback(links))

label_id=Label(root,text="Enter Query of your Search",fg='black')
label_id.pack()
E1=Entry(root,textvariable=name_var, bg="grey" ,fg="white" ,font = ('calibre',10))
E1.pack()
# E1.insert(0,"Enter keyword:")
myButton=Button(root,text="Let's Scrape",padx=50 ,command=open)
# myButton.grid(row =0,column=1)
myButton.pack(pady=20)



button_quit=Button(root,text="Exit",command=root.quit)
button_quit.pack()



root.mainloop()