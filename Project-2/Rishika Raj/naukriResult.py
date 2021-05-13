from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import time 

root1 = Tk()
root1.title("Naukri.com Search Result")
root1.call('wm', 'iconphoto', root1._w, PhotoImage(file='Images/naukri.png'))

naukri_logo = ImageTk.PhotoImage(Image.open("Images/naukrifull.jpg"))
label_naukri = Label(image=naukri_logo)

search_bar = Entry(root1, width=50, borderwidth=2, font=(18))

label_naukri.grid(column=0, row=0,padx=70, pady=40,columnspan=3)
search_bar.grid(column=0, row=2,columnspan=3,pady=10)

def on_click():
    search_text = search_bar.get()
    url = "https://www.naukri.com/software-developer-jobs?k="+search_text
    driver = webdriver.Chrome("C:\\Users\\Rishika Raj\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html5lib")
    # print(soup.prettify())
    driver.quit()
    results = soup.find(class_='list')
    f = True
    if results.find('article',class_='jobTuple bgWhite br4 mb-8'):
        job_elem = results.find('article',class_='jobTuple bgWhite br4 mb-8')
        link = job_elem.find('a',class_='title fw500 ellipsis').get('href')
        if job_elem.find('span',class_='starRating fleft dot'):
            rat = job_elem.find('span',class_='starRating fleft dot').get_text()
        else :
            rat=' N/A '
        if job_elem.find('a',class_='title fw500 ellipsis'):
            title= job_elem.find('a',class_='title fw500 ellipsis').get_text()
        else:
            title=' No job available '
        if job_elem.find('li',class_='fleft grey-text br2 placeHolderLi experience'):
            Exp = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi experience')
            dura= Exp.find('span',class_='ellipsis fleft fs12 lh16').get_text()
        else:
            dura=" N/A "
        if job_elem.find('li',class_='fleft grey-text br2 placeHolderLi salary'):
            Sal = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi salary')
            sal=Sal.find('span',class_='ellipsis fleft fs12 lh16').get_text()
        else:
            sal=' N/A '
        if job_elem.find('li',class_='fleft grey-text br2 placeHolderLi location'):
            Loc = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi location')
            loc=Loc.find('span',class_='ellipsis fleft fs12 lh16').get_text()
        else:
           loc=" N/A "
        if job_elem.find('a',class_='subTitle ellipsis fleft'):
            comp=job_elem.find('a',class_='subTitle ellipsis fleft').get_text()
        else:
            comp=' N/A '
        if soup.find('div',class_='tags has-description'):
            skill=soup.find('div',class_='tags has-description').get_text()
        else:
            skill=' N/A '  
        
    else:
        f = False
        title= ' No job available '
        comp=' N/A '
        rat =' N/A '
        sal= ' N/A '
        loc= ' N/A '
        dura= ' N/A '
        skill= ' N/A '
        
        
    title_label = Label(root1, text=title)
    des_label = Label(root1, text='Company :'+comp)
    rat_label = Label(root1, text='Ratings : '+rat)
    salary_label= Label(root1, text='Salary : '+sal )
    loca_label=Label(root1, text='Location : '+ loc )
    durat_label= Label(root1, text='Experience : '+dura )
    skill_label= Label(root1, text='Required skills : '+skill)    
    title_label.config(font=(14))
    des_label.config(font=(10))
    rat_label.config(font=(10))
    salary_label.config(font=(10))
    loca_label.config(font=(10))
    durat_label.config(font=(10))
    skill_label.config(font=(10))
    title_label.grid(column=1, row=4, pady=5)
    des_label.grid(column=1, row=5, pady=0)
    rat_label.grid(column=1, row=6, pady=0)
    salary_label.grid(column=1, row=7, pady=0)
    loca_label.grid(column=1, row=8, pady=0)
    durat_label.grid(column=1, row=9, pady=0)
    skill_label.grid(column=1, row=10, pady=0)
    
    def label_del():
        title_label.grid_forget()
        des_label.grid_forget()
        rat_label.grid_forget()
        exit_btn.grid_forget()
        salary_label.grid_forget()
        loca_label.grid_forget()
        durat_label.grid_forget()
        skill_label.grid_forget()
        if f:
            link_button.grid_forget()
        else:
            exit_btn.grid_forget()
        on_click()
    
    def open_link():
        webbrowser.open_new(link)
            
    my_button = Button(root1, text="Search", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(14)) 
    my_button.grid(column=1, row=3, pady=12,padx=40)

    exit_btn = Button(root1, text="Exit", command=root1.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    if f:
        link_button = Button(root1, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_button.config(font=(14))
        link_button.grid(column=1, row=11, pady=10, padx=40)
        exit_btn.grid(column=1, row=12, pady=5, padx=40)
    else:
        exit_btn.grid(column=1, row=12, pady=5, padx=40)


my_button = Button(root1, text="Search", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(14)) 
my_button.grid(column=1, row=3, pady=15,padx=40)


root1.mainloop()