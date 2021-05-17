#This program scrapes the google search page of the keyword entered by the user. The #information scraped are :-
#First Heading of the google search page
#First Description of the google search page
#First URL of the google search page

#The GUI is the structural part of the program.The google logo is embedded 
# at the top of the GUI to give it a famiiar look .It :-
#Takes input
#Prints the information scraped
#Creates a button which when clicked, directs to the first URL   

#Tech Stack Used:
#Language - Python 3.9.4
#Modules - Tkinter , requests , Beautiful Soup and WebBrowser 

from tkinter import *
import tkinter as tk
from tkinter import *
import tkinter as tki
import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import Tk, Label
from PIL import Image, ImageTk
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#keyword globally declared to be enable calling it within various functions.
kw='global declaration'

#takes the keyword as paramenter and return the heading , description 
# and url of corresonding page 
def scraped(entry):

    url='https://www.google.com/search?q='+entry
    url = url.replace(' ',"+")

    html_text=requests.get(url , headers= headers )

    soup = BeautifulSoup(html_text.text , "html.parser")

#   class containing the heading
    head_class=soup.find('div',class_='BNeawe vvjwJb AP7Wnd')
    
    if head_class is None:
        heading = 'Not Found'
#if no such class is found , store the string 'Not Found' 
        
    else:
        heading = head_class.text    
    
#   class containing the description
    x=soup.find('div', class_='BNeawe s3v9rd AP7Wnd') 
    
    if x is None:
        description = '''No Such terms found.
Suggestions:
Make sure that all words are spelled correctly.
Try different keywords.
Try more general keywords.        
        '''
#if no such class is found , store the string 
    
    else:    
        description = x.text
    

    link = 'Your search did not match any documents.'
#this is the default value stored , if a link is found 
# , the link will automatically over-write this string
    
    #Class containing the link
    x=soup.find_all( 'div',class_='kCrYT')
    for y in x:
        if(y.a ):
            link = y.a['href']
            break
    
    return [heading , description , link] ;


#This function:
#1->takes the information from scraped() function
#2->Creates a Frame named bottomframe
#3->Manipulates the information to get a format-string named Fact
#4->Puts the string Fact in the bottomframe
#5->Creates a button for directing the user to the link
def myClick():
    kw=entry.get()

    bottomframe = Frame(root)
        
    answer = Text(bottomframe,height=15)
    answer.pack()

    bottomframe.pack()
 
    Fact = '''
Heading :
{0}

Description :
{1}

Link :
{2}

    '''.format(scraped(kw)[0],scraped(kw)[1],scraped(kw)[2]).strip()

    
    answer.insert(tk.END, Fact)
    
    def cmd():
        webbrowser.open('https://google.com/'+scraped(kw)[2])

#The if-else statement here ensures that if a link is not found,
#The 'Visit Link' Button automatically gets DISABLED
    if scraped(kw)[2] != 'Your search did not match any documents.':
        linkButton = Button(bottomframe,text='Visit Link',command=cmd)
        linkButton.pack()
    
    else:
        linkButton = Button(bottomframe,text='Visit Link',command=cmd,state=DISABLED )
        linkButton.pack()

 
#Main Root containing the Google Logo and a search bar 

root = Tk()
root.geometry("800x500")
my_img1 = ImageTk.PhotoImage(Image.open("google-logo-web2.jpg"))
my_label = Label(image=my_img1)
my_label.pack()
topframe = Frame (root)
entry = Entry(topframe,width=80)
entry.pack(ipady=3)

button = Button(topframe,text='search',command=myClick)
button.pack()

labelSpace0=Label(topframe, text=' ')
labelSpace0.pack() 


topframe.pack(side= TOP)

root.mainloop()
