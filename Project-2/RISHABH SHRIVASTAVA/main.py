
import requests


import webbrowser
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from bs4 import BeautifulSoup
from PIL import Image, ImageTk  
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("page1.jpg")
        load = load.resize((800, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
      
        Button = tk.Button(self,text="Next", font=("Arial", 10),padx=30, command=lambda: controller.show_frame(SecondPage))
        Button.place(x=650, y=450)
        
        Button = tk.Button(self, text="Quit", font=("Arial", 10),padx=30, command=quit)
        Button.place(x=100, y=450)
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #size paramter of icons for ratio application
        x=100
        y=100
        right=50
        down=150
        self.configure(bg='light blue')
        label=tk.Label(self,text="Click on the icon to open website",font=("Arial bold",16),bg="light blue")
        label.place(x=50, y=60)
        

        
        load = Image.open("google.jpg")
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        Button = tk.Button(self,image=photo,font=("Arial", 15), command=lambda: controller.show_frame(google))
        Button.image=photo
        Button.place(x=right, y=down)
        right=right+x*1.5

        load = Image.open("linkedin.png")
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        Button = tk.Button(self, image=photo,font=("Arial", 15), command=lambda: controller.show_frame(linkedin))
        Button.image=photo
        Button.place(x=right, y=down)
        right=right+x*1.5

        load = Image.open("lintern.png")
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        Button = tk.Button(self, image=photo,font=("Arial", 15), command=lambda:controller.show_frame(letsintern))
        Button.image=photo
        Button.place(x=right, y=down)
        right=right+x*1.5
        
        load = Image.open("simplyhired.jpg")
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        Button = tk.Button(self, image=photo,font=("Arial", 15), command=lambda:controller.show_frame(simply_hired))
        Button.image=photo
        Button.place(x=right, y=down)
        right=right+x*1.5

        load = Image.open("indeed.jpg")
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        Button = tk.Button(self, image=photo,font=("Arial", 15), command=lambda: controller.show_frame(indeed))
        Button.image=photo
        Button.place(x=right, y=down)
        list=["google","linkedin","lets intern","simplyhired","indeed"]
    
        right=60
        for items in list:
            Label = tk.Label(self, text=items, font=("Arial Bold",10))
            

            Label.place(x=right, y=down+120)
            right=right+x*1.5
        Button = tk.Button(self, text="Back", font=("Arial", 10), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)    
               
class google(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='white')
        load = Image.open("google_search.jpg")
        #2432 x 1216
        x=500
        y=250
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=150,y=0)
        
        entry1 =tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
        entry1.place(x=250,y=300)
        entry1.insert(0,"")
        def google_search()  :
           search=entry1.get()
           search=search.replace(" ","+")
           res=requests.get("https://www.google.com/search?q="+' '.join(search))
           soup=BeautifulSoup(res.text,"html.parser")
           link_elements=soup.select('.kCrYT a')
           link_length=min(3,len(link_elements))
           for i in range (link_length):
             link=link_elements[i].get('href')
             webbrowser.open('https://google.com/'+link)
             break
        
        
        
        
        save = tk.Button(self, text = 'search',command=google_search)
        save.place(x=370,y=330)  
        button2= tk.Button(self, text="GO BACK", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))  
        button2.place(x=650, y=450)

def openweb(text):
    webbrowser.open(text)             

class linkedin(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='white')
        load = Image.open("linkedin_search.png")
        #1800 x 950
        x=400
        y=200
        load = load.resize((x,y), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        label1 = tk.Label(self, image=photo)
        label1.image=photo
        label1.place(x=200,y=0)
        
        
        label2=tk.Label(self,text="Job title:  ",font=("Arial bold",12))
        label2.place(x=20,y=220)
        
        label3=tk.Label(self,text="Location:",font=("Arial bold",12))
        label3.place(x=20,y=260)

        
        
        entry1 =tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
        entry1.place(x=110,y=223)
        entry1.insert(0,"")
        
        

        
        entry2=tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
        entry2.place(x=110,y=263)
        entry2.insert(0,"")
        button1= tk.Button(self, text="Back", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))
        button1.place(x=650, y=450)

        def linkedin_result():
           
           job_title=entry1.get()
           place=entry2.get()
           label1.destroy()
           label2.destroy()
           label3.destroy()
           entry1.destroy()
           entry2.destroy()
           save.destroy()
           button1.destroy()
      
           self.configure(bg="light blue")
          
           url="https://in.linkedin.com/jobs"
           url_S=(f"https://in.linkedin.com/jobs/search?keywords={job_title}&location={place}&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit")
      
           r = requests.get(url_S)		# r variable has all the HTML code
           htmlContent = r.content
           soup = BeautifulSoup(htmlContent,'html.parser')
           # handle for invalid search or no jobs found page()
    
           div1=soup.find_all('div',class_='result-card__contents job-result-card__contents')
           div2=soup.find_all('a',class_="result-card__full-card-link")
       
           title=[]
           about=[]
           location=[]
           for items in div1:  
             title.append(items.find('h3').text)
             about.append(items.find('h4').text)
             location.append(items.find('span').text)
             
           link=[]
           for items in div2:
             link.append(items.get('href'))
           x=len(link)
           if x<=6:
               x=len(link)
           else:
               x=6
           for i in range(0,x):
             y=str(i+1)
             label=tk.Label(self,text=y+"  JOB TITLE:"+title[i],font=("Arial bold",10))
             label.place(x=0,y=80*i)    
             label=tk.Label(self,text=" COMPANY:"+about[i],font=("Arial bold",10))  
             label.place(x=0,y=25+80*i)
             label=tk.Label(self,text="  LOCATION:"+location[i],font=("Arial bold",10))
             label.place(x=0,y=50+80*i)
           #to get the link
           
           for i in range(0,x):
            
               load = Image.open("apply_now.jpg")
               load = load.resize((180,60), Image.ANTIALIAS)
               photo = ImageTk.PhotoImage(load)
               text=link[i]
               button=tk.Button(self,image=photo,text="apply now",command=lambda:openweb(text))
               button.place(x=450,y=80*i)
               button.image=photo
           
           button2= tk.Button(self, text="GO BACK", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))  
           button2.place(x=650, y=450)
        save = tk.Button(self, text = 'search',command=linkedin_result)
        save.place(x=370,y=330) 
    
class letsintern(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.configure(bg='white')
    load = Image.open("lets_intern.png")
        #1800 x 950
    x=400
    y=200
    #load = load.resize((x,y), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    label1= tk.Label(self, image=photo)
    label1.image=photo
    label1.place(x=200,y=0)
        
        
    label2=tk.Label(self,text="SEARCH INTERNSHIP:  ",font=("Arial bold",12))
    label2.place(x=20,y=220)
    
        
    


    
    entry3=tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
    entry3.place(x=20,y=250)
    entry3.insert(0,"")
   



    
    def letsintern_result():
     search=entry3.get()
     entry3.destroy()
     label1.destroy()
     label2.destroy()
     buttonx.destroy()
     buttony.destroy()

     url=(f"https://www.letsintern.com/internships?search={search}")
     r = requests.get(url)		
     htmlContent = r.content
     soup = BeautifulSoup(htmlContent,'html.parser')
     div=soup.find_all('div',class_="single-job-card")
     job=[]
     about=[]
     i=0
     for items in div:
         i=i+1
         jb=items.find('h4').text
         if(len(jb)==1):#data cleaning if nothing is returned
           continue
       
        
         job.append(jb)
         about.append(items.find('ul',class_="list-group").text)
       
    
     site=soup.find_all('a',class_="btn btn-primary")
     url="https://www.letsintern.com"
    
     link=[]
     for items in site:
        
        link.append(url+items.get('href'))
        
    
    
     load = Image.open("apply_now.jpg")
     load = load.resize((180,60), Image.ANTIALIAS)
     photo = ImageTk.PhotoImage(load)
     start=0
    
     for i in range(start,5):
             x=str(i+1)
             label=tk.Label(self,text=x+"  JOB TITLE:"+job[i],font=("Arial bold",10))
             label.place(x=0,y=80*i)    
             
             label=tk.Label(self,text="   ABOUT:    "+about[i],font=("Arial",7))  
             label.place(x=0,y=35+80*i)
             
             button3=tk.Button(self,image=photo,text="apply now",command=lambda:openweb(link[i]))
             button3.place(x=450,y=80*i)
             button3.image=photo
    
     button4= tk.Button(self, text="GO BACK", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))  
     button4.place(x=650, y=450) 
    buttonx= tk.Button(self, text="Search", font=("Arial", 10), command=letsintern_result)
    buttonx.place(x=370,y=330)
    buttony= tk.Button(self, text="Back", font=("Arial", 10), command=lambda: controller.show_frame(SecondPage))  
    buttony.place(x=100, y=450)  

def st(text):
    text=text[0,25]
    return text
class simply_hired(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.configure(bg='white')
    load = Image.open("simply_hired.png")
        #1800 x 950
    x=400
    y=200
    #load = load.resize((x,y), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    label1= tk.Label(self, image=photo)
    label1.image=photo
    label1.place(x=200,y=0)
        
        

        
        
    label2=tk.Label(self,text="Job title:  ",font=("Arial bold",12))
    label2.place(x=20,y=220)
        
    label3=tk.Label(self,text="Location:",font=("Arial bold",12))
    label3.place(x=20,y=260)

        
        
    entry1 =tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
    entry1.place(x=110,y=223)
    entry1.insert(0,"")
        
        

        
    entry2=tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
    entry2.place(x=110,y=263)
    entry2.insert(0,"")
    

    def simply_hired_result():
           
           job_search=entry1.get()
           job_search=job_search.replace(" ","+")
           location=entry2.get()
           location=location.replace(" ","+")
           label1.destroy()
           label2.destroy()
           label3.destroy()
           entry1.destroy()
           entry2.destroy()
           save.destroy()
           button1.destroy()
           
      
           self.configure(bg="light blue")
          
           
           url=(f"https://www.simplyhired.co.in/search?q={job_search}&l={location}")
           r = requests.get(url)		
           htmlContent = r.content
           soup = BeautifulSoup(htmlContent,'html.parser')
           div=soup.find_all('div',class_="SerpJob-jobCard card")
           #contain code of each search card of result from search
    
     
           div2=soup.find_all('a',class_="SerpJob-link card-link")  
           #this contain html code for url of specific job in the search list
           link=[]
    
           site="https://www.simplyhired.co.in"
    
           for items in div2:

              link.append(site+items.get('href'))
              if(len(link)==5):#let the user choose how many link he want
                break
           title=[]
           company=[]
           location=[]
           for items in link:
              r = requests.get(items)		
              htmlContent = r.content
              soup = BeautifulSoup(htmlContent,'html.parser')
              try:

               title.append(soup.find('div',class_="viewjob-jobTitle h2").text)
              except:
               continue
              try:
               zeug = [y.get_text() for y in soup.find_all('div', attrs={'class': 'viewjob-labelWithIcon'})]
              except:
               title.pop()
               continue
              company.append(zeug[0])
              location.append(zeug[1])
 
           x=len(link)
           if x<=6:
             x=len(link)
           else:
             x=6
           for i in range(0,x):
               y=str(i+1)
               label=tk.Label(self,text=y+"  JOB TITLE:"+title[i],font=("Arial bold",10))
               label.place(x=0,y=80*i)    
               label=tk.Label(self,text=" COMPANY:"+company[i],font=("Arial bold",10))  
               label.place(x=0,y=25+80*i)
               label=tk.Label(self,text="  LOCATION:"+location[i],font=("Arial bold",10))
               label.place(x=0,y=50+80*i)
           #to get the link
           
           for i in range(0,x):
            
               load = Image.open("apply_now.jpg")
               load = load.resize((180,60), Image.ANTIALIAS)
               photo = ImageTk.PhotoImage(load)
               text=link[i]
               button=tk.Button(self,image=photo,text="apply now",command=lambda:openweb(text))
               button.place(x=450,y=80*i)
               button.image=photo
           
           button2= tk.Button(self, text="GO BACK", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))  
           button2.place(x=650, y=450)
    button1= tk.Button(self, text="Back", font=("Arial", 10), command=controller.show_frame(SecondPage))  
    button1.place(x=650, y=450)
    save = tk.Button(self, text = 'search',command=simply_hired_result)
    save.place(x=370,y=330)

class indeed(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.configure(bg='white')
    load = Image.open("indeed.jpg")
        #1800 x 950
    x=400
    y=200
    load = load.resize((x,y), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    label1= tk.Label(self, image=photo)
    label1.image=photo
    label1.place(x=200,y=0)
        
        

        
        
    label2=tk.Label(self,text="Job title:  ",font=("Arial bold",12))
    label2.place(x=20,y=220)
        
    label3=tk.Label(self,text="Location:",font=("Arial bold",12))
    label3.place(x=20,y=260)

        
        
    entry1 =tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
    entry1.place(x=110,y=223)
    entry1.insert(0,"")
        
        

        
    entry2=tk.Entry(self,bg="white",width=50,justify="left",highlightcolor="white",cursor="xterm white")
    entry2.place(x=110,y=263)
    entry2.insert(0,"")
    

    def indeed_result():
           
           job_search=entry1.get()
           job_search=job_search.replace(" ","+")
           location=entry2.get()
           location=location.replace(" ","+")
           label1.destroy()
           label2.destroy()
           label3.destroy()
           entry1.destroy()
           entry2.destroy()
           save.destroy()
           button1.destroy()
           
      
           self.configure(bg="light blue")
          
           
           
           url="https://in.indeed.com"
           url_S=(f"https://in.indeed.com/jobs?q={job_search}&l={location}")
           r = requests.get(url_S)		# r variable has all the HTML code
           htmlContent = r.content
           soup = BeautifulSoup(htmlContent,'html.parser')
           div1=soup.find_all('div',class_='jobsearch-SerpJobCard')
           post=[]
           company=[]
           place=[]
           for items in div1:#every variable has been tried for non::atribute error
             try:
                  post.append(items.find('h2').text)
             except:
                  
                  continue
                  
             try:  
                  
                  company.append(items.find('span',class_="company").text)
                  
             except:
                  post.pop()
                  continue
       
             try:  
                place.append(items.find('span',class_="location accessible-contrast-color-location").text)
             except:
                post.pop()
                company.pop()
                continue
           
           link=[]
           site="https://in.indeed.com/"
           #using array index system return the direct link to selected job offers
           div2=soup.find_all('a',class_="jobtitle turnstileLink")
           for items in div2:
             link.append(site+items.get('href'))
 
           x=len(post)
           if x<=6:
              x=len(post)
           else:
              x=6
          
           for i in range(0,x):
               y=str(i+1)
               
               labelx=tk.Label(self,text=y+"  JOB TITLE:"+(post[i].replace("\n"," ")),font=("Arial bold",10))
               labelx.place(x=0,y=80*i)    
               labely=tk.Label(self,text=" COMPANY:"+company[i].replace("\n"," "),font=("Arial bold",10))  
               labely.place(x=0,y=25+80*i)
               labelz=tk.Label(self,text="  LOCATION:"+place[i].replace("\n"," "),font=("Arial bold",10))
               labelz.place(x=0,y=50+80*i)
            #to get the link
           
           for i in range(0,x):
            
               load = Image.open("apply_now.jpg")
               load = load.resize((180,60), Image.ANTIALIAS)
               photo = ImageTk.PhotoImage(load)
               text=link[i]
               button=tk.Button(self,image=photo,text="apply now",command=lambda:openweb(text))
               button.place(x=450,y=80*i)
               button.image=photo
           
           button2= tk.Button(self, text="GO BACK", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))  
           button2.place(x=650, y=450)
    button1= tk.Button(self, text="Back", font=("Arial", 10), command=lambda:controller.show_frame(SecondPage))  
    button1.place(x=650, y=450)
    save = tk.Button(self, text = 'search',command=indeed_result)
    save.place(x=370,y=330)

    


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, google,linkedin,letsintern,simply_hired,indeed):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        
        
        self.show_frame(FirstPage)
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")

 
app = Application()
app.title("career-wise")
app.maxsize(800,500)
app.mainloop()