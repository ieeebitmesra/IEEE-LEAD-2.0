import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.grid_columnconfigure((0,1), weight=1)
root.configure(background="#10D5E2")
root.geometry("800x600")
root.title("JOB COMPARATOR ")
root.configure(borderwidth="10",relief="sunken",background="#A58FAA",cursor="arrow")
root.resizable(False,False)

Label1 = tk.Label(root)
_img1 = PhotoImage(file="webscrapper.png")
Label1.configure(image=_img1)
Label1.configure(text='''Label''')
Label1.grid(row=1,column=0,pady=2)


label_pro=tk.Label(root,text="Job Name ",width=20,bg="#72147E",fg="white",padx=10,font=("Times",18),relief="raised",pady=10)
label_pro.grid(row=7,column=0)

label_pro=tk.Label(root,text=" Location ",width=20,bg="#72147E",fg="white",padx=10,font=("Times",18),relief="raised",pady=10)
label_pro.grid(row=8,column=0)


def myclass():
  show(job.get(),location.get())
    
job= tk.Entry(root,width=40,bg="#687980",fg="black",font=("Times",18),relief="sunken")
job.grid(row=7,column=2,columnspan=1)
location= tk.Entry(root,width=40,bg="#687980",fg="black",font=("Times",18),relief="sunken")
location.grid(row=8,column=2,columnspan=1)

button_find=tk.Button(root,text=" Compare ",bg="#464F41",fg="white",width=8,pady=5,font=("lob ",18),command=myclass,relief="raised",padx=50)
button_find.grid(row=9,column=2,columnspan=1)

def show(job,location):
    job= job.replace(" ", "+")
    url_indeed = "https://in.indeed.com/jobs?q="+job+"&l="+location
    r = requests.get(url_indeed)
    htmltext = r.content
    soup = BeautifulSoup(htmltext, 'html.parser')
    card = soup.find('div', class_='jobsearch-SerpJobCard')
    job_title = card.h2.a
    job_location = card.find('span', class_='location accessible-contrast-color-location')
    job_company = card.find('span', class_='company')
    link=card.h2.a.get('href')
    job_link = 'https://www.indeed.com' + link
    job_summary = card.find('div', class_='summary')
    post_date = card.find('span', class_='date date-a11y')
    try:
        job_salary = card.find('span', class_='salaryText').get_text()
    except AttributeError:
        job_salary = "NA"

    url_timesjob = (f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job}&txtLocation={location}")
    r = requests.get(url_timesjob)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    divs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    div = divs[0]
    title = div.a
    link_job=div.h2.a.get('href')
    job_linktimesjob='https://www.timesjobs.com/'+link_job
    comp = div.find('h3', class_="joblist-comp-name")
    descrip = div.find('ul', class_='list-job-dtl clearfix')
    location_job = div.find('ul', class_='top-jd-dtl clearfix')
    str1 = location_job.get_text()
    str2 = str(str1)
    str3 = str2.replace("card_travel", "Experience Required:  ")
    tempList = [job_link,job_title.get_text().strip(),job_company.get_text().strip(),job_summary.get_text().strip(),job_salary,job_location.get_text().strip(),post_date.get_text()]
    tempList1=[job_linktimesjob,title.get_text().strip(),comp.get_text().strip(),descrip.get_text().strip(),str3.strip()]
    indeed_list=["Job Link:  ","Job Title:  ","Company Name:  ","Job Summary:  ","Job Salary:  ","Job Location:  ","post date:  "]
    listBox.insert(END,"INDEED")
    listBox.insert(END, "\n")
    listBox.insert(END, "\n")
    for i in range(0,7):
        listBox.insert(END,indeed_list[i])
        listBox.insert(END,tempList[i])
        listBox.insert(END, "\n")

    listBox.insert(END, "\n")
    listBox.insert(END, "TIMES JOB")
    listBox.insert(END, "\n")
    listBox.insert(END, "\n")

    listBox.insert(END, "Job Link:  ")
    listBox.insert(END, tempList1[0])
    listBox.insert(END, "\n")
    listBox.insert(END, "Job Title:")
    listBox.insert(END, "\n")
    listBox.insert(END, tempList1[1])
    listBox.insert(END, "\n")
    listBox.insert(END,"Company Name:  ")
    listBox.insert(END, "\n")
    for i in range(2,5):
        listBox.insert(END, tempList1[i])
        listBox.insert(END, "\n")

listBox = Text(root,width=80,bg="#E1E5EA",relief="sunken",font=("Helvetica",10,"bold"))
listBox.grid(row=1, column=2,)
listBox.insert(END,"JOB COMPARATOR ( INDEED VS TIMESJOB )")
listBox.insert(END,"\n")
root.mainloop()