#This Program Scrapes Jobs from 2 websites , namely TimesJobs and LinkedIn. The Scraped Jobs are then #displayed with the help of a simple and distinctive GUI . A button is also present corresponding 
#to each Job, which when clicked directs the user to the detailed information of the Job.

#Tech Stack Used:
#Language - Python 3.9.4
#Modules - Tkinter , requests , Beautiful Soup , WebBrowser and PIL

from tkinter import *
import tkinter as tk
from tkinter import *
import tkinter as tki
import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import Tk, Label
from PIL import Image, ImageTk
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#Scrapes the post,experience,company name,location and links of 15-20 jobs 
#The scraped jobs are stored in a list of dictionaries containing the informations
#This list is returned
def TimesJob(kw):
        url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='+kw+'&txtLocation=India#'

        html_text=requests.get(url , headers= headers )
        soup = BeautifulSoup(html_text.text , "html.parser")
        data_list = []
        
        z=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
        for x in z:
            temp_dict = {}
            
            y=x.header.h2.a.text.strip()
            temp_dict['POST']= y

            y=x.ul
            y=y.find_all('li')
            for p in y:
                li_descendants = p.descendants 
                for d in li_descendants :
                    if(d.name == 'span'):

                        temp_dict['LOCATION']=d.text 
                

            y=x.ul.li.text.strip().replace('card_travel','')
            temp_dict['EXPERIENCE']= y

            y=x.header.h2.a['href']
            temp_dict['KNOW MORE']= y

            y=x.header.h3.text.replace('(More Jobs)','').strip()
            temp_dict['COMPANY'] = y  

            data_list.append(temp_dict)
        
        return data_list


#Scrapes the Post, Company name and link of 15-20 jobs
#The scraped jobs are stored in a list of dictionaries containing the informations
#This list is returned
def LinkedInJobs(kw):
    LinkedIn_list =[]

    url ='https://in.linkedin.com/jobs/search?keywords='+kw+'&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0'

    html_text=requests.get(url , headers= headers )

    soup = BeautifulSoup(html_text.text , "html.parser")

    z = soup.find_all('div' ,class_='base-card base-card--link base-search-card base-search-card--link job-search-card' )
    for x in z:
        temp_dict2 = {}
        y=x.find('a',class_='job-search-card__subtitle').text.strip()
        temp_dict2['C'] = y

        y=x.find('h3',class_='base-search-card__title').text.strip()
        temp_dict2['P'] = y

        y=x.find('div',class_='base-search-card__metadata').span.text.strip()
        temp_dict2['L']=y

        y=x.find('a' , class_='base-card__full-link')
        temp_dict2['Know'] =y['href']

        LinkedIn_list.append(temp_dict2) 
    
    return LinkedIn_list


#This function comes into action on clicking the search Button
#It displays the jobs after manipulating the data obtained from 2 scraping functions
def myClick():

    kw =entry.get()

    Times_list = TimesJob(kw) 

    LinkedIn_list = LinkedInJobs(kw)  


#The below two commands correspond to a button which contains the detailed link of Jobs 
    def cmd1():
        webbrowser.open(Times_list[0]['KNOW MORE'])
        
    def cmd2():
        webbrowser.open(LinkedIn_list[0]['Know'])

        

#Stores the data of Job scraped from TimesJobs    
    bottomframe = Frame(root)
    answer1 = Text(bottomframe,height=15)
    answer1.pack()
    
#The if else statements ensures that if no link is found , the 'Visit Link'
#buttons will automatically get DISABLED    
    if (len(Times_list) == 0):
        linkButton1 = Button(bottomframe,text='Visit Link',command=cmd1,state=DISABLED)
        linkButton1.pack()
 
    else:
        linkButton1 = Button(bottomframe,text='Visit Link',command=cmd1)
        linkButton1.pack()

#This label creates a blank line separating the 2 Jobs 
    labelSpace=Label(bottomframe, text=' ')
    labelSpace.pack() 
    
#Stores the data of Job scraped from TimesJobs
    answer2 = Text(bottomframe,height=10)
    answer2.pack()

#The if else statements ensures that if no link is found , the 'Visit Link'
#buttons will automatically get DISABLED    
    if (len(LinkedIn_list) == 0):
        linkButton2 = Button(bottomframe,text='Visit Link',command=cmd2,state=DISABLED)
        linkButton2.pack()
 
    else:
        linkButton2 = Button(bottomframe,text='Visit Link',command=cmd2)
        linkButton2.pack()

    bottomframe.pack()

#This is the default value of Text containing Job, so that the GUI doesnot 
# terminates if the list of Jobs is empty , i.e. No Job is found    
    Fact1 = 'Not Found'

    if (len(Times_list) != 0):
             
        Fact1 ='''Times Jobs  

COMPANY:
{0}

POST:
{1}

LOCATION:
{2}

EXPERIENCE:
{3}

        '''.format(Times_list[0]['COMPANY'],Times_list[0]['POST'],Times_list[0]['LOCATION'],Times_list[0]['EXPERIENCE'])

#This is the default value of Text containing Job, so that the GUI doesnot 
# terminates if the list of Jobs is empty , i.e. No Job is found     
    Fact2 = 'Not Found'
    if (len(LinkedIn_list) != 0):
            Fact2 ='''LinkedIn

COMPANY: 
{0}

POST:
{1}

LOCATION:
{2}

            '''.format(LinkedIn_list[0]['C'],LinkedIn_list[0]['P'],LinkedIn_list[0]['L'])


    answer1.insert(tk.END,Fact1)
    answer2.insert(tk.END,Fact2)
    
    

#the main window of Tkinter contains the topframe and bottomframe
#The topframe has an entry widget and a search button to shoot the further program
root = Tk()
root.geometry("800x650")

topframe = Frame (root)
entry = Entry(topframe,width=80)
entry.pack(ipady=3)

button = Button(topframe,text='search',command=myClick)
button.pack()
labelSpace0=Label(topframe, text=' ')
labelSpace0.pack() 
topframe.pack(side= TOP)

root.mainloop()
