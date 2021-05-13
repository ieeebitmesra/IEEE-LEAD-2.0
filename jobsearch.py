import requests
from bs4 import BeautifulSoup
from tkinter import *
 
root=Tk() 
root.geometry("900x700")
root.minsize(800,650)

#creating functions
def shine():

    global List
    list = Listbox(root,width=100,height=20,relief=SUNKEN,borderwidth=10)                           
    list.grid(row=4,columnspan=3)
    a=job_entry.get()
    url="https://www.shine.com/job-search/python-jobs".replace("python",a)
    r=requests.get(url)
    html_content=r.content
    soup=BeautifulSoup(html_content,'lxml')
    jobs=soup.find_all('ul',class_="d-flex flex-column result-display")
    for job in jobs:
        Expereince=job.find_all('li',class_="w-30 mr-10 result-display__profile__years")
        for Exp in Expereince:
            firm_name=Exp.previous_element.previous_element
            jobdesc=Exp.previous_element.previous_element.previous_element.previous_element
            list.insert(END,f"Firm Name : {firm_name.strip()}")
            list.insert(END,f"Expereince Req : {Exp.text.strip()}")
            list.insert(END,f"Location : {Exp.next_sibling.text.strip()}")
            list.insert(END,f"Job Description :{jobdesc.strip()}")
            list.insert(END," ")


def times():
    global list
    list = Listbox(root,width=100,height=20,relief=SUNKEN,borderwidth=10)
    list.grid(row=4,columnspan=3)
    
    b=job_entry.get() 
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=".replace("python",b)

    r=requests.get(url)
    html_content=r.content
    soup=BeautifulSoup(html_content,'lxml')
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        firm_name=job.find('h3',class_="joblist-comp-name").text.replace("  ","")
        exp=job.ul.li.text.replace("card_travel","Experience requirement :")
        venue=job.ul.li.next_sibling.next_sibling.text.replace("location_on","")
        job_desc=job.ul.next_sibling.next_sibling.li.label.next_element.next_element
        key_skills=job.ul.next_sibling.next_sibling.li.next_sibling.next_sibling.label.next_sibling.next_sibling.text
        
        list.insert(END,f"Firm: {firm_name.strip()}")
        list.insert(END,exp)
        list.insert(END,f"Venue : {venue.strip()}")
        list.insert(END,f"Job Description : {job_desc.strip()}")
        list.insert(END,f"Skills Required : {key_skills.strip()}")
        list.insert(END," ")




#creating heading:
heading=Label(root,text="Job Search",font="Arial 25 bold",relief=SUNKEN,padx=40,pady=20,bg="grey",fg="white",anchor=CENTER)
heading.grid(row=0,columnspan=3)
#getting the details from the user

job=Label(root,text="Enter the Job : ",padx=10,pady=40,font="Arial 15 bold")
uservalue = StringVar()
job_entry=Entry(root, textvariable = uservalue,width=50,borderwidth=10,bg="white",fg="dark red",relief=SUNKEN,font="Arial 15 bold")
job.grid(row=1,column=0)
job_entry.grid(row=1,column=1,columnspan=3)

#giving the search buttons:
Search=Label(root,text="Search : ",padx=15,pady=20,font="Arial 18 bold",bg="dark red",fg="white",relief=SUNKEN)
shine_button=Button(root,text="Shine",font="Arial 18 bold",padx=25,pady=20,command=shine,bg="dark blue",fg="white",relief=SUNKEN)
times_button=Button(root,text="Timesjob",font="Arial 18 bold",padx=15,pady=20,command=times,bg="dark blue",fg="white",relief=SUNKEN)

#displaying search buttons
Search.grid(row=2,column=0)
shine_button.grid(row=2,column=1)
times_button.grid(row=2,column=2)
root.mainloop()