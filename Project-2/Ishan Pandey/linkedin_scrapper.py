from tkinter.constants import NONE
import requests
from bs4 import BeautifulSoup
import urllib

soup = NONE

def linkedin_search(job_profile,location,n):
    url = url_gen(job_profile, location)
    page = requests.get(url)
    global soup
    soup = BeautifulSoup(page.content, "html.parser")
    details(n)


def url_gen(job_profile, location):
    job_profile = urllib.parse.quote(job_profile, safe='')
    location = urllib.parse.quote(location, safe='')
    template = f"https://in.linkedin.com/jobs/search?keywords={job_profile}&location={location}"
    return template

cards = []
title = NONE
company_name = NONE
job_location = NONE
short_description = NONE
posted = NONE
card_link = NONE

def details(n):
    global cards,title,company_name,job_location,short_description,posted,card_link
    cards = soup.find_all(class_="result-card")
    if(len(cards) != 0):
        try:
            title = cards[n].find(class_="screen-reader-text").get_text()
        except AttributeError:
            title = "NOT AVAILABLE"
        try:
            company_name = cards[n].find(class_="result-card__subtitle").get_text()
        except AttributeError:
            company_name= "NOT AVAILABLE"
        try:
            job_location = cards[n].find(class_="job-result-card__location").get_text()
        except AttributeError:
            location = "NOT AVAILABLE"
        try:
            short_description = cards[n].find(class_="job-result-card__snippet").get_text()
        except AttributeError:
            short_description = "NOT AVAILABLE"
        try:
            posted = cards[n].find("time")["datetime"]
        except AttributeError:
            posted = "NOT AVAILABLE"
        card_link = cards[n].find(class_="result-card__full-card-link")["href"]


