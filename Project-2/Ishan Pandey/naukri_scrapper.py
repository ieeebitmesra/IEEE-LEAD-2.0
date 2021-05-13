# from os import replace
from tkinter.constants import NONE
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver

soup = NONE

def naukri_search(job_profile,location,n):
    url = url_gen(job_profile, location)
    print(url)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=options)
    driver.get(url)
    global soup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    details(n)

def url_gen(job_profile, location):
    temp1 = job_profile
    temp1 = temp1.replace(' ','-')
    temp2=location
    temp2=temp2.replace(' ', '-')
    job_profile = (urllib.parse.quote(job_profile, safe=''))
    location = (urllib.parse.quote(location, safe=''))
    template = f"https://www.naukri.com/{temp1}-jobs-in-{temp2}?k={job_profile}&l={location}"
    return template

title = NONE
company_name = NONE
rating = NONE
experience = NONE
salary = NONE
job_location = NONE
skills = NONE
description = NONE
card_link = NONE
cards = []

def details(n):
    global cards
    global title
    global company_name
    global rating
    global salary
    global job_location
    global skills
    global card_link
    global description

    cards = soup.find_all(class_="jobTuple")
    if len(cards)!=0:
        header = cards[n].find(class_="jobTupleHeader")
        try:
            title = header.find(class_="title")["title"]
        except AttributeError:
            title = "NOT AVAILABLE"
        try:
            company_name = header.find(class_="subTitle")["title"]
        except AttributeError:
            company_name ="NOT AVAILABLE"
        try:
            rating = header.find(class_="starRating").get_text()
        except AttributeError:
            rating = "NOT AVAILABLE"
        try:
            experience = header.find(class_="experience").get_text()
        except AttributeError:
            experience = "NOT AVAILABLE"
        try:
            salary = header.find(class_="salary").get_text()
        except AttributeError:
            salary = "NOT AVAILABLE"
        try:
            job_location = header.find(class_="location").get_text()
        except AttributeError:
            job_location = "NOT AVAILABLE"
        try:
            description = cards[n].find(class_="job-description").get_text()
        except AttributeError:
            description = "NOT AVAILABLE"
        try:
            title_tag = cards[n].find(class_="tags")
            skills_list = title_tag.find_all("li")
            skill_list = []
            for skill in range(0,len(skills_list)):
                skill_list.append(skills_list[skill].get_text())
            skills=''
            for i in range(0,len(skill_list)):
                if i==0:
                    skills+=f"{skill_list[i]}"
                else:
                    skills+=f",{skill_list[i]}"
        except AttributeError:
            skills = "NOT AVAILABLE"
        card_link = header.find(class_="title")["href"]