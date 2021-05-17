import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup 
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
root=Tk()
root.geometry('700x700')
root.title('Indeed Job Scraping')

img = ImageTk.PhotoImage(Image.open("ind.png"))
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

#   print(job)
#   print(loc)
  

   def get_url(position , location): #generate a url  from  loc n pos
        template='https://in.indeed.com/jobs?q={}&l={}'
        url = template.format(position,location)
        return url
  
   url = get_url(job, loc)


  #Extract the raw html
   response=requests.get(url)
   soup = BeautifulSoup(response.text ,'html.parser')
   cards = soup.find_all('div' ,'jobsearch-SerpJobCard')
  # cards= len(cards)
  # print (sham)

  #prototype the first modal  
   # card=cards[0]
   for card in cards:
      print("SCRAPED RESULT :-\n")   
      atag = card.h2.a 
      job_title= atag.get('title')
      print('job title:--->' + job_title)
      print('------------')
   # title=Label(root,text="job title--->"+job_title)
   # title.pack()

      job_url = 'https://www.indeed.com' + atag.get('href')
      print ('job url:--->' + job_url)
      print('------------')
      company= card.find('span', 'company').text.strip()
      print('company:--->' + company)
      print('------------')
      job_location = card.find('div','recJobLoc').get('data-rc-loc')
      print('job location:--->'+ job_location)
      print('------------')
      # job=Label(root,text=job_location)
       # job.pack()
      job_summary= card.find('div', 'summary').text.strip()
      print('job summary:--->' + job_summary)
      print('------------')
      post_date =card.find('span' , 'date date-a11y').text
      print('Post_date:--->' + post_date)

      today= datetime.today().strftime('%Y-%m-%d')
      print ('current status:--->' + today)
      print('------------')
      try:
         job_salary= card.find('span','salaryText').text.strip()
      except AttributeError : 
         job_salary = ' '

      print ('job salary:-->' + job_salary)
      print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->>->->->->->->->->->->->->->->")
      
   job_var.set(" ") 
   loc_var.set(" ")

def callback(url):
   webbrowser.open_new_tab(url)


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
   title=Label(root,text="job title--->"+job_title)
   title.pack()

   
   jobu ='https://www.indeed.com'+ atag.get('href')
   
   
   company= card.find('span', 'company').text.strip()
   job_location = card.find('div','recJobLoc').get('data-rc-loc')
   job=Label(root,text='job location:--->'+job_location)
   job.pack()
   job_summary= card.find('div', 'summary').text.strip()
   job_summary=job_summary.replace("\n"," ")
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

   
   job_var.set(" ")   
   loc_var.set(" ")
   url=Label(root,text='Wanna know More? Click Here to view Job Website',fg="navy",font=('calibre',15), cursor='hand2')
   url.pack()
   url.bind("<Button-1>",lambda e : callback(jobu))
   


myButton=Button(root,text="Let's Scrape 1 st result of the search",padx=50, command=click)
# myButton.grid(row =0,column=1,justify=center)
myButton.pack(side=TOP,pady=40)

button=Button(root,text="scrape more results for terminal display",command=click1)
button.pack(side=TOP,pady=40)

# button_quit=Button(root,text="Have a Happy Scraping! Exit",command=root.quit)
# button_quit.pack()


root.mainloop()