import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from tkinter import *


def myclass():
    show(t1.get())


root = tk.Tk()
root.grid_columnconfigure((0, 1), weight=1)
root.configure(background="#10D5E2")
root.geometry("800x600")
root.title("WEB SCRAPPING TOOL")
root.configure(borderwidth="10", relief="sunken",
               background="#F4D160", cursor="arrow")
root.resizable(False, False)
label_head = tk.Label(root, text="GOOGLE SEARCH First URL", font=(
    "lob", 35), relief="flat", fg="white", background="#2978B5")
label_head.grid(row=0, column=2, pady=20)

Label1 = tk.Label(root)
_img1 = PhotoImage(file="google.png")
Label1.configure(image=_img1, background="#E5D008")
Label1.configure(text='''Label''')
Label1.grid(row=2, column=2, padx=250, pady=10)


t1 = tk.Entry(root, width=40, bg="white", fg="black",
              font=("lob", 15), relief="sunken")
t1.grid(row=7, column=2, pady=10)

label1 = tk.Label(root, text="Enter the keyword", bg="#00917C",
                  fg="white", font=("lob", 15), relief="flat",)
label1.grid(row=6, column=2, pady=10)

button_find = tk.Button(root, text=" Click to open the website", bg="#2978B5", fg="white",
                        width=30, pady=5, font=("lob ", 18), command=myclass, relief="raised", padx=50)
button_find.grid(row=9, column=2)


def show(search_text):
    text = search_text
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    res = requests.get("https://www.google.com/search?q="+' '.join(text))
    soup = BeautifulSoup(res.text, "html.parser")
    link_elements = soup.select('.kCrYT a')
    link_length = min(1, len(link_elements))
    for i in range(link_length):
        url = link_elements[i].get('href')
        webbrowser.open('https://google.com/'+url)


root.mainloop()
