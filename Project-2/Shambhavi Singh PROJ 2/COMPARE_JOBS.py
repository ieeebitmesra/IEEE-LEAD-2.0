import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup 
from tkinter import *
from PIL import ImageTk,Image
import webbrowser

root=Tk()
root.geometry('700x700')
root.title(' LETS COMPARE')

img = ImageTk.PhotoImage(Image.open("comp.png"))
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
E2.pack()

def callback(jo):
  webbrowser.open_new_tab(jo)
def click():
   job=job_var.get()
   loc=loc_var.get()

   def get_url(position , location): #generate a url  from  loc n pos
        template='https://in.indeed.com/jobs?q={}&l={}'
        url = template.format(position,location)
        return url
  
   url = get_url(job, loc)


  #Extract the raw html
   response=requests.get(url)
   soup = BeautifulSoup(response.text ,'html.parser')
   cards = soup.find_all('div' ,'jobsearch-SerpJobCard') 
   card=cards[0] 
   atag = card.h2.a 
   job_title= atag.get('title')
   labelI=Label(root,text="INDEED RESULTS FOR COMPARISON:",fg='Indian red', font=('calibre 15 underline'))
   labelI.pack()
   title=Label(root,text="job title--->"+job_title)
   title.pack()

   job_url = 'https://www.indeed.com' + atag.get('href')
   
   company= card.find('span', 'company').text.strip()
   job_location = card.find('div','recJobLoc').get('data-rc-loc')
   job=Label(root,text='job location:--->'+job_location)
   job.pack()
   job_summary= card.find('div', 'summary').text.strip()
   job_summary=job_summary.replace('\n'," ")
   job_sum=Label(root,text='job summary:--->'+ job_summary)
   job_sum.pack()
   post_date =card.find('span' , 'date date-a11y').text
   date=Label(root,text='job posted date:--->'+post_date)
   today= datetime.today().strftime('%Y-%m-%d')
   status=Label(root,text='current status:--->'+today)
   status.pack()
   date.pack()
   try:
       job_salary= card.find('span','salaryText').text.strip()
   except AttributeError : 
       job_salary = ' '
   salary=Label(root,text='job Salary:--->'+job_salary)
   salary.pack()
   url=Label(root,text='Wanna know More? Click Here to view Job Website',fg="navy", cursor='hand2')
   url.pack()
   url.bind("<Button-1>",lambda e : callback(job_url))

   job1=job_var.get()
   loc1=loc_var.get()

   def get_url1(position1 , location1): #generate a url  from  loc n pos
      template='https://www.shine.com/job-search/{}-jobs-in-{}'
      url1 = template.format(position1,location1)
      return url1


   url1= get_url1(job1 , loc1)

   #Extract the raw html
   response1=requests.get(url1)
   soup1 = BeautifulSoup(response1.text ,'html.parser')
   # soup2=soup.find('div','SearchResult__jobs').text.strip()
   cards1=soup1.find_all('li','result-display__profile flex-row mt-5 mb-5 animateElement cls_fade')
   # print(len(cards)
   card1=cards1[0]
   # for items in cards:
   i=1
   
   label=Label(root,text="SHINE RESULTS FOR COMPARISON:",fg='Indian red', font=('calibre 15 underline'))
   label.pack()
   job_title=soup1.find('a','job_title_anchor').text.strip()
   job1=Label(root,text='job title:--->'+job_title)
   job1.pack()
   
   card1=soup1.h2.a
   job_url1=card1.get('href')
   job_url1='https://www.shine.com' + job_url1
    

   
   company_name=soup1.find('span','result-display__profile__company-name').text.strip()
   job4=Label(root,text='Company :--->'+company_name)
   job4.pack()
   job_location= soup1.find('ul', 'd-flex flex-row mt-10').text.strip()
   job=job_location.replace("\n"," ")
   job5=Label(root,text='job location:--->'+job_location)
   job5.pack()
   job_date= soup1.find('ul', 'd-flex flex-row align-items-center mt-10').text.strip()
   job6=Label(root,text='job posted date:--->'+job_date)
      
   today= datetime.today().strftime('%Y-%m-%d')
   job7=Label(root,text='Current Status:--->'+today)
   job7.pack()
   job6.pack()

   
   job_var.set(" ")   
   loc_var.set(" ")
   url1=Label(root,text='Wanna know More? Click Here to view Job Website',fg="navy", cursor='hand2')
   url1.pack()
   url1.bind("<Button-1>",lambda e : callback(job_url1))



myButton=Button(root,text="Let's Scrape & Compare ",padx=20, command=click)
myButton.pack(side=TOP,pady=10)
 




root.mainloop()