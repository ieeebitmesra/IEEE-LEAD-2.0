import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
 
root = Tk()
root.geometry("1600x800")
root.configure(background="white")
root.title("   Times Job")
root.wm_iconbitmap("timesjob.ico")


photo= PhotoImage(file="timesjob.png")
lab1= Label(image= photo)
lab1.pack()


def click():
    global keyword,title, company, experience, location, desc_title, descs
    global text
    global url

    keyword=screen.get()
    url = ("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords="+str(keyword))
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    title =soup.select_one("#searchResultData ul li header a").text.strip()
    company=soup.select_one("#searchResultData ul li header h3").text.strip()
    experience=soup.select_one("#searchResultData ul li .top-jd-dtl li").contents[1]
    location=soup.select_one("#searchResultData ul li .top-jd-dtl li span").contents[0]
    desc_title= soup.select_one("#searchResultData ul li .list-job-dtl li label").contents[0]
    descs= soup.select_one("#searchResultData ul li .list-job-dtl li").contents[2].strip()
    print(title)
    print("Company: ",company)
    print("Experience required: ",experience)
    print("Location: ",location)
    print(desc_title)
    print(descs)
    value=((f"{title}\nCompany: {company}\nExperience: {experience}\nLocation: {location}\n{desc_title}: {descs}\n"))
    scvalue.set(value)
    display.update()
    scvalue1.set("Visit site")
    display1.update()
    


def opener():
    webbrowser.open(url)
keyword=StringVar()
keyword.set(" ")
screen = Entry(root, textvar=keyword, font="Angsana 30 " )
screen.configure( background="white smoke")
screen.pack(fill=X, ipadx=8, padx=100, pady=5)


f = Frame(root, bg="light gray")
# b = Button(f,text="Search",font="Helvetica 25 ", padx=27,pady=5)
b=Button(f ,text="Search",font="Helvetica 15 ", padx=27,pady=5,command=click)
b.pack(side= LEFT, padx=2, pady=2)
b.bind("<Button-1>",click)
b.configure( background="silver")
f.pack()



scvalue = StringVar()
scvalue.set("")
display = Label(root, textvar=scvalue, font="Angsana 12 " )
display.configure( background="white smoke")
display.pack(fill=X, ipadx=8, padx=5, pady=5)


f = Frame(root, bg="light gray")
scvalue1 = StringVar()
scvalue1.set("TIMES JOB")
display1 = Button(f, textvar=scvalue1, font="Angsana 12 ",command=opener ,padx=27,pady=5)
display1.configure( background="white smoke")
display1.pack(fill=X, ipadx=8, padx=5, pady=5)
f.pack()

root.mainloop()

