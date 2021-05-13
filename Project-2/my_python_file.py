from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import requests
from bs4 import BeautifulSoup


#===========================================
def open_google():
    google_window = Toplevel(root)
    google_window.geometry("500x400") #widthxheight
    google_window.minsize(200,100) #width,height
    google_window.title("google")

    f1 = Frame(google_window, bg="white", borderwidth=6)
    f1.pack(side=TOP, fill="x")
    # photo = PhotoImage(file="D:\wallpapers\google2.png") #if png image    
    # piclb = Label(google_window,image=photo)
    # piclb.pack()
    # photo = ImageTk.PhotoImage(Image.open("D:\wallpapers\google2.png"))
    # piclb = Label(google_window, image=photo).pack()
    f2 = Frame(google_window, bg="grey", borderwidth=6)
    f2.pack(side=TOP, fill="x")
    f3 = Frame(google_window, bg="grey", borderwidth=6)
    f3.pack(side=TOP, fill="x")

    #==================================================
    def searchit():
        searchWord = keyword.get()
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        r = requests.get("https://www.google.com/search?q=" + ''.join(searchWord),headers = header)
        htmlContent = r.content
        # print(htmlContent) #------yuRUbf
        soup = BeautifulSoup(htmlContent, 'html.parser')
        result_links = soup.select('.yuRUbf a')
        link_len = min(1, len(result_links))

        all_links = set()
        count = 0
        radvar = radio.get()

        link = result_links[0]
        linkText = link.get('href')
        if(radvar=="1"):
            webbrowser.open(linkText)
        else:
            cur_text = Text(google_window, height=1, relief=GROOVE)
            cur_text.pack(fill="x")
            cur_text.insert(INSERT,linkText)

        # for link in result_links:
        #     if(link.get('href') != '#'):
        #         linkText = link.get('href')
        #         count = count + 1
        #         if(radvar=="1"):
        #             webbrowser.open(linkText)
        #         else:
        #             # print(">>>>>>>> " +linkText)
        #             cur_text = 'text' + str(count)
        #             cur_text = Text(root, bg="yellow", height=5, relief=GROOVE)
        #             cur_text.pack(fill="x")
        #             cur_text.insert(INSERT,linkText)
        #     if(count == 6):
        #         break
    #==================================================

    mylabel2 = Label(f2, text="search here")
    mylabel2.grid(row=0,column=0, padx=20, pady=10)

    keyword = StringVar()#input keyword
    Entry(f2, textvariable=keyword).grid(row=0,column=1)


    mylabel3 = Label(f2, text="enter 1 if you want to be directed directly to webpages")
    mylabel3.grid(row=1,column=0, padx=20, pady=10)

    radio = StringVar()#input keyword
    Entry(f2, textvariable=radio).grid(row=1,column=1)

    b1 = Button(f2, fg="red", text="search", command=searchit)
    b1.grid(row=3,column=1)
#===========================================
#===========================================
def open_indeed():
    indeed_window = Toplevel(root)
    indeed_window.geometry("800x650") #widthxheight
    indeed_window.minsize(200,100) #width,height
    indeed_window.title("jobs here!!")
    f1 = Frame(indeed_window, bg="black", borderwidth=6)
    f1.pack(side=TOP, fill="x")
    l1 = Label(f1, text="job list at INDEED")
    l1.pack()

    f2 = Frame(indeed_window, bg="grey", borderwidth=6)
    f2.pack(side=TOP, fill="x")
    labels = ['name / post','company','location']

    for i in range(len(labels)):
        cur_lb = 'lb' + str(i)
        cur_lb = Label(f2, text=labels[i], bg="yellow", height=1, relief=GROOVE)
        cur_lb.grid(row=0,column=i, padx=3, pady=3)
    #=========================================================
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/90.0.4430.93 Safari/537.36'}
    r = requests.get("https://in.indeed.com/jobs-in-Varanasi,-Uttar-Pradesh")
    htmlContent = r.content
    # print(htmlContent)
    soup = BeautifulSoup(htmlContent, 'html.parser')

    cn = 0
    for names in soup.select('a.jobtitle'):
        cn = cn + 1
        if cn==11:
            break
        mytxt = names.getText()
        #print(names.getText())
        cur_lb = 'lb' + str(cn)
        cur_lb = Label(f2, text=mytxt, width=50, relief=GROOVE)
        cur_lb.grid(row=cn,column=0, padx=3, pady=3)
    #=============================================
    cn = 0
    for names in soup.select('span.company'):
        cn = cn + 1
        if cn==11:
            break
        mytxt = names.getText()
        #print(names.getText())
        cur_lb = 'lb2' + str(cn)
        cur_lb = Label(f2, text=mytxt, width=30, relief=GROOVE)
        cur_lb.grid(row=cn,column=1, padx=3, pady=3)
    #=============================================
    cn = 0
    for names in soup.select('span.location'):
        cn = cn + 1
        if cn==11:
            break
        mytxt = names.getText()
        #print(names.getText())
        cur_lb = 'lb3' + str(cn)
        cur_lb = Label(f2, text=mytxt, width=20, relief=GROOVE)
        cur_lb.grid(row=cn,column=2, padx=3, pady=3)


#=====================indeed ends here=======================
root = Tk()
#gui logic
root.geometry("200x200") #widthxheight
root.minsize(100,100) #width,height
root.title("scrapping project")

btn1 = Button(root, text="get first search result from google", command=open_google)
btn1.pack()
btn2 = Button(root, text="get scrapping results for indeed.com", command=open_indeed)
btn2.pack()
#===============================
root.mainloop()
