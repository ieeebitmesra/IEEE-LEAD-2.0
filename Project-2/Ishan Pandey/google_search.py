from PIL import ImageTk
import PIL.Image
from tkinter import *
import urllib
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# -------URL generator----------


def url_gen(search_term):
    search_term = (urllib.parse.quote(search_term, safe=''))
    template = f"https://www.google.com/search?q={search_term}"
    return template

# ---------GOOGLE SEARCH----------


def google(search_term,):
    url = url_gen(search_term)
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    page = requests.get(url, headers=headers)
    global soup
    soup = BeautifulSoup(page.text, "html.parser")
    search_results()


def search_results():
    global heading
    global description
    global link
    global result_found
    first_search = soup.find("div", attrs={"class": "hlcw0c"})
    heading = first_search.find("h3", attrs={"class": "LC20lb DKV0Md"}).get_text()
    description = first_search.find("span", attrs={"class": "aCOpRe"}).get_text()
    a = first_search.find('a')
    link = a['href']
    if link[0] == '/':
        link = "https://www.google.com"+link



# GUI App

root = Tk()
root.geometry("1000x650")
root.title("Google.com")
root.configure(background='white')


def open_page():
    global driver
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(link)


def destroy_frame():
    global result_container
    result_container.pack_forget()
    result_container = LabelFrame(root,bg="white",borderwidth=0,highlightthickness=0)
    result_container.pack(pady=20)


def display_result():

    global display_frm
    display_frm = LabelFrame(result_container, padx=5, pady=5)
    my_label = Label(display_frm, text="Search Result",font=('Bahnschrift Light', 10, 'normal'))
    heading_lable = Label(display_frm, text=heading,font=('Bahnschrift Light', 15, 'normal'))
    description_label = Label(display_frm, text=description, wraplength=700, justify=LEFT, font=('Bahnschrift Light', 10, 'normal'))
    visit_button = Button(display_frm, text="Visit Page", command=open_page)
    close_button = Button(display_frm, text="Close", command=destroy_frame)

    display_frm.pack(pady=5, padx=30)
    my_label.grid(row=0, column=0, padx=0)
    heading_lable.grid(row=1, column=0)
    description_label.grid(row=2, column=0)
    visit_button.grid(row=3, column=0)
    close_button.grid(row=3, column=1)


def search():
    global result_container
    result_container.pack_forget()
    result_container = LabelFrame(root,bg="white",borderwidth=0,highlightthickness=0)
    result_container.pack(pady=20)
    search_term = str(search_entry.get())
    google(search_term)
    display_result()


my_img1 = ImageTk.PhotoImage(PIL.Image.open('./Images\google.png'))

empty_label1 = Label(root, height=7, bg="white")
google_label = Label(root, image=my_img1, bg="white")
empty_label2 = Label(root, height=2, bg="white")
search_entry = Entry(root, width=50, font=('Bahnschrift Light', 15, 'normal'))
empty_label3 = Label(root, height=1, bg="white")
search_button = Button(root, text="Google Search",padx=10, pady=10, command=search, bg="white")
result_container = LabelFrame(root,bg="white",borderwidth=0,highlightthickness=0)


empty_label1.pack()
google_label.pack()
empty_label2.pack()
search_entry.pack(ipady=2)
empty_label3.pack()
search_button.pack()
result_container.pack(pady=20)

root.mainloop()
