# from job_scrapper_gui import naukri_gui
from tkinter import *
from PIL import ImageTk
import PIL.Image
import naukri_scrapper
import linkedin_scrapper
import indeed
import simply_hired_scrapper
from selenium import webdriver


root = Tk()
root.title("Compare Jobs")
root.geometry("1000x670")
root.configure(background='white')

# ----------------Header GUI----------------
# -------Creating All labels--------
logo = ImageTk.PhotoImage(PIL.Image.open("./Images\compare.png"))
header_frame = LabelFrame(bg="#135EC2",borderwidth=0,highlightthickness=0)
# logo 
logo_label = Label(header_frame,image=logo,bg='#135EC2')
# job title container
job_title_frame = LabelFrame(header_frame,bg='#135EC2',borderwidth=0,highlightthickness=0)
job_label = Label(job_title_frame,text="JOB TITLE",bg='#135EC2',fg="white",font=('Bahnschrift Light', 13, 'normal'))
job_profile_box = Entry(job_title_frame, width=30, font=('Bahnschrift Light', 13, 'normal'))
# location container
location_frame = LabelFrame(header_frame,bg='#135EC2',borderwidth=0,highlightthickness=0) 
location_label = Label(location_frame,text="LOCATION",bg='#135EC2',fg="white",font=('Bahnschrift Light', 13, 'normal'))
location_box = Entry(location_frame, width=30, font=('Bahnschrift Light', 13, 'normal'))
# compare button container
compare_button_frame = LabelFrame(header_frame,padx=50,pady=10,bg='#135EC2',borderwidth=0,highlightthickness=0)
# ------labels created-------

# ------packing labels-------
header_frame.pack(fill=X)
logo_label.grid(row=0,column=0,pady=3,padx=10)
job_title_frame.grid(row=0,column=1,pady=10,padx=20)
job_profile_box.pack()
job_label.pack(side=LEFT)
location_frame.grid(row=0,column=2,pady=10,padx=20)
location_box.pack()
location_label.pack(side=LEFT)
compare_button_frame.grid(row=1,column=1,columnspan=2)
# ------------Header GUI ends--------------

# ------------Compare JOBS GUI--------------

card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
card_container.pack(fill=X)

def visit(website):
    if website=="Naukri.com":
        url = str(naukri_scrapper.card_link)
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url)
    if website=="indeed.com":
        url = str(indeed.card_link)
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url)
    if website=="Linkedin":
        url = str(linkedin_scrapper.card_link)
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url)
    if website=="SimplyHired":
        url = str(simply_hired_scrapper.card_link)
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url)

# ----Naukri.com GUI----
def naukri_gui():
    if len(naukri_scrapper.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_label = Label(error_card_frame,text="Naukri.com",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.pack()
        site_name_label.pack(fill=X,pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else :
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text="Naukri.com",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        visit_button = Button(site_name_frame,text="Visit",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=lambda: visit("Naukri.com"))
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        title_lable = Label(head_frame,text=naukri_scrapper.title,wraplength=300,font=('Bahnschrift Light', 13, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=naukri_scrapper.company_name,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=naukri_scrapper.job_location,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        rating_label = Label(head_frame,text=f"Rating: {naukri_scrapper.rating}",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        salary_label = Label(head_frame,text=f"Salary: {naukri_scrapper.salary}",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        skills_label = Label(head_frame,text=f"Skills:\n{naukri_scrapper.skills}",wraplength=300,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")

        card_frame.grid(row=0,column=0,padx=100)
        site_name_frame.pack(fill=X)
        visit_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        title_lable.pack()
        company_name_lable.pack()
        job_location_label.pack()
        rating_label.pack()
        salary_label.pack()
        skills_label.pack()
# ----Naukir.com GUI completed----

# --------indeed GUI--------------
def indeed_gui():
    if len(indeed.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_label = Label(error_card_frame,text="indeed.com",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.grid(row=0,column=1)
        site_name_label.pack(fill=X,pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text="indeed.com",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        visit_button = Button(site_name_frame,text="Visit",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=lambda: visit("indeed.com"))
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        title_lable = Label(head_frame,text=indeed.title,wraplength=300,font=('Bahnschrift Light', 13, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=indeed.company_name,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=indeed.job_location,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        rating_label = Label(head_frame,text=f"Rating: {indeed.rating}",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        salary_label = Label(head_frame,text=f"Salary: {indeed.salary}",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")   

        card_frame.grid(row=0,column=1,padx=50)
        site_name_frame.pack(fill=X)
        visit_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        title_lable.pack(padx=50)
        company_name_lable.pack()
        job_location_label.pack()
        rating_label.pack()
        salary_label.pack()
# ----indeed GUI completed----

# -------Linkedin GUI---------
def linkedin_gui():
    if len(linkedin_scrapper.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white")
        site_name_label = Label(error_card_frame,text="Linkedin",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white",borderwidth=0,highlightthickness=0)
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.grid(row=1,column=0)
        site_name_label.pack(fill=X,pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text="indeed.com",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        visit_button = Button(site_name_frame,text="Visit",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=lambda: visit("Linkedin"))
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        title_lable = Label(head_frame,text=linkedin_scrapper.title,wraplength=300,font=('Bahnschrift Light', 13, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=linkedin_scrapper.company_name,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=linkedin_scrapper.job_location,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        rating_label = Label(head_frame,text="Rating: Not Available",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        salary_label = Label(head_frame,text="Salary: Not Available",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        
        card_frame.grid(row=1,column=0,padx=100,pady=5)
        site_name_frame.pack(fill=X)
        visit_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        title_lable.pack(padx=50)
        company_name_lable.pack(pady=5)
        job_location_label.pack(pady=5)
        rating_label.pack()
        salary_label.pack()
# --------Linkedin GUI completed------------

# ---------SimplyHired GUI------------------
def simply_hired_gui():
    if len(simply_hired_scrapper.cards)==0:
        error_card_frame = LabelFrame(card_container,bg="white",borderwidth=0,highlightthickness=0)
        site_name_label = Label(error_card_frame,text="SimplyHired",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        no_result_label = Label(error_card_frame,text="No result",bg="white",font=('Bahnschrift Light', 12, 'bold'),fg="#135EC2",highlightthickness=0)
        message_frame = LabelFrame(error_card_frame,bg="white")
        message_lable = Label(message_frame,text="OOPS!!! check your keyword and try again",bg="white",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",highlightthickness=0)

        error_card_frame.grid(row=1,column=1)
        site_name_label.pack(fill=X,pady=1)
        no_result_label.pack()
        message_frame.pack()
        message_lable.pack(side=LEFT)
    else:
        card_frame = LabelFrame(card_container,bg="white")
        site_name_frame = LabelFrame(card_frame,bg="white",borderwidth=0,highlightthickness=0)
        site_name_lable = Label(site_name_frame,text="indeed.com",bg="white",font=('Bahnschrift Light', 11, 'bold'),fg="#135EC2",highlightthickness=0)
        visit_button = Button(site_name_frame,text="Visit",font=('Bahnschrift Light', 10, 'bold'),fg="#135EC2",bg="white",command=lambda: visit("SimplyHired"))
        head_frame = LabelFrame(card_frame,borderwidth=0,highlightthickness=0,bg="#135EC2")
        title_lable = Label(head_frame,text=simply_hired_scrapper.title,wraplength=300,font=('Bahnschrift Light', 13, 'bold'),bg="#135EC2",fg="white")
        company_name_lable = Label(head_frame,text=simply_hired_scrapper.company_name,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        job_location_label = Label(head_frame,text=simply_hired_scrapper.job_location,wraplength=250,font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        rating_label = Label(head_frame,text="Rating: Not Available",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        salary_label = Label(head_frame,text="Salary: Not Available",font=('Bahnschrift Light', 11, 'normal'),bg="#135EC2",fg="white")
        
        card_frame.grid(row=1,column=1,padx=50,pady=5)
        site_name_frame.pack(fill=X)
        visit_button.pack(side=RIGHT,pady=1,padx=1)
        site_name_lable.pack(pady=1)
        head_frame.pack(fill=X)
        title_lable.pack(pady=5,padx=50)
        company_name_lable.pack(pady=5)
        job_location_label.pack(pady=5)
        rating_label.pack()
        salary_label.pack()
# ----------SimplyHired GUI-------------

def close():
    global card_container
    card_container.pack_forget()
    card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
    card_container.pack(fill=X)

is_both_empty = False
def compare():
    global card_container
    card_container.pack_forget()
    card_container = LabelFrame(root,bg="white",pady=20,borderwidth=0,highlightthickness=0)
    card_container.pack(fill=X)
    if not str(job_profile_box.get()) and not str(location_box.get()) :
        global is_both_empty
        is_both_empty=True
        message_frame = LabelFrame(card_container,bg="white",padx=20,pady=30)
        message_label = Label(message_frame,text="Please enter Job Title and Location to compare",font=('Bahnschrift Light', 14, 'bold'),bg="white",fg="#135EC2")
        close_button = Button(card_container,text="Close",font=('Bahnschrift Light', 14, 'bold'),bg="white",fg="#135EC2",command=close)

        message_frame.pack(pady=20)
        message_label.pack()
        close_button.pack()
    else:
        job_profile = str(job_profile_box.get())
        location = str(location_box.get())
        naukri_scrapper.naukri_search(job_profile,location,0)
        indeed.indeed_search(job_profile,location,0)
        linkedin_scrapper.linkedin_search(job_profile,location,0)
        simply_hired_scrapper.simplyhired_search(job_profile,location,0)
        naukri_gui()
        indeed_gui()
        linkedin_gui()
        simply_hired_gui()

compare_button = Button(compare_button_frame,text="Comapre",padx=15,pady=7,font=('Bahnschrift Light', 12, 'bold'),bg="white",fg="#135EC2",command=compare)
compare_button.pack()

root.mainloop()