from tkinter.constants import NONE
import urllib
from bs4 import BeautifulSoup
import requests

soup = NONE

def indeed_search(job_profile,location,n):
    url = url_gen(job_profile, location)
    print(url)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    page = requests.get(url, headers=headers)
    global soup
    soup = BeautifulSoup(page.content, "html.parser")
    details(n)


def url_gen(job_profile, location):
    job_profile = (urllib.parse.quote(job_profile, safe=''))
    location = (urllib.parse.quote(location, safe=''))
    template = f"https://in.indeed.com/jobs?q={job_profile}&l={location}"
    return template

#  DETAILS WE GET 
title = NONE
company_name = NONE
rating = NONE
job_location = NONE
summary = NONE
card_link = NONE
salary = NONE 
cards = []


def details(n):
    global cards
    cards = soup.find_all(class_="jobsearch-SerpJobCard")

    # To handle when no search result found
    if len(cards)!=0:
        title_tag = cards[n].h2.a
        global title
        global company_name
        global rating
        global job_location
        global salary
        global summary
        global card_link
        title = str(title_tag.get_text()).replace(" ","")

        try:
            company_name = cards[n].find(class_="company").get_text()
        except AttributeError:
            company_name = "Not Available"
        try:
            rating = cards[n].find(class_="ratingsContent").get_text()
        except AttributeError:
            rating = "Not Available"
        try:
            job_location = str(cards[n].find(class_="recJobLoc")["data-rc-loc"])
        except AttributeError:
            job_location = "Not Available"
        try:
            salary = cards[n].find(class_="salaryText").get_text()
        except AttributeError:
            salary = "Not Available"
        try:
            summary = cards[n].find(class_="summary").get_text()
        except AttributeError:
            summary = "Not Available"
        card_link = "https://in.indeed.com" + cards[n].find(class_="jobtitle")["href"]

