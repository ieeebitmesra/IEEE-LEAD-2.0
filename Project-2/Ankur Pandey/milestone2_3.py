import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os


root = tk.Tk()
root.grid_columnconfigure((0, 1), weight=1)
root.configure(bg="#F7A440")
root.geometry("800x700")
root.title("JOB FINDER ")
root.resizable('False', 'False')


Label1 = tk.Label(root)
_img1 = PhotoImage(file="webscrapper.png")
Label1.configure(image=_img1, background="#F7A440")
Label1.configure(text='''Label''')
Label1.grid(row=1, column=0, pady=2)


label_pro = tk.Label(root, text="Job Name  : ", width=20, bg="#00ADB5",
                     fg="black", padx=10, font=("Times", 18), relief="raised")
label_pro.grid(row=7, column=0, pady=10)

label_pro = tk.Label(root, text=" Location : ", width=20, bg="#00ADB5",
                     fg="black", padx=10, font=("Times", 18), relief="raised")
label_pro.grid(row=8, column=0, pady=10)


def myclass():
    show(t2.get(), t3.get())


t2 = tk.Entry(root, width=40, bg="#ffffff", fg="black",
              font=("Times", 18), relief="sunken")
t2.grid(row=7, column=2, columnspan=1)
t3 = tk.Entry(root, width=40, bg="#ffffff", fg="black",
              font=("Times", 18), relief="sunken")
t3.grid(row=8, column=2, columnspan=1)

button_find = tk.Button(root, text=" Search ", bg="#344FA1", fg="white", width=15, pady=5, font=(
    "lob ", 18), command=myclass, relief="raised", padx=50)
button_find.grid(row=9, column=2, columnspan=1)


def show(ttext, ttext1):
    ttext = ttext.replace(" ", "+")
    url = "https://in.indeed.com/jobs?q="+ttext+"&l="+ttext1
    res = requests.get(url)
    html_text = res.content
    soup = BeautifulSoup(html_text, 'html.parser')
    job_card = soup.find('div', class_='jobsearch-SerpJobCard')
    job_title = job_card.h2.a
    job_location = job_card.find(
        'span', class_='location accessible-contrast-color-location')
    job_company = job_card.find('span', class_='company')
    job_link = 'https://www.indeed.com' + job_card.h2.a.get('href')
    job_summary = job_card.find('div', class_='summary')
    post_date = job_card.find('span', class_='date date-a11y')

    url_S = (
        f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={ttext}&txtLocation={ttext1}")
    r = requests.get(url_S)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    divs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    div = divs[0]
    avar = div.a
    comp = div.find('h3', class_="joblist-comp-name")
    descrip = div.find('ul', class_='list-job-dtl clearfix')
    loca = div.find('ul', class_='top-jd-dtl clearfix')
    str1 = loca.get_text()
    str2 = str(str1)
    str3 = str2.replace("card_travel", "experience ")

    try:
        job_salary = job_card.find('span', class_='salaryText').get_text()
    except AttributeError:
        job_salary = ' '
    tempList = [job_title.get_text(), job_location.get_text(), job_company.get_text(
    ), job_summary.get_text(), job_salary, post_date.get_text()]
    tempList1 = [avar.get_text(), comp.get_text(), descrip.get_text(), str3]
    indeed_list = ["Job Title:", "Job Location:", "Company Name:",
                   "Job Summary:", "Job Salary:", "post date:"]
    listBox.insert(END, "INDEED")
    listBox.insert(END, "\n")
    for i in range(0, 6):
        listBox.insert(END, indeed_list[i])
        listBox.insert(END, tempList[i])
        listBox.insert(END, "\n")

    listBox.insert(END, "\n")
    listBox.insert(END, "TIMES JOB")
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


listBox = Text(root, width=80, bg="#E1E5EA",
               relief="sunken", font=("Times", 10))
listBox.grid(row=1, column=2,)
listBox.insert(END, "JOB FINDER")
listBox.insert(END, "\n")

root.mainloop()
