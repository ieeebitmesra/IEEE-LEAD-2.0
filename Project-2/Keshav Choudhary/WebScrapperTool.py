import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

root = tk.Tk()
root.grid_columnconfigure((0,1), weight=1)
root.configure(background="#10D5E2")
root.state('zoomed')
root.title("WEB SCRAPPER TOOL")
root.configure(borderwidth="10",relief="sunken",background="#3B3F3F",cursor="arrow")
root.resizable(False,False)

Label1 = tk.Label(root)
_img1 = PhotoImage(file="r.png")
Label1.configure(image=_img1,background="#3B3F3F")
Label1.configure(text='''Label''')
Label1.grid(row=12,column=2,padx=250,pady=10)


label_pro=tk.Label(root,text="Job Name  : ",width=20,bg="#3B3F3F",fg="white",padx=10,font=("Comic Sans Ms",18),relief="flat")
label_pro.grid(row=7,column=0,pady=15)

label_pro=tk.Label(root,text=" Location : ",width=20,bg="#3B3F3F",fg="white",padx=10,font=("Comic Sans Ms",18),relief="flat")
label_pro.grid(row=8,column=0,pady=15)


def myclass():
  show(ttext.get(),ttext1.get())
    
ttext= tk.Entry(root,width=40,bg="black",fg="white",font=("Comic Sans Ms",18),relief="sunken")
ttext.grid(row=7,column=2,columnspan=1,pady=15)
ttext1= tk.Entry(root,width=40,bg="black",fg="white",font=("Comic Sans Ms",18),relief="sunken")
ttext1.grid(row=8,column=2,columnspan=1,pady=15)

button_find=tk.Button(root,text=" Click to scrape the website",bg="black",fg="white",width=30,pady=5,font=("Comic Sans Ms",18),command=myclass,relief="raised",padx=50)
button_find.grid(row=9,column=2,columnspan=1) 



def show(ttext,ttext1):
    ttext= ttext.replace(" ", "+")
    url = "https://in.indeed.com/jobs?q="+ttext+"&l="+ttext1
    res = requests.get(url)
    html_text = res.content
    # print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    job_card = soup.find('div', class_='jobsearch-SerpJobCard')
    job_title = job_card.h2.a
    job_location = job_card.find('span', class_='location accessible-contrast-color-location').get_text()
    job_company = job_card.find('span', class_='company')
    job_link = 'https://www.indeed.com' + job_card.h2.a.get('href')
    job_summary = job_card.find('div', class_='summary')
    post_date = job_card.find('span', class_='date date-a11y')

    url_S = (
        f"https://www.simplyhired.com/search?q={ttext}&l={ttext1}&job=lm9EtweZZunferjmfD34bFPIQjau4qk6XambAV4UDZhgAnbf10piJg")
    r = requests.get(url_S)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    job1 = soup.find('div', class_='SerpJob-jobCard card')
    job1_title = job1.h3.a
    job1_cname = job1.find('span', class_="JobPosting-labelWithIcon jobposting-company")
    job1_loc = job1.find('span', class_="jobposting-location")
    job1_summary = job1.find('p', class_="jobposting-snippet")


    a=job_title.get_text()
    b=job_company.get_text()
    c=job_location
    d=job_summary.get_text()
    e=post_date.get_text()
    f=job1_title.get_text()
    g=job1_cname.get_text()
    h=job1_loc.get_text()
    i=job1_summary.get_text()
    j="post date not mentioned"

    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(6):
                for j in range(3):
                    self.e = Entry(root, width=20, fg='black',
                                   font=('Comic Sans Ms', 16))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])


    lst = [('WEBSITE NAMES','INDEED','SIMPLY HIRED'),
           ('JOB TYPE :',a,f),
           ("JOB COMPANY ",b,g),
           ("JOB LOCATION",c,h),
           ('JOB SUMMARY',d,i),
           ('POST DATE',e,j)]
    t=Table(root)


root.mainloop()