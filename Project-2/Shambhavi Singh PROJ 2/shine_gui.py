import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup 
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
root=Tk()
root.geometry('700x700')
root.title('Shine Job Scraping')

img = ImageTk.PhotoImage(Image.open("shine.png"))
img_label=Label(image=img,padx=150 , pady=20)
img_label.pack()

# global job_var
# global loc_var
job_var=StringVar()
loc_var=StringVar()
name_label=Label(root,text='Enter Job/Position Preferred-->',font=('sans serif','15','bold'))
name_label.pack()
E1=Entry(root, textvariable=job_var,bg="grey" ,fg="white" ,font = ('calibre',10))
job_label=Label(root,text='Enter City/State Preferred-->',font=('sans serif','15','bold'))

E2=Entry(root,textvariable=loc_var,bg="grey" ,fg="white",font = ('calibre',10))

E1.pack()
job_label.pack()
# E1.insert(0,"Enter your JOB:")


E2.pack()
# E2.insert(0,"Enter your Location:")





def click1():
    job=job_var.get()
    loc=loc_var.get()
    def get_url(position , location): #generate a url  from  loc n pos
       template='https://www.shine.com/job-search/{}-jobs-in-{}'
       url = template.format(position,location)
       return url


    url = get_url(job , loc)
    label=Label(root,text="SHINE MULTIPLE JOB SEARCH IS DISPLAYED IN TERMINAL :",bg='white',fg='navy')
    label.pack()

    #Extract the raw html
    response=requests.get(url)
    soup = BeautifulSoup(response.text ,'html.parser')
    soup2=soup.find('div','SearchResult__jobs').text.strip()
    # soup3=soup.find('h1','ml-5').text.strip()
    s=soup2.replace("     ","")
    s1=s.replace("\n","")
    print(s1)
    print('--------')
    # s4=soup3.lstrip()
    # print(s4)
    cards=soup.find_all('li','result-display__profile flex-row mt-5 mb-5 animateElement cls_fade')
    # print(len(cards)


    for items in cards:
#   i=1
      print("SCRAPED RESULT :-" )
      job_title=soup.find('a','job_title_anchor').text.strip()
      print("Job Title:-->" + job_title)
      card=soup.h2.a
      job_url=card.get('href')
      job_url='https://www.shine.com' + job_url
      print("Job Url:-->"+job_url)
      company_name=soup.find('span','result-display__profile__company-name').text.strip()
      print("Company Name:-->"+ company_name)
      # requirement=soup.find('li','result-display__profile__years').text.strip()
      # print(requirement)
      job_location= soup.find('ul', 'd-flex flex-row mt-10').text.strip()
      job=job_location.replace("  ","")
      print("Job Location:-->"+ job)
      job_date= soup.find('ul', 'd-flex flex-row align-items-center mt-10').text.strip()
      print("Job Posted date:-->"+job_date)
      today= datetime.today().strftime('%Y-%m-%d')
      print ('current status:--->' + today)
      print('----')
      print('-->>-->>-->>-->>-->>->>-->>-->>-->>-->>-->>-->>-->>-->>')
    #   i+=1
      job_var.set(" ") 
      loc_var.set(" ")
def callback(url):
  webbrowser.open_new_tab(url)
def click():
    job=job_var.get()
    loc=loc_var.get()
    def get_url(position , location): #generate a url  from  loc n pos
       template='https://www.shine.com/job-search/{}-jobs-in-{}'
       url = template.format(position,location)
       return url


    url = get_url(job , loc)

    #Extract the raw html
    response=requests.get(url)
    soup = BeautifulSoup(response.text ,'html.parser')
    soup2=soup.find('div','SearchResult__jobs').text.strip()
    s=soup2.replace("     ","")
    s1=s.replace("\n","")
    des=Label(root,text='Search Display:'+s1,fg='dark goldenrod')
    des.pack()
    cards=soup.find_all('li','result-display__profile flex-row mt-5 mb-5 animateElement cls_fade')
    # print(len(cards)
    
    job_title=soup.find('a','job_title_anchor').text.strip()
    job1=Label(root,text='job title:--->'+job_title)
    job1.pack()
    card=cards[0]
    card=soup.h2.a
    job_url=card.get('href')
    job_url='https://www.shine.com' + job_url
    company_name=soup.find('span','result-display__profile__company-name').text.strip()
    job4=Label(root,text='Company Name :--->'+company_name)
    job4.pack()
    job_location= soup.find('ul', 'd-flex flex-row mt-10').text.strip()
    job=job_location.replace(" ","")
    job5=Label(root,text='job location:--->'+job_location)
    job5.pack()
    
    job_date= soup.find('ul', 'd-flex flex-row align-items-center mt-10').text.strip()
   
    job6=Label(root,text='job posted date:--->'+job_date)
      
    today= datetime.today().strftime('%Y-%m-%d')
    
    job7=Label(root,text='Current Status:--->'+today)
    job7.pack()
    job6.pack()
    #   i+=1
    job_var.set(" ") 
    loc_var.set(" ")
    url=Label(root,text='Wanna know More? Click Here to view Job Website',fg="blue", cursor='hand2')
    url.pack()
    url.bind("<Button-1>",lambda e : callback(job_url))

myButton=Button(root,text="Let's Scrape",padx=30, command=click)
# myButton.grid(row =0,column=1,justify=center)
myButton.pack(side=TOP,pady=10)

button=Button(root,text="Scrape More results for Terminal display",command=click1)
button.pack(side=TOP,pady=10)

button_quit=Button(root,text="Have a Happy Scraping! Exit",command=root.quit)
button_quit.pack(sid=BOTTOM,pady=3,padx=0)

root.mainloop()