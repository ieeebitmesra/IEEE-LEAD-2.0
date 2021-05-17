from bs4 import BeautifulSoup
import requests
from tkinter import *
from PIL import ImageTk,Image  
import webbrowser
import re
from tkinter import messagebox



jobscrapper=Tk()

jobscrapper.config(background="lemon chiffon")
def popupmsg():
    
    
    
    response=messagebox.showerror("Warning", "Sorry! Invalid Search. Try Again!")

    
    popup_label =Label(text=response)
    popup_label.pack()



   

def click():
    frame2 = LabelFrame(jobscrapper, bg="peach puff",fg="peach puff",width=50, height=50,border=8)
    frame2.pack()
    
    
    url="https://www.freshersworld.com/jobs/jobsearch/"+E1.get()+"-jobs-in-"+E2.get()

    html_text=requests.get(url)
    soup = BeautifulSoup(html_text.text,'lxml')
    soup.prettify()
    try:
        compname=soup.find('h3',class_='latest-jobs-title font-16 margin-none inline-block').text
    except:
        popupmsg()
    
    compname=soup.find('h3',class_='latest-jobs-title font-16 margin-none inline-block').text
    job=soup.find('div',class_='col-md-12 col-xs-12 col-lg-12 padding-none left_move_up')
    jobtitle=job.find('div').text
    qualification=job.find('span',class_='bold_elig').text
    description=soup.find('span',class_='desc').text
    
    def callback(url):
        webbrowser.open_new_tab(url)
    
    
    label0=Label(frame2,text="JOBFRESHERS",font=('Helvetica bold', 15), fg="Red",bg="peach puff")
    label0.pack()
    Lab2=Label(frame2,text="Job Title="+jobtitle,font=('Helvetica bold', 10), fg="Black",bg="peach puff")
    Lab2.pack()
    Lab=Label(frame2,text="Company Name="+compname,font=('Helvetica bold', 10), fg="Black",bg="peach puff")
    Lab.pack()
    
    Lab3=Label(frame2,text="Skills/qualifications="+qualification,font=('Helvetica bold',10), fg="Black",bg="peach puff")
    Lab3.pack()
    Lab4=Label(frame2,text="Job Description="+description,font=('Helvetica bold', 10), fg="Black",bg="peach puff")
    Lab4.pack()
    
    link = Label(frame2, text="To Know More,click here",font=('Helvetica bold', 10), fg="blue", cursor="hand2",bg="peach puff")
    link.pack()
    link.bind("<Button-1>", lambda e:callback(url))
    frame3 = LabelFrame(jobscrapper, bg="papaya whip",fg="hot pink" ,width=50, height=50,border=8)
    frame3.pack()
    
    url2="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords="+E1.get()+"&txtLocation="+E2.get()

    html_text2=requests.get(url2)
    soup2 = BeautifulSoup(html_text2.text,'lxml')
    soup2.prettify()
    compname2=soup2.find('h3',class_='joblist-comp-name').text.strip()
    job2=soup2.find('ul',class_='list-job-dtl clearfix')
    
    skills2=job2.find('span',class_="srp-skills").text.strip()
    description2=job2.find('li').text.strip()
    
    label20=Label(frame3,text="TIMESJOB",font=('Helvetica bold', 15), fg="Red",bg="papaya whip")
    label20.pack()
    Lab22=Label(frame3,text="Job Title= "+E1.get(),font=('Helvetica bold', 10), fg="Black",bg="papaya whip")
    Lab22.pack()
    Lab2=Label(frame3,text="Company Name= "+compname2,font=('Helvetica bold', 10), fg="Black",bg="papaya whip")
    Lab2.pack()
    Lab52=Label(frame3,text="Skills/Qualifications= "+skills2,font=('Helvetica bold',10), fg="Black",bg="papaya whip")
    Lab52.pack()
    Lab42=Label(frame3,text=description2,font=('Helvetica bold', 10), fg="Black",bg="papaya whip")
    Lab42.pack()
    
    
    link2 = Label(frame3, text="To Know More,click here",font=('Helvetica bold',10), fg="blue", cursor="hand2",bg="papaya whip")
    link2.pack()
    link2.bind("<Button-1>", lambda e:callback(url2))
    




    
    
    
job=StringVar()
city=StringVar()



lab=Label(jobscrapper,text="WELCOME   TO   JOB   COMPARATOR  WINDOW",font=('Helvetica bold', 17),bg="light goldenrod")
lab.pack()

L1 = Label(jobscrapper, text="Enter Job/Skill",font=('Helvetica bold', 13))
L1.pack()
E1 = Entry(jobscrapper, bd=5,textvariable=job)
E1.pack()
L2 = Label(jobscrapper, text="Enter City",font=('Helvetica bold', 13))
L2.pack()
E2 = Entry(jobscrapper, bd=5,textvariable=city)
E2.pack()
b1=Button(jobscrapper,text="Search&Compare",command=click)
b1.pack()

jobscrapper.mainloop()
