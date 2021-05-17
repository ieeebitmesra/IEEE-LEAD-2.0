from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser


root3 = Tk()
root3.title("Compare ")
root3.call('wm', 'iconphoto', root3._w, PhotoImage(file='WebScrapping/Images/ieee.png'))

compare_logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/images.png"))
label_0 =Label(root3, text="Enter basis of comparision:")
label_compare = Label(image=compare_logo)
label_0.config(font=(40))


search_bar = Entry(root3, width=50, borderwidth=3, font=(18))

label_compare.grid(column=0, row=0,padx=70, pady=50,columnspan=3)
label_0.grid(column=0, row=1, columnspan=3)
search_bar.grid(column=0, row=2,columnspan=3,pady=10,padx=30)

ns_logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/web_ns.png"))
label_ns = Label(image=ns_logo)

ms_logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/web_ms.png"))
label_ms = Label(image=ms_logo)


def on_click():
    label_ns.grid(column=0, row=4, padx="30")
    label_ms.grid(column=2, row=4, padx="30")
    
    search_text = search_bar.get()
    url1 = "https://www.google.co.in/search?q="+search_text
    url2 = "https://www.google.co.in/search?q="+search_text
    headers = {"user-agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req1 = requests.get(url1, headers=headers)
    req2 = requests.get(url2, headers=headers)
    soup1 = BeautifulSoup(req1.content, "html.parser")
    soup2 = BeautifulSoup(req2.content, "html.parser")
    flag1 = True
    flag2 = True
    
    # anchors = soup.find('div', class_="g")
    # print(anchors.prettify)
        
        
    if flag and anchors.find('h3'):
        title_label = Label(root3, text=anchors.find('h3').get_text(), fg='blue')
        link_label = Label(root3, text=anchors.find('cite').get_text(),fg='purple')
        des_label = Label(root3, text=soup.find('div',class_='IsZvec').get_text(),fg='#888888', wraplength=900, justify="left")
        f=1;
        link_btn = Button(root3, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_btn.config(font=(14))
        link_btn.grid(column=0, row=8, pady=10, padx=40)
    
        link_btn2 = Button(root3, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_btn2.config(font=(14))
        link_btn2.grid(column=2, row=8, pady=10, padx=40)
    else:
        f=0
        title_label = Label(root3, text="Ooops (Search Failed)!!",fg="#415662")
        link_label = Label(root3, text="No Results",fg="#415662")
        des_label = Label(root3, text="Try another keyword..",fg="#415662")
    
    title_label.config(font=(32))
    link_label.config(font=(24))
    des_label.config(font=(16))

    
    title_label.grid(column=1, row=5, pady=0)
    link_label.grid(column=1, row=6, pady=0)
    des_label.grid(column=1, row=7, pady=0)
    
    # link_btn = Button(root3, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
    # link_btn.config(font=(14))
    # link_btn.grid(column=0, row=8, pady=10, padx=40)
    
    # link_btn2 = Button(root3, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
    # link_btn2.config(font=(14))
    # link_btn2.grid(column=2, row=8, pady=10, padx=40)
    
    
    def label_del():
        title_label.grid_forget()
        link_label.grid_forget()
        des_label.grid_forget()
        exit_btn.grid_forget()
        if f==1:
            link_btn.grid_forget()
            link_btn2.grid_forget()
        else:
            on_click()
            
    my_button = Button(root3, text="Comapare", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(14)) 
    my_button.grid(column=1, row=3, pady=20,padx=40)


    exit_btn = Button(root3, text="Exit", command=root3.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    exit_btn.grid(column=1, row=10, pady=10, padx=40)


my_button = Button(root3, text="Comapare", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(14)) 
my_button.grid(column=1, row=3, pady=20,padx=40)



root3.mainloop()