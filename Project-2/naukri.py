import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from tkinter import *
import webbrowser
from PIL import ImageTk, Image

root = Tk()
root.geometry("1600x800")
root.configure(background="white")
root.title("   naukri.com")
root.wm_iconbitmap("naukri_logo.ico")


image = Image.open("naukri_img.jpg")
photo = ImageTk.PhotoImage(image)
lab1= Label(image= photo)
lab1.pack()


def click():
    global url
    df = pd.DataFrame(columns=['Title', 'Company', 'Ratings', 'Reviews',
                      'Experience', 'Salary', 'Location', 'Job_Post_History', 'URL'])
    keyword = screen.get()
    url = ("https://www.naukri.com/"+str(keyword)+"-jobs")

    page = requests.get(url)

    driver = webdriver.Chrome("C:\\Users\\hp\\Downloads\\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html5lib')

    driver.quit()

    results = soup.find(class_='list')
    job_elem = results.find('article', class_='jobTuple bgWhite br4 mb-8')

    URL = job_elem.find('a', class_='title fw500 ellipsis').get('href')

   
    Title = job_elem.find('a', class_='title fw500 ellipsis')

    Company = job_elem.find('a', class_='subTitle ellipsis fleft')

    rating_span = job_elem.find('span', class_='starRating fleft dot')
    if rating_span is None:
        Ratings = " "

    else:
        Ratings = rating_span.text

    Review_span = job_elem.find(
        'a', class_='reviewsCount ml-5 fleft blue-text')
    if Review_span is None:
        Reviews = " "

    else:
        Reviews = Review_span.text

    Exp = job_elem.find(
        'li', class_='fleft grey-text br2 placeHolderLi experience')
    Exp_span = Exp.find('span', class_='ellipsis fleft fs12 lh16')
    if Exp_span is None:

        Experience = " "
    else:
        Experience = Exp_span.text


    Sal = job_elem.find(
        'li', class_='fleft grey-text br2 placeHolderLi salary')
    Sal_span = Sal.find('span', class_='ellipsis fleft fs12 lh16')
    if Sal_span is None:

        Salary = " "
    else:
        Salary = Sal_span.text

    Loc = job_elem.find(
        'li', class_='fleft grey-text br2 placeHolderLi location')
    Loc_exp = Loc.find('span', class_='ellipsis fleft fs12 lh16')
    if Loc_exp is None:
        Location = " "

    else:
        Location = Loc_exp.text

    Hist = job_elem.find(
        "div", ["type br2 fleft grey", "type br2 fleft green"])
    Post_Hist = Hist.find('span', class_='fleft fw500')
    if Post_Hist is None:

        Post_History = " "
    else:
        Post_History = Post_Hist.text

    df = df.append({'URL': URL, 'Title': Title.text, 'Company': Company.text, 'Ratings': Ratings, 'Reviews': Reviews,
                   'Experience': Experience, 'Salary': Salary, 'Location': Location, 'Job_Post_History': Post_History}, ignore_index=True)

    value = ((f"{Title.text}\nCompany: {Company.text}\nExperience: {Experience}\nLocation: {Location}\nRatings: {Ratings}\nReview: {Reviews}\nSalary: {Salary}\nJob Post History: {Post_History}"))
    scvalue.set(value)
    display.update()
    scvalue1.set("Visit site")
    display1.update()


def opener():
    webbrowser.open(url)


keyword = StringVar()
keyword.set(" ")
screen = Entry(root, textvar=keyword, font="Angsana 30 ")
screen.configure(background="white smoke")
screen.pack(fill=X, ipadx=8, padx=100, pady=5)


f = Frame(root, bg="light gray")
# b = Button(f,text="Search",font="Helvetica 25 ", padx=27,pady=5)
b = Button(f, text="Search", font="Helvetica 15 ",
           padx=27, pady=5, command=click)
b.pack(side=LEFT, padx=2, pady=2)
# b.bind("<Button-1>",click)
b.configure(background="silver")
f.pack()


scvalue = StringVar()
scvalue.set("")
display = Label(root, textvar=scvalue, font="Angsana 12 ")
display.configure(background="white smoke")
display.pack(fill=X, ipadx=8, padx=5, pady=5)


f = Frame(root, bg="light gray")
scvalue1 = StringVar()
scvalue1.set("NAUKRI.COM")
display1 = Button(f, textvar=scvalue1, font="Angsana 12 ",
                  command=opener, padx=27, pady=5)
display1.configure(background="white smoke")
display1.pack(fill=X, ipadx=8, padx=5, pady=5)
f.pack()

root.mainloop()
