from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser


root0 = Tk()
root0.title("Google First Search Result")
root0.call('wm', 'iconphoto', root0._w, PhotoImage(file='Images/google.png'))

global f

search_logo = ImageTk.PhotoImage(Image.open("Images/googlefull.png"))
label_search = Label(image=search_logo)

search_bar = Entry(root0, width=50, borderwidth=2, font=(18))

label_search.grid(column=1, row=0,padx=80, pady=60,columnspan=2)
search_bar.grid(column=1, row=2,columnspan=2,pady=10)

def on_click():
    f=0
    search_text = search_bar.get()
    url = "https://www.google.co.in/search?q="+search_text
    headers = {"user-agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    flag = True
    anchors = soup.find('div', class_="g")
    # print(anchors.prettify)
    if anchors:
        link = anchors.find('a')['href']
    else:
        flag = False

    def open_link():
        webbrowser.open_new(link)
        
        
    if flag and anchors.find('h3'):
        title_label = Label(root0, text=anchors.find('h3').get_text(), fg='blue')
        link_label = Label(root0, text=anchors.find('cite').get_text(),fg='purple')
        des_label = Label(root0, text=soup.find('div',class_='IsZvec').get_text(),fg='#888888', wraplength=950, justify="left")
        f=1;
        link_button = Button(root0, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_button.config(font=(14))
        link_button.grid(column=1, row=7, pady=10,sticky="E", padx=40)
    else:
        f=0
        title_label = Label(root0, text="Ooops (Search Failed)!!",fg="#a9a9a9")
        link_label = Label(root0, text="No Results",fg="#a9a9a9")
        des_label = Label(root0, text="Try another keyword..",fg="#a9a9a9")
    
    title_label.config(font=(32))
    link_label.config(font=(24))
    des_label.config(font=(16))

    
    title_label.grid(column=1, row=4, columnspan=2, pady=0, padx=10)
    link_label.grid(column=1, row=5, columnspan=2, pady=0, padx=10)
    des_label.grid(column=1, row=6, columnspan=2, pady=0, padx=10)

    def label_del():
        title_label.grid_forget()
        link_label.grid_forget()
        des_label.grid_forget()
        exit_btn.grid_forget()
        if f==1:
            link_button.grid_forget()
        else:
            on_click()

    my_button = Button(root0, text="Google Search", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(15)) 
    my_button.grid(column=1, row=3,padx=40, pady=20,  sticky="E")
    
    my_button = Button(root0, text="I'm Feeling Lucky", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(15)) 
    my_button.grid(column=2, row=3,padx=40, pady=20,  sticky="W")

    exit_btn = Button(root0, text="Exit", command=root0.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    exit_btn.grid(column=2, row=7, pady=10,sticky="W", padx=40)

my_button = Button(root0, text="Google Search", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(15)) 
my_button.grid(column=1, row=3, pady=20,padx=40,  sticky="E")
    
my_button = Button(root0, text="I'm Feeling Lucky", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(15)) 
my_button.grid(column=2, row=3, pady=20,padx=40,  sticky="W")

root0.mainloop()