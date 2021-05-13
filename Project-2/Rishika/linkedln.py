from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser
from datetime import date, timedelta, datetime
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from warnings import warn


root3 = Tk()
root3.title("LinkedIn Search Result")
root3.call('wm', 'iconphoto', root3._w, PhotoImage(file='Images/link.png'))

monster_logo = ImageTk.PhotoImage(Image.open("Images/linkfull.png"))
label_moster = Label(image=monster_logo)

search_bar = Entry(root3, width=50, borderwidth=2, font=(18))

label_moster.grid(column=0, row=0,padx=80, pady=60,columnspan=3)
search_bar.grid(column=0, row=2,columnspan=3,pady=10)

def on_click():
    search_text = search_bar.get()
    url = "https://www.linkedin.com/jobs/search/?keywords="+search_text
    # headers = {"user-agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    driver = webdriver.Chrome("C:\\Users\\Rishika Raj\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)
    time.sleep(10)
    action = ActionChains(driver)
    pageSource = driver.page_source
    lxml_soup = BeautifulSoup(pageSource, 'lxml')
    #soup = BeautifulSoup(driver.page_source, "html5lib")
    job = lxml_soup.find('ul', class_ = 'jobs-search__results-list')
    print(lxml_soup.prettify())
    # driver.quit()
    f = True
    if lxml_soup.find('ul', class_ = 'jobs-search__results-list'):
        link = lxml_soup.find('a',class_='base-card__full-link').get('href')
        if job.find("span", class_="screen-reader-text"):
            title= job.find("span", class_="screen-reader-text").get_text()
        else:
            title=' No job available '
        # if job_elem.find('li',class_='fleft grey-text br2 placeHolderLi experience'):
        #     Exp = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi experience')
        #     dura= Exp.find('span',class_='ellipsis fleft fs12 lh16').get_text()
        # else:
        #     dura=" N/A "
        if job.find('li',class_='fleft grey-text br2 placeHolderLi salary'):
            Sal = job.find('li',class_='fleft grey-text br2 placeHolderLi salary')
            sal=Sal.find('span',class_='ellipsis fleft fs12 lh16').get_text()
        else:
            sal=' N/A '
        job_xpath = '/html/body/main/div/section/ul/li[{}]/img'.format()
        driver.find_element_by_xpath(job_xpath).click()
        time.sleep(3)
        type_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[2]'
        dura = driver.find_element_by_xpath(type_xpath).text.splitlines(0)[1]
        
        if job.find("span", class_="job-result-card__location"):
            # Loc = job_elem.find('li',class_='fleft grey-text br2 placeHolderLi location')
            loc=job.find("span", class_="job-result-card__location").get_text()
        else:
           loc=" N/A "
        comp=job.select_one('img')['alt']
        if lxml_soup.find('ul', class_ = 'job-criteria__list'):
            job_criteria_container = lxml_soup.find('ul', class_ = 'job-criteria__list')
            skill=job_criteria_container.find("span", class_='job-criteria__text job-criteria__text--criteria').get_text()
        else:
            skill=' N/A '  
        rat = job.select_one('time')['datetime']
        
    else:
        f = False
        title= ' No job available '
        comp=' N/A '
        rat =' N/A '
        sal= ' N/A '
        loc= ' N/A '
        dura= ' N/A '
        skill= ' N/A '
        
        
    title_label = Label(root3, text=title)
    des_label = Label(root3, text='Company :'+comp)
    rat_label = Label(root3, text='Post date : '+rat)
    salary_label= Label(root3, text='Salary : '+sal )
    loca_label=Label(root3, text='Location : '+ loc )
    durat_label= Label(root3, text='Type : '+dura )
    skill_label= Label(root3, text='Required skills : '+skill)    
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
            
    my_button = Button(root3, text="Search", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(14)) 
    my_button.grid(column=1, row=3, pady=12,padx=40)

    exit_btn = Button(root3, text="Exit", command=root3.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    if f:
        link_button = Button(root3, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_button.config(font=(14))
        link_button.grid(column=1, row=11, pady=10, padx=40)
        exit_btn.grid(column=1, row=12, pady=5, padx=40)
    else:
        exit_btn.grid(column=1, row=12, pady=5, padx=40)

my_button = Button(root3, text="Search", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(14)) 
my_button.grid(column=1, row=3, pady=20,padx=40)


root3.mainloop()