from tkinter import *
import tkinter.font
from tkinter import messagebox
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
from PIL import Image, ImageTk


WIDTH = 900
HEIGHT = 700

# functions


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # to not open the browser on runtime
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver


def google_search(job):
    try:
        if entry.get() == '':
            messagebox.showinfo('Help', 'Try using the search box')
            return None

        messagebox.showinfo('Loading', 'Please wait....parsing information')

        url = 'https://www.google.com/search?q=' + job
        url = url.replace(' ', '+')

        driver = setup_driver()
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        tag = soup.find('div', id='rso')

        site = []
        flag = 0

        for i in tag.contents:

            if i.has_attr('class'):

                if i['class'] == 'ULSxyf':
                    continue

                if i.a['href'][:5] != 'https':
                    continue

                site.append({'link': i.a['href'], 'name': i.h3.text})

        driver.quit()

        return site

    except:
        messagebox.showwarning('Warning', 'Please enter valid input!')
        error()
        raise


def link():
    loading_screen()
    return google_search(entry.get() + ' job')


def output(site, page):
    if site is None:
        return None

    if page < 0:
        page = len(site) - 1

    if page == len(site):
        page = 0

    clear_frame(outputFrame)

    link_ = site[page]['link']
    name = site[page]['name']

    site_name = Label(outputFrame, text=name, font=font16b, wraplength=450, justify=LEFT, fg='#4287f5')
    site_name.place(relwidth=0.8, rely=0.1, relx=0.1)

    print_url = Label(outputFrame, wraplength=450, text=f'URL: {link_}', font=font14, justify=LEFT, fg='#333')
    print_url.place(relwidth=0.8, rely=0.4, relx=0.1)

    visit_frame = Frame(outputFrame, bg='#fff')
    visit_btn = Button(visit_frame, text='Visit', bd=0, bg='#ddd', fg='#222', font=font14,
                       command=lambda: open_browser(link_))

    copy_frame = Frame(outputFrame, bg='#fff')
    copy_to_clip = Button(copy_frame, text='Copy URL', bd=0, bg='#ddd', fg='#222', font=font14,
                          command=lambda: copy(link_))

    visit_frame.place(relx=0.85, rely=0.88, relwidth=0.2, anchor='ne')
    visit_btn.pack(fill='x')

    copy_frame.place(relx=0.15, rely=0.88, relwidth=0.2)
    copy_to_clip.pack()

    pg_frame = Frame(outputFrame, bg='#fff')
    pg_indicator = Button(pg_frame, text=f'{page + 1}/{len(site)}', bd=0, bg='#eee', fg='#222', font=font14)
    pg_frame.place(relx=0.45, rely=0.88, relwidth=0.1)
    pg_indicator.pack(fill='both')

    back_btn = Button(outputFrame, text='(', bd=0, relief=GROOVE, fg='#222', bg='#ddd', font=font14b,
                      command=lambda: output(site, page - 1))
    back_btn.place(relheight=1)

    next_btn = Button(outputFrame, text=')', bd=0, relief=GROOVE, fg='#222', bg='#ddd', font=font14b,
                      command=lambda: output(site, page + 1))
    next_btn.place(relheight=1, relx=1, anchor='ne')


def open_browser(url):
    webbrowser.open(url)


def loading_screen():
    if entry.get() == '':
        return None
    clear_frame(outputFrame)
    loading = Label(outputFrame, text='Searching for your dream job...', font=font22, bg='#fff')
    loading.place(anchor='center', relx=0.5, rely=0.5)


def error():
    clear_frame(outputFrame)
    loading = Label(outputFrame, text='Error occured :(', font=font22, bg='#fff')
    loading.place(anchor='center', relx=0.5, rely=0.5)


def copy(url):
    root.clipboard_clear()
    root.clipboard_append(url)

    messagebox.showinfo('Success', 'URL copied to clipboard')


def clear_frame(widget):
    for w in widget.winfo_children():
        w.destroy()


def quitprg():
    response = messagebox.askokcancel('Quit Program', 'Are you sure you want to quit?')
    if response:
        root.quit()


def about():
    clear_frame(outputFrame)

    about_head = Label(outputFrame, text='About Me', font=font22, bg='#fff', fg='#222')
    about_head.place(relx=0.05, relwidth=0.9, rely=0.03)

    about_info = 'Hey, my name is Shivam Kumar. Currently am a first year undergrad student at ' \
                 'BIT Mesra pursuing major in Computer Science and Engineering.\n\n' \
                 'This app is made using the tkinter library of python. For more info ' \
                 'or any doubt contact me via my email (shivamx6174@gmail.com).'
    about = Label(outputFrame, text=about_info, wraplength=500, bg='#fff', fg='#333', font=font18, justify=LEFT, anchor='w')
    about.place(relwidth=0.9, relx=0.05, rely=0.2)

# -------------------------Website scrape functions----------------------#

def show_websites():
    clear_frame(outputFrame)

    output_lb = Label(outputFrame, text='Skrim the following sites', bg='#fff', fg='#333', bd=0, font=font18)
    output_lb.place(relx=0.05, relwidth=0.9, rely=0.02)

    naukri_btn = Button(outputFrame, text='Naukri.com', font=font20, bg='#ddd', fg='#222',
                        command=lambda: details_pane(naukri(entry.get()), 'naukri.com'), bd=0)
    naukri_btn.place(relheight=0.16, relwidth=0.4, rely=0.2, relx=0.05)

    linkedin_btn = Button(outputFrame, text='Linkedin', font=font20, bg='#ddd', fg='#222',
                          command=lambda: details_pane(linkedin(entry.get()), 'LinkedIn'), bd=0)
    linkedin_btn.place(relheight=0.16, relwidth=0.4, rely=0.5, relx=0.95, anchor='ne')

    monster_btn = Button(outputFrame, text='Monster Jobs', font=font20, bg='#ddd', fg='#222',
                         command=lambda: details_pane(monster(entry.get()), 'monsterindia.com'), bd=0)
    monster_btn.place(relheight=0.16, relwidth=0.4, rely=0.8, relx=0.05)


def details_pane(job_details, title):
    if job_details == 1:
        return None

    clear_frame(outputFrame)

    window = Toplevel(height=HEIGHT, width=WIDTH, bg='#fff')
    window.iconbitmap('graphics/icon.ico')
    window.title(title)
    window.resizable(0, 0)

    w_img = Image.open('graphics/bg.png').resize((WIDTH, HEIGHT))
    w_imgt = ImageTk.PhotoImage(w_img)
    w_bg = Label(window, image=w_imgt)
    w_bg.place(relwidth=1, relheight=1, relx=0, rely=0)

    w_heading = Label(window, text=title, bg='#fff', fg='#036ffc', font=font32)
    w_heading.place(relwidth=1)

    details = Frame(window, bg='#eee')
    details.place(relwidth=0.95, rely=0.15, relx=0.025, relheight=0.82)

    job_frame = Frame(details, bg='#eee')
    job_frame.place(relwidth=1, relheight=1)

    # Job Details

    global page_
    page_ = 0

    def print_job(pg_=0):
        if pg_ == len(job_details):
            pg_ = 0
        if pg_ < 0:
            pg_ = len(job_details) - 1

        w_pgno = Button(details, text=f'{pg_ + 1}/{len(job_details)}', bd=0, bg='#eee', font=font16)
        w_pgno.place(relheight=0.08, relwidth=0.15, relx=0.425, rely=0.85)

        global page_
        page_ = pg_

        clear_frame(job_frame)

        apply = Button(job_frame, text=f'Apply Now', bd=0, bg='#317df5', fg='#fff', font=font16,
                       command=lambda: webbrowser.open(job['link']))
        apply.place(relheight=0.08, relwidth=0.3, relx=0.35, rely=0.75)

        job = job_details[pg_]
        job_title = job['title']
        job_title = Label(job_frame, text=job_title, font=font22, bg='#eee', fg='blue', wraplength=800)
        job_title.place(relwidth=1, rely=0.07)

        starty = 0.3

        for key in job:
            if key == 'title':
                continue

            if job[key] == 'NA' or key == 'link':
                continue

            value = job[key]
            item = Label(job_frame, text=f'{key.upper()}:  {value}', font=font14, bg='#eee', fg='#333',
                         wraplength=800, justify=LEFT, anchor='w')
            item.place(rely=starty, relwidth=0.95, relx=0.05)
            starty += 0.05

    print_job(page_)

    back_job = Button(details, text='Back', bd=0, bg='#bbb', font=font16, command=lambda: print_job(page_ - 1))
    back_job.place(relheight=0.08, relwidth=0.1, relx=0.05, rely=0.85)
    next_job = Button(details, text='Next', bd=0, bg='#bbb', font=font16, command=lambda: print_job(page_ + 1))
    next_job.place(relheight=0.08, relwidth=0.1, relx=0.95, rely=0.85, anchor='ne')

    window.mainloop()


# ----------------------------------- WEBSITES ---------------------------------#


def linkedin(job):
    try:
        loading_screen()
        messagebox.showinfo('Loading', 'Parsing structure... This process may take some time. Please remain patient. Press OK to continue')

        url = 'https://in.linkedin.com/jobs/' + job + '-jobs'
        url = url.replace(' ', '-')
        driver = setup_driver()
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')

        tags = soup.find(class_='jobs-search__results-list')

        job_info = []

        for i in tags.contents:
            link_t = i.select_one('a')
            title_t = i.select_one('.result-card__title')
            subtitle_t = i.select_one('.result-card__subtitle')
            location_t = i.select_one('.job-result-card__location')
            status_t = i.select_one('.result-benefits__text')

            company = location = status = title = link_ = 'NA'

            if title_t:
                title = title_t.get_text()
            if subtitle_t:
                company = subtitle_t.get_text()
            if location_t:
                location = location_t.get_text()
            if status_t:
                status = status_t.get_text()
            if link_t:
                link_ = link_t['href']

            job_info.append({'title': title, 'company': company, 'location': location, 'status': status, 'link': link_})

        driver.quit()
        return job_info

    except:
        error()
        messagebox.showinfo('Invalid input', 'Invalid input detected. Try inputting a valid query.')
        return 1


def monster(job):

    try:

        loading_screen()
        messagebox.showinfo('Loading', 'Parsing structure... This process may take some time. '
                                       'Please remain patient. Press OK to continue')
        url = 'https://www.monsterindia.com/search/' + job + '-jobs'
        url = url.replace(' ', '-')
        driver = setup_driver()
        driver.get(url)
        # webbrowser.open(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        tags = soup.find_all(class_='card-apply-content')

        job_info = []

        for i in tags:
            title_ = i.select_one('.job-tittle h3 a')
            company_ = i.select_one('.company-name a')
            location_ = i.select_one('.mqfi-location-v2 + small')
            exp_ = i.select_one('.exp .loc small')
            skills_ = i.select('.descrip-skills .grey-link a')
            salary_ = i.select_one('.package .loc small')

            salary = ln = skills = exp = location = title = company = 'NA'

            if title_:
                title = title_.get_text()
                ln = title_['href']

            if company_:
                company = company_.get_text()

            if location_:
                t_st = location_.get_text()
                t_st = t_st.replace(',', ' ')
                t_st = t_st.strip()
                location = t_st

            if exp_:
                exp = exp_.get_text().strip()

            if skills_:
                for sk in skills_:
                    st = sk.get_text()
                    st = st.replace(',', ' ')
                    st = st.strip()

                    if skills == 'NA':
                        skills = st
                    else:
                        skills += ', ' + st

            if salary_:
                salary = salary_.get_text().strip()

            job_info.append({'title': title, 'company': company, 'location': location, 'experience': exp,
                             'salary': salary, 'skills': skills, 'link': ln})

        driver.quit()
        return job_info

    except:
        error()
        messagebox.showinfo('Invalid input', 'Invalid input detected. Try inputting a valid query.')
        return 1


def naukri(job):
    try:
        loading_screen()
        messagebox.showinfo('Loading', 'Parsing structure... This process may take some time. '
                                       'Please remain patient. Press OK to continue')
        url = 'https://www.naukri.com/' + job + '-jobs'
        url = url.replace(' ', '-')

        driver = setup_driver()
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')

        tags = soup.find('div', class_='list')

        job_info = []

        for i in tags.contents:
            if i.has_attr('class'):
                if i['class'][0] == 'jobTuple':
                    t = i.select_one('.title')
                    s = i.select_one('.subTitle')
                    star = i.select_one('.starRating')
                    rev = i.select_one('.reviewsCount')
                    exp = i.select_one('.experience span')
                    sal = i.select_one('.salary span')
                    loc = i.select_one('.location span')
                    skill_t = i.select('.has-description li')
                    star_rating = title = subtitle = reviews = salary = location = experience = 'NA'
                    skills = ''

                    if t:                           # checking if title variable is an empty list or not
                        title = t.get_text()
                    if s:
                        subtitle = s.get_text()
                    if star:
                        star_rating = star.get_text()
                    if rev:
                        reviews = rev.get_text()
                    if exp:
                        experience = exp.get_text()
                    if loc:
                        location = loc.get_text()
                    if sal:
                        salary = sal.get_text()
                    if skill_t:
                        for skill in skill_t:
                            if skills == '':
                                skills += skill.get_text()
                            else:
                                skills += ', ' + skill.get_text()

                    job_info.append({'title': title, 'company': subtitle, 'ratings': star_rating, 'reviews': reviews,
                                     'salary': salary, 'location': location, 'experience': experience, 'skills': skills})

        # print(job_info)
        driver.quit()
        return job_info

    except:
        error()
        messagebox.showinfo('Invalid input', 'Invalid input detected. Try inputting a valid query.')
        return 1

# ----------------------------------------------------------------------------- #


# root properties

root = Tk()
root.title('Job Search')
root.iconbitmap('graphics/icon.ico')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(0, 0)

# fonts

font32 = tkinter.font.Font(family='century gothic', size=32, weight='bold')
font12 = tkinter.font.Font(family='century gothic', size=12)
font14 = tkinter.font.Font(family='century gothic', size=14)
font14b = tkinter.font.Font(family='century gothic', size=14, weight='bold')
font16 = tkinter.font.Font(family='century gothic', size=16)
font16b = tkinter.font.Font(family='century gothic', size=17, weight='bold')
font18 = tkinter.font.Font(family='century gothic', size=18)
font20 = tkinter.font.Font(family='century gothic', size=20)
font22 = tkinter.font.Font(family='century gothic', size=22)

# main frame

main_frame = Frame(root, height=HEIGHT, width=WIDTH, bd=0)
main_frame.pack()

# background Image

bgImg = Image.open('graphics/bg.png')
bgImg = bgImg.resize((WIDTH, HEIGHT))
bgImgT = ImageTk.PhotoImage(bgImg)

bg = Label(main_frame, image=bgImgT)
bg.place(relwidth=1, relheight=1, relx=0, rely=0)

# heading

headingFrame = Frame(main_frame, bg='#1056c7')
headingFrame.place(anchor='center', relx=0.5, rely=0.1)

headingImg = ImageTk.PhotoImage(Image.open('graphics/heading.png'))
heading = Label(headingFrame, image=headingImg)
heading.pack(padx=7, pady=1)

# Search Box

entry_frame = Frame(main_frame, height=50)
entry_frame.place(anchor='center', relx=0.5, rely=0.25, relwidth=0.65)

entry = Entry(entry_frame, font=font16, bd=0, fg='#222')
entry.place(relwidth=0.9, relheight=1)
entry.focus()

searchImgTemp = Image.open('graphics/find.png')
searchImgTemp = searchImgTemp.resize((50, 50))
search_image = ImageTk.PhotoImage(searchImgTemp)

search_icon = Button(entry_frame, image=search_image, bd=0, bg='#f5f5f5', command=lambda: output(link(), 0))
search_icon.place(relwidth=0.1, relheight=1, relx=0.9)

root.bind('<Return>', lambda event=None: search_icon.invoke())

# Buttons

gbFrame = Frame(main_frame, bg='#1056c7')
gbFrame.place(rely=0.4, relx=0.05, relwidth=0.2)

google_btn = Button(gbFrame, text='Google', bd=0, relief=FLAT, fg='#333', bg='#fff', font=font22,
                    command=lambda: output(link(), 0))
google_btn.pack(fill='both', pady=3)

webFrame = Frame(main_frame, bg='#1056c7')
webFrame.place(rely=0.52, relx=0.05, relwidth=0.2)

webBtn = Button(webFrame, text='Websites', font=font22, bd=0, relief=FLAT, fg='#333', bg='#fff',
                command=lambda: show_websites())
webBtn.pack(fill='both', pady=3)

helpFrame = Frame(main_frame, bg='#1056c7')
helpFrame.place(rely=0.64, relx=0.05, relwidth=0.2)

helpBtn = Button(helpFrame, text='About', font=font22, bd=0, relief=FLAT, fg='#333', bg='#fff',
                 command=lambda: about())
helpBtn.pack(fill='both', pady=3)

exitFrame = Frame(main_frame, bg='red')
exitFrame.place(rely=0.85, relx=0.05, relwidth=0.2)

exitBtn = Button(exitFrame, text="Quit", font=font22, bd=0, relief=FLAT, fg='#333', bg='#fff',
                 command=lambda: quitprg())
exitBtn.pack(fill='both', pady=3)

# output frame

outputFrame = Frame(main_frame, bg='#fff')
outputFrame.place(relwidth=0.65, relheight=0.6, relx=0.315, rely=0.35)

home = Image.open('graphics/outputimage.jpg').resize((585, 420))
homeImg = ImageTk.PhotoImage(home)
homeLabel = Label(outputFrame, image=homeImg)
homeLabel.place(relheight=1, relwidth=1)


root.mainloop()
