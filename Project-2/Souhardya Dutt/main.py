import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.grid_columnconfigure((0, 1), weight=1)
root.configure(background="#10D5E2")
root.geometry("900x600")
root.title("JOB COMPARE ")
root.configure(borderwidth="10", relief="sunken", background="#282828")
root.resizable(True, True)

Label1 = tk.Label(root)
_img1 = PhotoImage(file="googleSearchImage.png")
Label1.configure(image=_img1)
Label1.configure(text='''Label''')
Label1.grid(row=1, column=0, pady=2)

label_job = tk.Label(root, text="Job Query  : ", width=20, bg="#282828", fg="aquamarine", padx=10, font=("Calibri", 18),
                     relief="raised", pady=10)
label_job.grid(row=7, column=0)

label_job = tk.Label(root, text=" Location : ", width=20, bg="#282828", fg="aquamarine", padx=10, font=("Calibri", 18),
                     relief="raised", pady=10)
label_job.grid(row=8, column=0)


def myClass():
    show(ttext.get(), ttext1.get())


ttext = tk.Entry(root, width=40, bg="aquamarine", fg="black", font=("Calibri", 18), relief="raised")
ttext.grid(row=7, column=2, columnspan=1)
ttext1 = tk.Entry(root, width=40, bg="aquamarine", fg="black", font=("Calibri", 18), relief="raised")
ttext1.grid(row=8, column=2, columnspan=1)

button_find = tk.Button(root, text=" Search for Jobs ", bg="#CC9B68", fg="white", width=15, pady=5, font=("Calibri ", 18),
                        command=myClass, relief="raised", padx=50)
button_find.grid(row=9, column=2, columnspan=1)


def show(ttext, ttext1):
    ttext = ttext.replace(" ", "+")
    url = "https://in.indeed.com/jobs?q=" + ttext + "&l=" + ttext1
    res = requests.get(url)
    html_text = res.content
    soup = BeautifulSoup(html_text, 'html.parser')
    job_card = soup.find('div', class_='jobsearch-SerpJobCard')
    print(job_card)
    try:
        job_title = job_card.h2.a
    except AttributeError:
        job_title = ' '
    try:
        job_location = job_card.find('span', class_='location accessible-contrast-color-location')
    except AttributeError:
        job_location = ' '
    try:
        job_company = job_card.find('span', class_='company')
    except AttributeError:
        job_company = ' '
    try:
        job_link = 'https://www.indeed.com' + job_card.h2.a.get('href')
    except AttributeError:
        job_link = ' '
    try:
        job_summary = job_card.find('div', class_='summary')
    except AttributeError:
        job_summary = ' '
    try:
        post_date = job_card.find('span', class_='date date-a11y')
    except AttributeError:
        post_date = ' '

    url_S = (
        f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={ttext}&txtLocation={ttext1}")
    r = requests.get(url_S)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    div = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    avar = div.a
    comp = div.find('h3', class_="joblist-comp-name")
    desc = div.find('ul', class_='list-job-dtl clearfix')
    loc = div.find('ul', class_='top-jd-dtl clearfix')
    str1 = loc.get_text()
    str2 = str(str1)
    location = str2.replace("card_travel", "experience ")

    try:
        job_salary = job_card.find('span', class_='salaryText').get_text()
    except AttributeError:
        job_salary = ' '
    tempList = [job_title.get_text(), job_location.get_text(), job_company.get_text(), job_summary.get_text(),
                job_salary, post_date.get_text()]
    tempList1 = [avar.get_text(), comp.get_text(), desc.text.strip(), location]
    indeed_list = ["Job Title:", "Job Location:", "Company Name:", "Job Summary:", "Job Salary:", "post date:"]
    listBox.insert(END, "INDEED: ")
    listBox.insert(END, "\n")
    for i in range(0, 6):
        listBox.insert(END, indeed_list[i])
        listBox.insert(END, tempList[i])
        listBox.insert(END, "\n")

    listBox.insert(END, "\n")
    listBox.insert(END, "TIMESJOBS: ")
    listBox.insert(END, "\n")

    listBox.insert(END, "Job Title:")
    listBox.insert(END, tempList1[0])
    listBox.insert(END, "\n")
    listBox.insert(END, "Company Name:")
    listBox.insert(END, tempList1[1])
    listBox.insert(END, "\n")
    listBox.insert(END, tempList1[2])
    listBox.insert(END, "\n")

    listBox.insert(END, tempList1[3])
    listBox.insert(END, "\n")


listBox = Text(root, width=80, bg="aquamarine", relief="raised", font=("Calibri", 10))
listBox.grid(row=1, column=2, )
listBox.insert(END, "JOB COMPARE")
listBox.insert(END, "\n")

root.mainloop()
