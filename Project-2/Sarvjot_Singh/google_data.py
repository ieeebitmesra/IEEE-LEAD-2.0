import requests
from bs4 import BeautifulSoup
import re

def google_fun(query):

    query = query.replace(" ", "+")

    url = "https://www.google.com/search?q="+query

    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")

    div_list = soup.find_all("div", class_="kCrYT")
    link_list = []
    name_list = []

    for div in div_list:
        for a in div.find_all("a"):
            final_url = a["href"]
            pattern = "/url\\?q=.*?&sa"
            final_url = re.search(pattern, final_url)
            if final_url is not None:
                final_url = final_url.group()
                final_url = final_url[7:len(final_url)-3]
                link_list.append(final_url)

                pattern2 = "://.*?/"
                name = re.search(pattern2,final_url).group()   
                name = name.replace("://","")
                name = name.replace("www.","")
                name = name.replace("/","")
                name_list.append(name)
                # webbrowser.open(final_url)

    google_obj = {
        'names' : name_list,
        'links' : link_list
    }

    return google_obj