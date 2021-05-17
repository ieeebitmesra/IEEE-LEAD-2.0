import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from tkinter import *


def myClass():
    show(ttext.get())


root = tk.Tk()
root.grid_columnconfigure((0, 1), weight=1)
root.configure(background="#10D5E2")
root.geometry("800x800")
root.title("IEEE LEAD2.0")
root.configure(borderwidth="5", background="#282828", cursor="arrow")
root.resizable(False, False)
label_head = tk.Label(root, text="GOOGLE SEARCH", font=("Cambrian", 45), relief="flat", fg="aquamarine",
                      background="#282828")
label_head.grid(row=0, column=2, pady=20)

Label1 = tk.Label(root)
_image1 = PhotoImage(file="googleSearchImage.png")
Label1.configure(image=_image1, background="aquamarine")
Label1.configure(text='''Label''')
Label1.grid(row=2, column=2, padx=200, pady=10)

ttext = tk.Entry(root, width=50, bg="white", fg="black", font=("Calibri", 15), relief="flat")
ttext.grid(row=7, column=2, pady=5)

label1 = tk.Label(root, text="Enter query: ", bg="#282828", fg="aquamarine", font=("lob", 15), relief="flat", )
label1.grid(row=6, column=2, pady=10)

button_find = tk.Button(root, text="Search for Jobs", bg="#282828", fg="aquamarine", width=30, pady=5,
                        font=("Calibri", 18), command=myClass, relief="raised", padx=50)
button_find.grid(row=9, column=2)


def show(search_text):
    text = search_text
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    res = requests.get("https://www.google.com/search?q=" + ' '.join(text))
    soup = BeautifulSoup(res.text, "html.parser")
    link_elements = soup.select('.kCrYT a')
    link_length = min(1, len(link_elements))
    for i in range(link_length):
        url = link_elements[i].get('href')
        webbrowser.open('https://google.com/' + url)


root.mainloop()
