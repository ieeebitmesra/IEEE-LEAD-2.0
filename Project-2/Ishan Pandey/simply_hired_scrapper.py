from tkinter.constants import NONE
import requests
from bs4 import BeautifulSoup
import urllib

soup = NONE

def simplyhired_search(job_profile, location, n):
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
    template = f"https://www.simplyhired.co.in/search?q={job_profile}&l={location}"
    return template

cards = []
title = NONE
company_name = NONE
job_location = NONE
description = NONE
card_link = NONE

def details(n):
    global cards, title, company_name, job_location, description, card_link
    cards = soup.find_all(class_="SerpJob-jobCard")
    if len(cards)!=0:
        try:
            title = cards[n].find(class_="jobposting-title").get_text()
        except AttributeError:
            title = "NOT AVAILABLE"
        try:
            company_name = cards[n].find(class_="jobposting-company").get_text()
        except AttributeError:
            company_name = "NOT AVAILABLE"
        try:
            job_location = cards[n].find(class_="jobposting-location").get_text()
        except AttributeError:
            job_location = "NOT AVAILABLE"
        try:
            description = cards[n].find(class_="jobposting-snippet").get_text()
        except AttributeError:
            description = "NOT AVAILABLE"
        card_link = ("https://www.simplyhired.co.in" +cards[n].find(class_="SerpJob-link")["href"])