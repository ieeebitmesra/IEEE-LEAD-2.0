from tkinter import *
from PIL import ImageTk
import PIL.Image
import indeed
import linkedin_scrapper
import naukri_scrapper
import simply_hired_scrapper
from selenium import webdriver
from tkinter import ttk

root = Tk()
root.title("Job Searcher")
root.geometry("1100x700")
root.configure(background='white')

# HEADER GUI FOR SEARHCING
clicked ="Naukri.com"
options = [
    "Naukri.com",
    "Linkedin",
    "indeed.com",
    "SimplyHired"
]
def selected(event):
    global clicked
    clicked = site_box.get()
    print(clicked)

logo = ImageTk.PhotoImage(PIL.Image.open("./Images\logo.png"))
header_frame = LabelFrame(bg="#135EC2",borderwidth=0,highlightthickness=0)
logo_label = Label(header_frame,image=logo,bg='#135EC2')
job_frame = LabelFrame(header_frame,bg='#135EC2',borderwidth=0,highlightthickness=0)
job_label = Label(job_frame,text="JOB TITLE",bg='#135EC2',fg="white",font=('Bahnschrift Light', 13, 'normal'))
job_profile_box = Entry(job_frame, width=30, font=('Bahnschrift Light', 13, 'normal'))
location_frame = LabelFrame(header_frame,bg='#135EC2',borderwidth=0,highlightthickness=0) 
location_label = Label(location_frame,text="LOCATION",bg='#135EC2',fg="white",font=('Bahnschrift Light', 13, 'normal'))
location_box = Entry(location_frame, width=30, font=('Bahnschrift Light', 13, 'normal'))
site_frame = LabelFrame(header_frame,borderwidth=0,highlightthickness=0,bg='#135EC2')
site_box = ttk.Combobox(site_frame,value=options,font=('Bahnschrift Light', 11, 'normal'))
site_box.set(options[0])
site_label = Label(site_frame,text="Website",bg='#135EC2',fg="white",font=('Bahnschrift Light', 13, 'normal'))
site_box.bind("<<ComboboxSelected>>",selected)
button_frame = LabelFrame(header_frame,padx=50,pady=10,bg='#135EC2',borderwidth=0,highlightthickness=0)

header_frame.pack(fill=X)
logo_label.grid(row=0,column=0,pady=3,padx=5)
job_frame.grid(row=0,column=1,pady=20,padx=20)
job_profile_box.pack()
job_label.pack(side=LEFT)
location_frame.grid(row=0,column=2,pady=20,padx=20)
location_box.pack()
location_label.pack(side=LEFT)
site_frame.grid(row=0,column=3,padx=20)
site_box.pack()
site_label.pack(side=LEFT)
button_frame.grid(row=1,column=1,columnspan=2)
# HEADER GUI ENDS HERE

# SEARCH RESULT GUI
# user's website choice

card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
card_container.pack(fill=X)

def close():
    global card_container
    card_container.pack_forget()
    card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
    card_container.pack(fill=X)

def next_card(card_num):
    global card_container
    card_container.pack_forget()
    card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
    card_container.pack(fill=X)
    if clicked=="indeed.com":
        indeed.details(card_num)
        indeed_gui(card_num)
    elif clicked=="Naukri.com":
        naukri_scrapper.details(card_num)
        naukri_gui(card_num)
    elif clicked=="Linkedin":
        linkedin_scrapper.details(card_num)
        linkedin_gui(card_num)
    else :
        simply_hired_scrapper.details(card_num)
        simply_hired_gui(card_num)

def prev_card(card_num):
    global card_container
    card_container.pack_forget()
    card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
    card_container.pack(fill=X)
    if clicked=="indeed.com":
        indeed.details(card_num)
        indeed_gui(card_num)
    elif clicked=="Naukri.com":
        naukri_scrapper.details(card_num)
        naukri_gui(card_num)
    elif clicked=="Linkedin":
        linkedin_scrapper.details(card_num)
        linkedin_gui(card_num)
    else :
        simply_hired_scrapper.details(card_num)
        simply_hired_gui(card_num)

def visit_site(link):
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(link)


def indeed_gui(card_num):
    if len(indeed.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        description_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="white") 
        title_lable = Label(head_frame,text=indeed.title,wraplength=350,font=('Bahnschrift Light', 15, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=indeed.company_name,wraplength=300,font=('Bahnschrift Light', 12, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=indeed.job_location,wraplength=300,font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        rating_label = Label(head_frame,text=f"Rating: {indeed.rating}",font=('Bahnschrift Light', 12, 'normal'),bg="#135EC2",fg="white")
        salary_label = Label(head_frame,text=f"Salary: {indeed.salary}",font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        summmary_lable = Label(description_frame,bg="white",fg="#135EC2",text=indeed.summary,wraplength=500,justify=LEFT, font=('Bahnschrift Light', 12, 'bold'))
        button_container = LabelFrame(card_container,bg="white",borderwidth=0,highlightthickness=0)

        prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: prev_card(card_num-1))
        visit = Button(button_container,text="Visit",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: visit_site(indeed.card_link))
        next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: next_card(card_num+1))
        
        if card_num==0:
            prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        if len(indeed.cards)-1==card_num:
            next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        description_frame.pack(fill=X)
        title_lable.pack()
        company_name_lable.pack()
        job_location_label.pack()
        rating_label.pack()
        salary_label.pack()
        summmary_lable.pack(fill=X)
        button_container.pack()
        prev.pack(side=LEFT,padx=15,pady=5)
        visit.pack(side=LEFT,padx=15,pady=5)
        next.pack(padx=15,pady=5)

def naukri_gui(card_num):
    if len(naukri_scrapper.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        description_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="white") 
        title_lable = Label(head_frame,text=naukri_scrapper.title,wraplength=350,font=('Bahnschrift Light', 15, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=naukri_scrapper.company_name,wraplength=300,font=('Bahnschrift Light', 12, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=naukri_scrapper.job_location,wraplength=300,font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        rating_label = Label(head_frame,text=f"Rating: {naukri_scrapper.rating}",font=('Bahnschrift Light', 12, 'normal'),bg="#135EC2",fg="white")
        salary_label = Label(head_frame,text=f"Salary: {naukri_scrapper.salary}",font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        skills_label = Label(head_frame,text=f"Skills:\n{naukri_scrapper.skills}",wraplength=300,font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        summmary_lable = Label(description_frame,bg="white",fg="#135EC2",text=naukri_scrapper.description,wraplength=500,justify=LEFT, font=('Bahnschrift Light', 12, 'bold'))
        button_container = LabelFrame(card_container,bg="white",borderwidth=0,highlightthickness=0)

        prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: prev_card(card_num-1))
        visit = Button(button_container,text="Visit",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: visit_site(naukri_scrapper.card_link))
        next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: next_card(card_num+1))
        
        if card_num==0:
            prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        if len(naukri_scrapper.cards)-1==card_num:
            next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        description_frame.pack(fill=X)
        title_lable.pack()
        company_name_lable.pack()
        job_location_label.pack()
        rating_label.pack()
        salary_label.pack()
        skills_label.pack()
        summmary_lable.pack(fill=X)
        button_container.pack()
        prev.pack(side=LEFT,padx=15,pady=5)
        visit.pack(side=LEFT,padx=15,pady=5)
        next.pack(padx=15,pady=5)

def linkedin_gui(card_num):
    if len(linkedin_scrapper.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        description_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="white") 
        title_lable = Label(head_frame,text=linkedin_scrapper.title,wraplength=350,font=('Bahnschrift Light', 15, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=linkedin_scrapper.company_name,wraplength=300,font=('Bahnschrift Light', 14, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=linkedin_scrapper.job_location,wraplength=300,font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        posted_label = Label(head_frame,text=f"Posted on: {linkedin_scrapper.posted}",font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        summmary_lable = Label(description_frame,bg="white",fg="#135EC2",text=linkedin_scrapper.short_description,wraplength=500,justify=LEFT, font=('Bahnschrift Light', 13, 'bold'))
        button_container = LabelFrame(card_container,bg="white",borderwidth=0,highlightthickness=0)

        prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: prev_card(card_num-1))
        visit = Button(button_container,text="Visit",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: visit_site(linkedin_scrapper.card_link))
        next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: next_card(card_num+1))
        
        if card_num==0:
            prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        if len(linkedin_scrapper.cards)-1==card_num:
            next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        description_frame.pack(fill=X)
        title_lable.pack()
        company_name_lable.pack(pady=5)
        job_location_label.pack(pady=5)
        posted_label.pack(pady=5)
        summmary_lable.pack(fill=X,pady=5)
        button_container.pack()
        prev.pack(side=LEFT,padx=15,pady=5)
        visit.pack(side=LEFT,padx=15,pady=5)
        next.pack(padx=15,pady=5)

def simply_hired_gui(card_num):
    if len(simply_hired_scrapper.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text=clicked,bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        close_button = Button(site_name_frame,text=" X ",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=close)
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        description_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="white") 
        title_lable = Label(head_frame,text=simply_hired_scrapper.title,wraplength=350,font=('Bahnschrift Light', 15, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=simply_hired_scrapper.company_name,wraplength=300,font=('Bahnschrift Light', 14, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=simply_hired_scrapper.job_location,wraplength=300,font=('Bahnschrift Light', 13, 'normal'),bg="#135EC2",fg="white")
        summmary_lable = Label(description_frame,bg="white",fg="#135EC2",text=simply_hired_scrapper.description,wraplength=500,justify=LEFT, font=('Bahnschrift Light', 13, 'bold'))
        button_container = LabelFrame(card_container,bg="white",borderwidth=0,highlightthickness=0)

        prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: prev_card(card_num-1))
        visit = Button(button_container,text="Visit",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: visit_site(simply_hired_scrapper.card_link))
        next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",command=lambda: next_card(card_num+1))
        
        if card_num==0:
            prev = Button(button_container,text="Prev",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        if len(simply_hired_scrapper.cards)-1==card_num:
            next = Button(button_container,text="Next",padx=10,pady=5,font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",bg="white",state=DISABLED)

        card_frame.pack()
        site_name_frame.pack(fill=X)
        close_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        description_frame.pack(fill=X)
        title_lable.pack(pady=5)
        company_name_lable.pack(pady=7)
        job_location_label.pack(pady=7)
        summmary_lable.pack(fill=X,pady=7)
        button_container.pack()
        prev.pack(side=LEFT,padx=15,pady=5)
        visit.pack(side=LEFT,padx=15,pady=5)
        next.pack(padx=15,pady=5)

def search():
    global card_container
    card_container.pack_forget()
    card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
    card_container.pack(fill=X)
    job_profile = str(job_profile_box.get())
    location = str(location_box.get())
    if not str(job_profile_box.get()) and not str(location_box.get()) :
        global is_both_empty
        is_both_empty=True
        message_frame = LabelFrame(card_container,bg="white",padx=20,pady=30)
        message_label = Label(message_frame,text="Please enter Job Title and Location to search",font=('Bahnschrift Light', 14, 'bold'),bg="white",fg="#135EC2")
        close_button = Button(card_container,text="Close",font=('Bahnschrift Light', 14, 'bold'),bg="white",fg="#135EC2",command=close)

        message_frame.pack(pady=20)
        message_label.pack()
        close_button.pack()
    else:
        if clicked=="indeed.com":
            indeed.indeed_search(job_profile,location,0)
            indeed_gui(0)
        elif clicked=="Naukri.com":
            naukri_scrapper.naukri_search(job_profile,location,0)
            naukri_gui(0)
        elif clicked=="Linkedin":
            linkedin_scrapper.linkedin_search(job_profile,location,0)
            linkedin_gui(0)
        else :
            simply_hired_scrapper.simplyhired_search(job_profile,location,0)
            simply_hired_gui(0)

job_search_button = Button(button_frame,text ="Find Jobs",padx=15,pady=7,font=('Bahnschrift Light', 12, 'bold'),bg="white",fg="#135EC2",command=search)

job_search_button.pack()

root.mainloop()