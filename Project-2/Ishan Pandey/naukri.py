from job_scrapper_gui import naukri_gui
import requests
from bs4 import BeautifulSoup
import urllib

job_profile = input()
location = input()

def url_gen(job_profile, location):
    # temp1 = job_profile
    # temp1 = temp1.replace(' ','-')
    # temp2=location
    # temp2=temp2.replace(' ', '-')
    job_profile = (urllib.parse.quote(job_profile, safe=''))
    location = (urllib.parse.quote(location, safe=''))
    # template = f"https://www.naukri.com/{temp1}-jobs-in-{temp2}?k={job_profile}&l={location}"
    template = f'https://www.naukri.com/search?k={job_profile}&l={location}'
    return template

def naukri_search(job_profile,location):
    # job_profile = input()
    # location = input()
    url = url_gen(job_profile, location)
    print(url)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    # page = requests.get(url, headers=headers)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless') 
    # driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=options)
    # driver.get(url)
    page = requests.get(url,headers=headers)
    global soup
    soup = BeautifulSoup(page.content, "html.parser")
    with open('./temp.html', 'a', encoding="utf-8") as f:
        f.write(str(soup))

naukri_search(job_profile,location)