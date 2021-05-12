import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup 
import os
import random
from tkinter import *
import webbrowser
from PIL import ImageTk,Image
root=Tk()
root.geometry('500x400')
root.title('LinkedIn Job Scraping')
# root.config(bg='light cyan')
img = ImageTk.PhotoImage(Image.open("linkedin.png"))
img_label=Label(image=img)
img_label.pack()
job_var=StringVar()
loc_var=StringVar()

def callback(url):
    webbrowser.open_new(url)

def Extract():
  job=job_var.get()
  loc=loc_var.get()
  def get_url(position , location): #generate a url  from  loc n pos
      template='https://in.linkedin.com/jobs/search?keywords={}&location={}'
      url = template.format(position,location)
      return url

  # pos = input("Enter the Position/Job preferred: ")
  # loc = input("Enter the Location preferred: ")
  # url = get_url('Senior accountant' , 'Chennai')
  url = get_url(job , loc)

  #Extract the raw html
  response=requests.get(url)
  soup = BeautifulSoup(response.text ,'html.parser')
  total_job_found=soup.find('h1' ,'results-context-header__context').text.strip()
  
  total=Label(root,text="Total Job Extracted of The Specified Domain--->"+total_job_found)
  total.pack()


  cards = soup.find_all('ul' , 'jobs-search__results-list')
# total =soup.find_all('div' ,'result-context-header')


  card= cards[0] 
  job_title= card.find('span' , 'screen-reader-text').text.strip()
  title=Label(root,text="Job Title--->"+job_title)
  title.pack()



#image scrapping of the main website of linkedin which only provides link

def imagedown(url):
     r =requests.get(url)
     soup = BeautifulSoup(r.text ,'html.parser')
# print(soup.title.text)
     images =soup.find_all('img')
# print(images)
     links = []
     for image in images:
        name= image['alt']
        link=image['data-delayed-url']
        links.append(link)
     return links

     
        # print(name,link)

def scrape():
   img=Label(root,text= 'Images Link For Linkedin website',fg='black',font=('Helvetica 15 underline'))
   link=imagedown('https://www.linkedin.com/')
   img.pack()
   li1=link[0]
   link1 = Label(root, text="Scraped link for the First Image", fg="midnight blue", cursor="hand2")
   link1.pack()
   link1.bind("<Button-1>", lambda e: callback(li1))
   li2=link[1]
   link2 = Label(root, text="Scraped link for the Second Image", fg="midnight blue", cursor="hand2")
   link2.pack()
   link2.bind("<Button-1>", lambda e: callback(li2))
   li3=link[2]
   link3 = Label(root, text="Scraped link for the Third Image", fg="midnight blue", cursor="hand2")
   link3.pack()
   link3.bind("<Button-1>", lambda e: callback(li3))
   li4=link[3]
   link4 = Label(root, text="Scraped link for the Fourth Image", fg="midnight blue", cursor="hand2")
   link4.pack()
   link4.bind("<Button-1>", lambda e: callback(li4))
   li5=link[4]
   link5 = Label(root, text="Scraped link for the Fifth Image", fg="midnight blue", cursor="hand2")
   link5.pack()
   link5.bind("<Button-1>", lambda e: callback(li5))
   li6=link[5]
   link6= Label(root, text="Scraped link for the Sixth Image", fg="midnight blue", cursor="hand2")
   link6.pack()
   link6.bind("<Button-1>", lambda e: callback(li6))

def imagedowns(url,folder): 
    r =requests.get(url)
    soup = BeautifulSoup(r.text ,'html.parser')
     # print(soup.title.text)
    images =soup.find_all('img')
    links = []
    for image in images:
          name= image['alt']
          link=image['data-delayed-url']
          links.append(link)     
    os.mkdir('LinkedIn_jpg')
    i=0
    for index , img_link in enumerate(links):
        if(i<=15):
            img_data=requests.get(img_link).content
            with open ("LinkedIn_jpg/"+str(index+1)+ '.jpg' , 'wb+') as f:
              f.write(img_data)  
            i+= 1
        else:
            f.close()
            break

def folder():
     print('The images in jpg format created in the folder named LinkedIn_jpg :)')
     print("--------------")
     imagedowns('https://www.linkedin.com/' , 'Image')
     FOL=Label(root,text= 'Images  Folder  Named: LinkedIn_jpg Has been Created! CHECK ',bg='slate gray' ,fg='navy',font=('Helvetica 15 underline'))
     FOL.pack()
name_label=Label(root,text='Enter Job/Position Preferred-->',font=('sans serif','15','bold'))
name_label.pack()
E1=Entry(root, textvariable=job_var,bg="grey" ,fg="white" ,font = ('calibre',10))
job_label=Label(root,text='Enter City/State Preferred-->',font=('sans serif','15','bold'))
E1=Entry(root,textvariable=job_var, bg="grey" ,fg="white" ,font = ('calibre',10))
E1.pack()
# E1.insert(0,"Enter Job:")
job_label.pack()
E2=Entry(root,textvariable=loc_var, bg="grey" ,fg="white" ,font = ('calibre',10))
E2.pack()
# E2.insert(0,"Enter Location:")
# myButton2=Button(root,text="Submit",padx=50, command=plz)
# myButton2.pack(side=TOP,pady=30)

myButton1=Button(root,text="Let's Scrape LinkedIn",padx=50, command=Extract)
myButton1.pack(side=TOP,pady=10)

myButton=Button(root,text="Let's Scrape Images link of Linkedin",padx=50, command=scrape)
myButton.pack(side=TOP,pady=20)

myButton=Button(root,text=" Scraped Images in jpg format in folder",padx=50, command=folder)
myButton.pack(side=TOP,pady=20)



button_quit=Button(root,text="Exit",padx=20,command=root.quit)
button_quit.pack(side=TOP,pady=10)



root.mainloop()