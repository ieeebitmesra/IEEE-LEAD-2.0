from bs4 import BeautifulSoup
import requests
import tkinter as tk


root =tk.Tk()
root.geometry("500x500")
root.title("Job Search")





location_var=tk.StringVar()
job_type_var=tk.StringVar()
experience_var=tk.StringVar()

def scrap():
    url = "https://www.shine.com/job-search"
    location = location_var.get()
    location = location.replace(" ", "-")
    job_type = job_type_var.get()
    job_type = job_type.replace(" ", "-")
    experience = experience_var.get()
    url_1 = url + "/" + job_type + "-jobs-in-" + location
    req = requests.get(url_1)
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')

    jobs = soup.find_all('div', {'class': 'w-90 ml-25'})

    print("<-------------------Jobs Handpicked For You--------------------->")

    for job in jobs:
        exp = job.find('li', {'class': 'w-30 mr-10 result-display__profile__years'}).text
        exp = exp.replace("Yrs", "")
        exp = exp.replace(" ", "")
        exp = exp.replace("\n", "")
        if int(experience) >= int(exp.split("to")[0]):
            title = job.find('a', {'class': 'job_title_anchor'}).text
            link = job.find('a', {'class': 'job_title_anchor'}).get('href')
            link = "https://www.shine.com" + link
            print('Job Title: ', title)
            print('Link: ', link)



    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords="
    location = location.replace("-", "+")
    job_type = job_type.replace("-", "+")
    url_1 = url + job_type + "&txtLocation=" + location

    req = requests.get(url_1)
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')

    jobs = soup.find_all('li', {'class': 'clearfix job-bx wht-shd-bx'})

    for job in jobs:
        exp_1 = job.find('ul', {'class': 'top-jd-dtl clearfix'})
        exp = exp_1.find('li').text
        exp = exp.replace("card_travel", "")
        exp = exp.replace("yrs", "")
        exp = exp.replace(" ", "")

        if int(experience) >= int(exp.split("-")[0]):
            try:
                a = job_type.split("+")[0]
                b = job_type.split("+")[1]
                a = a.capitalize()
                b = b.capitalize()
            except:
                a=job_type.capitalize()
                b=""
            title = a + " " + b
            link_1 = job.find('header', {'class': 'clearfix'})
            link_2 = link_1.find('h2')
            link = link_2.find('a').get('href')
            print('Job Title: ', title)
            print('Link: ', link)

    location_var.set("")
    experience_var.set("")
    job_type_var.set("")

location_label = tk.Label(root, text='Location', font=('calibre',10, 'bold'))
location_entry = tk.Entry(root, textvariable= location_var, font=('calibre',10, 'normal'))

job_type_label = tk.Label(root, text='Job Type', font=('calibre',10, 'bold'))
job_type_entry = tk.Entry(root, textvariable= job_type_var, font=('calibre',10, 'normal'))

experience_label = tk.Label(root, text= 'Experience', font=('calibre',10, 'bold'))
experience_entry = tk.Entry(root, textvariable= experience_var, font=('calibre',10, 'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = scrap)

location_label.grid(row=0,column=0)
location_entry.grid(row=0,column=1)
job_type_label.grid(row=1,column=0)
job_type_entry.grid(row=1,column=1)
experience_label.grid(row=2,column=0)
experience_entry.grid(row=2,column=1)
sub_btn.grid(row=5,column=1)



root.mainloop()





