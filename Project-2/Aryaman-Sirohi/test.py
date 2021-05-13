from os import error
import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.request import urlopen
import time
text=input("Enter the type of job: ")
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
res=requests.get("https://www.google.com/search?q="+''.join(text)+" jobs linkedin",headers=headers)
soup=BeautifulSoup(res.text,"lxml")
link_elements=soup.find_all('div', class_='yuRUbf')
link_length=min(3,len(link_elements))
i=0
j=0
while i<link_length:
    try:
        link=link_elements[j].a.get('href')
    except:
        print("that was all the links")
        break
    if link.find("linked")==-1:
        j+=1
        continue
    x=input("Enter 1 for website, anything else for description: ")
    if link.find("linked")!=-1:
        if x=='1':
            webbrowser.open(link)
        else:
            try:
                # print("the link is: "+link)
                r = requests.get(link, headers=headers)
                soup1 = BeautifulSoup(r.content, 'lxml')
                
                # link_length1=min(3,len(link_elements1))
                link_elements1=soup1.find_all('a', class_='base-card__full-link')
                if len(link_elements1)==0:
                    link_elements1=soup1.find_all('a', class_='result-card__full-card-link')
                for d in range(min(len(link_elements1),3)):
                    link=link_elements1[d].get('href')
                    print(link)
                    r1=requests.get(link, headers=headers)
                    soup2=BeautifulSoup(r1.content,'lxml')
                    try:
                        post=soup2.find_all('h1', class_='topcard__title')[0].get_text()
                    except:
                        post="NA"
                    try:
                        company=soup2.find_all('a', class_='topcard__org-name-link')[0].get_text()
                    except:
                        company="NA"
                    try:
                        company_link=soup2.find_all('a', class_='topcard__org-name-link')[0].get('href')
                    except:
                        company_link="NA"
                    try:
                        location=soup2.find_all('span', class_='topcard__flavor--bullet')[0].get_text()
                    except:
                        location="NA"
                    try:    
                        noapplicants=soup2.find_all('figcaption', class_='num-applicants__caption')[0].get_text()
                    except:
                        noapplicants="NA"
                    try:
                        time1=soup2.find_all('span', class_="posted-time-ago__text")[0].get_text()
                    except:
                        time1="NA"
                    try:
                        seniority= soup2.find_all('li', class_='description__job-criteria-item')[0].get_text()
                    except:
                        seniority="NA"
                    try:
                        employment_type=soup2.find_all('li', class_='description__job-criteria-item')[1].get_text()
                    except:
                        employment_type="NA"
                    try:
                        jobfunc=soup2.find_all('li', class_='description__job-criteria-item')[2].get_text()
                    except:
                        jobfunc="NA"
                    try:
                        industries=soup2.find_all('li',class_='description__job-criteria-item')[3].get_text()
                    except:
                        industries="NA"
                    print("Post:",post.strip())
                    print("Company:",company.strip())
                    # print("",company_link.strip())
                    print("Location:",location.strip())
                    print("Time of posting:",time1.strip())
                    print("No. of applicants so far:",noapplicants.strip())
                    print("Offered post seniority:",seniority.strip()[15:].strip())
                    print("Employment type:",employment_type.strip()[16:].strip())
                    print("Job function:",jobfunc.strip()[12:].strip())
                    print("Industries:",industries.strip()[10:].strip())
                    try:
                        r3=requests.get(company_link,headers=headers)
                    except:
                        r3="NA"
                    try:
                        soup3=BeautifulSoup(r3.content,'lxml')
                        # comp_spec=soup3.find_all("dd",class_="basic-info-item__description")[6].get_text()
                        comp_indust=soup3.find_all("dd",class_="basic-info-item__description")[1].get_text()
                        comp_size=soup3.find_all("dd",class_="basic-info-item__description")[2].get_text()
                        comp_type=soup3.find_all("dd",class_="basic-info-item__description")[4].get_text()
                        comp_website=soup3.find_all("dd",class_="basic-info-item__description")[0].get_text()
                        print("Company industries:",comp_indust)
                        print("No. of personnel:",comp_size)
                        print("Company type:",comp_type)
                    except:
                        print("due to login page, html of the company website is not accessible, and only the link to the profile of the company can be given")
                        print(company_link,"\n\n\n")
                i+=1
            except:
                print("Error occured.\nWill retry")
                time.sleep(3)
                continue

    j+=1
            # for i in range(link_length1):
            #     r1 = requests.get(link_elements1[i].get('href'))
            #     soup2 = BeautifulSoup(r1.content, 'lxml')
            #     soup2.get_text()
            
            