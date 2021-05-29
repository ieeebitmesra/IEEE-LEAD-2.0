from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import webbrowser
import re
from functools import partial
from tkinter import *
from tkinter import ttk

links = []
button_list = []
result_labels = []


def open_link(link_id):
    webbrowser.open(links[link_id])


def search(*args):
    for button in button_list:
        button.destroy()

    for label in result_labels:
        label.destroy()

    result_labels.clear()
    button_list.clear()
    links.clear()

    search_keywords = user_input.get().split()

    base_url = "https://www.google.com/search?q="

    url = base_url + "+".join(search_keywords)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(url=url, headers=headers)

    html = urlopen(req).read()

    soup = BeautifulSoup(html, 'html.parser')

    base_redirect_url = "https://www.google.com"

    link_count = 0
    max_link_count = 5
    row_num = 5

    label = ttk.Label(frame, text="here are some search results from google!".upper())
    label.grid(column=1, row=4, sticky=(W, E), pady=5)
    result_labels.append(label)

    for section in soup.find_all("div", class_="kCrYT"):
        for a_tag in section.find_all("a"):
            result_url = base_redirect_url + a_tag["href"]

            link_text = re.search("/url\\?q=(.*)?&sa", result_url)[0]
            link_text = link_text[len("/url?q="):len(link_text) - len("&sa")]

            check_hash = re.search("%23.*$", link_text)
            if check_hash is not None:
                link_text = link_text[:len(link_text) - len(check_hash[0])]

            already_present = False
            for old_link in links:
                if old_link == link_text:
                    already_present = True

            if already_present:
                continue

            links.append(link_text)
            button = ttk.Button(frame, text=link_text, command=partial(open_link, link_count))
            button_list.append(button)

            button.grid(column=1, row=row_num, sticky=(E, W), pady=5)
            row_num += 1
            link_count += 1
            if link_count >= max_link_count:
                break
        if link_count >= max_link_count:
            break

    if link_count == 0:
        ttk.Button(frame, text="No Results Found!!!").grid(column=1, row=row_num, sticky=(E, W))


root = Tk()

root.title("Google Search")

frame = ttk.Frame(root, padding="20 30 30 30")

frame.grid(column=0, row=0, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

user_input = StringVar()

ttk.Label(frame, text="What would you like to search ?".upper())\
    .grid(column=1, row=1, sticky=(W, E), pady=5)

user_input_widget = ttk.Entry(frame, width=60, justify='center',
                              textvariable=user_input)

user_input_widget.grid(column=1, row=2, sticky=(E, W))

ttk.Button(frame, text="Search", command=search).grid(column=1, row=3, sticky=(E, W), pady=10)

user_input_widget.focus()

root.bind('<Return>', search)

root.mainloop()
