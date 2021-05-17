import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.grid_columnconfigure((0,1), weight=1)
root.configure(background="#FCECDD")
root.geometry("1400x1200")
root.title("WEB SCRAPPER")
root.resizable(True,True)

label_pro=tk.Label(root,text="Job Name",width=20,bg="#FEA82F",fg="white",padx=10,font=("Times",25),relief="flat",pady=5)
label_pro.grid(row=7,column=0)

label_pro=tk.Label(root,text="Location",width=20,bg="#FEA82F",fg="white",padx=10,font=("Times",25),relief="flat",pady=5)
label_pro.grid(row=8,column=0)

def myclass():
  show(t2.get(),t3.get())
    
t2= tk.Entry(root,width=40,bg="#FFC288",fg="black",font=("Times",25),relief="sunken")
t2.grid(row=7,column=2,columnspan=1)    
t3= tk.Entry(root,width=40,bg="#FFC288",fg="black",font=("Times",25),relief="sunken")
t3.grid(row=8,column=2,columnspan=1)

button_find=tk.Button(root,text="Click Here",bg="#FF8303",fg="white",width=12,pady=5,font=("lob ",18),command=myclass,padx=50)
button_find.grid(row=9,column=2,columnspan=1,pady=20) 

def show(jobenter,jobenter1):
    url_S = (f"https://www.simplyhired.com/search?q={jobenter}&l={jobenter1}&job=lm9EtweZZunferjmfD34bFPIQjau4qk6XambAV4UDZhgAnbf10piJg")
    r = requests.get(url_S)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    job = soup.find('div', class_='SerpJob-jobCard card')
    job_title = job.h3.a
    job_company = job.find('span', class_="JobPosting-labelWithIcon jobposting-company")
    job_location = job.find('span', class_="jobposting-location")
    job_summary = job.find('p', class_="jobposting-snippet")

    url = (f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={jobenter}&txtLocation={jobenter1}")
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    divs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    card = divs[0]
    atitle = card.a
    company = card.find('h3', class_="joblist-comp-name")
    summary= card.find('ul', class_='list-job-dtl clearfix')

    simplylist = [job_title.get_text(),job_location.get_text(),job_company.get_text(),job_summary.get_text()]
    timeslist=[atitle.get_text().strip(),company.get_text().strip(),summary.get_text().strip()]
    output=Label(root,text="SIMPLYHIRED ",font=('Helvetica', 15), fg="Black",bg="#FEA82F")
    output.grid(row=11,column=0,columnspan=1,pady=20)
    output=Label(root,text="Job Title: "+simplylist[0],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=310)
    output.grid(row=13,column=0,columnspan=1)
    output=Label(root,text="Job Location: "+simplylist[1],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=310)
    output.grid(row=14,column=0,columnspan=1)
    output=Label(root,text="Company Name: "+simplylist[2],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=310)
    output.grid(row=15,column=0,columnspan=1)
    output=Label(root,text="Job Summary: "+simplylist[3],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=250,padx=30,pady=30)
    output.grid(row=16,column=0,columnspan=1)
    
    output=Label(root,text="TIMESJOBS",font=('Helvetica', 15), fg="Black",bg="#FEA82F")
    output.grid(row=11,column=1,columnspan=2,pady=20)

    output=Label(root,text="Job Title: "+timeslist[0],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=500)
    output.grid(row=13,column=1,columnspan=2)
    output=Label(root,text="Company Name: "+timeslist[1],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=500)
    output.grid(row=14,column=1,columnspan=2)
    output=Label(root,text="Job Summary: "+timeslist[2],font=('Times', 12), fg="Black",bg="#FEA82F",wraplength=500)
    output.grid(row=16,column=1,columnspan=2)
  

root.mainloop()