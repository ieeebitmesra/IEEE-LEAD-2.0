from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
import time


root2 = Tk()
root2.title("Monster.com Search Result")
root2.call('wm', 'iconphoto', root2._w, PhotoImage(file='Images/monster.png'))

monster_logo = ImageTk.PhotoImage(Image.open("Images/monsterfull.png"))
label_moster = Label(image=monster_logo)

search_bar = Entry(root2, width=50, borderwidth=2, font=(18))

label_moster.grid(column=0, row=0,padx=80, pady=60,columnspan=3)
search_bar.grid(column=0, row=2,columnspan=3,pady=10)

def on_click():
    search_text = search_bar.get()
    url = "https://www.monsterindia.com/srp/results?query="+search_text
    # headers = {"user-agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    driver = webdriver.Chrome("C:\\Users\\Rishika Raj\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get(url)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html5lib")
    # print(soup.prettify())
    driver.quit()
    f = True
    if soup.find('div', class_='job-title'):
        if soup.find('h3', class_='medium'):
            title= soup.find('h3', class_='medium').get_text()
        else:
            title=' No job available '
        if soup.find('span', class_='loc'):
            dura= soup.find('span', class_='loc').get_text()
        else:
            dura=" N/A "
        if soup.find('span', class_='SalarySnb'):
            sal=soup.find('span', class_='SalarySnb').get_text()
        else:
            sal=' N/A '
        if soup.find('span', class_='loc'):
            loc=soup.find('span', class_='loc').get_text()
        else:
            loc=" N/A "
        if soup.find('p', class_='job-descrip'):
            des=soup.find('p', class_='job-descrip').get_text()
        else:
            des=' N/A '
        if soup.find('p',class_='descrip-skills'):
            skill=soup.find('p',class_='descrip-skills').get_text()
        else:
            skill=' N/A '  
        link = soup.find('a', target='_blank').get('href')
    else:
        f = False
        title= ' No job available '
        des=' N/A '
        sal= ' N/A '
        loc= ' N/A '
        dura= ' N/A '
        skill= ' N/A '
        
        
        
    def open_link():
        webbrowser.open_new(link)
        
    title_label = Label(root2, text=title)
    des_label = Label(root2, text='Description :'+des)
    salary_label= Label(root2, text='Salary : '+sal )
    loca_label=Label(root2, text='Location : '+ loc )
    durat_label= Label(root2, text='Experience : '+dura )
    skill_label= Label(root2, text='Required skills : '+skill)    
    title_label.config(font=(14))
    des_label.config(font=(10))
    salary_label.config(font=(12))
    loca_label.config(font=(12))
    durat_label.config(font=(12))
    skill_label.config(font=(10))
    title_label.grid(column=1, row=5, pady=0)
    des_label.grid(column=1, row=6, pady=0)
    salary_label.grid(column=1, row=7, pady=0)
    loca_label.grid(column=1, row=8, pady=0)
    durat_label.grid(column=1, row=9, pady=0)
    skill_label.grid(column=1, row=10, pady=0)
    
    def label_del():
        title_label.grid_forget()
        des_label.grid_forget()
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
            
    my_button = Button(root2, text="Search", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(14)) 
    my_button.grid(column=1, row=3, pady=20,padx=40)

    exit_btn = Button(root2, text="Exit", command=root2.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    if f:
        link_button = Button(root2, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_button.config(font=(14))
        link_button.grid(column=1, row=11, pady=10, padx=40)
        exit_btn.grid(column=1, row=12, pady=10, padx=40)
    else:
        exit_btn.grid(column=1, row=12, pady=10, padx=40)

my_button = Button(root2, text="Search", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(14)) 
my_button.grid(column=1, row=3, pady=20,padx=40)


root2.mainloop()