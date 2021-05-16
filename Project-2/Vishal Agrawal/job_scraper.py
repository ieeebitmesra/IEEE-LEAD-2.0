import webbrowser
import re
from functools import partial
from tkinter import *
import mechanicalsoup
from tkinter import ttk

post_frame_list = []
labels_list = []
divided_frame = None
divided_frame_left = None
divided_frame_right = None


def open_link(link):
    webbrowser.open(link)


def no_result_found_right():
    label_no_result = ttk.Label(divided_frame_right, text="No Results Found".upper())
    label_no_result.pack(expand=True, pady=5)
    labels_list.append(label_no_result)


def no_result_found_left():
    label_no_result = ttk.Label(divided_frame_left, text="No Results Found".upper())
    label_no_result.pack(expand=True, pady=5, side="left")
    labels_list.append(label_no_result)


def simply_hire_post(job_post):
    frame_post = ttk.Frame(divided_frame_right, padding="5 5 5 5")
    frame_post['borderwidth'] = 1
    frame_post['relief'] = 'solid'
    post_frame_list.append(frame_post)

    job_title_label = ttk.Label(frame_post, text=f"Job Title : {job_post[0]}".upper())
    job_title_label.pack(expand=True, pady=9)

    job_location_label = ttk.Label(frame_post, text=f"Location : {job_post[2]}".upper())
    job_location_label.pack(expand=True, pady=8)

    company_name_label = ttk.Label(frame_post, text=f"Company Name : {job_post[1]}".upper())
    company_name_label.pack(expand=True, pady=8)

    view_details_button = ttk.Button(frame_post, width=60, text="View Full Details",
                                     command=partial(open_link, job_post[3]))
    view_details_button.pack(expand=True, pady=9)
    frame_post.pack(expand=True, pady=8)


def simply_hired(job_type, job_location):
    browser = mechanicalsoup.Browser()
    url = "https://www.simplyhired.co.in"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    home_page = browser.get(url=url, headers=headers)
    home_page_html = home_page.soup

    job_form = home_page_html.find_all("form")[0]

    job_what_input = job_form.select("input")[1]
    job_where_input = job_form.select("input")[2]

    job_what_input["value"] = job_type
    job_where_input["value"] = job_location

    jobs_page = browser.submit(job_form, home_page.url)
    jobs_page_html = jobs_page.soup

    post_count = 1
    max_jobs = 3

    for article in jobs_page_html.select("article", class_="SerpJob"):
        if post_count > max_jobs:
            break
        anchor_tag = article.select("a")[0]
        card_link = anchor_tag["href"]
        position_name = anchor_tag.text

        card_complete_link = url + card_link
        card = browser.get(url=card_complete_link, headers=headers)
        card_html = card.soup
        div_tag = card_html.find_all("div", class_="viewjob-labelWithIcon")
        apply_button = card_html.find_all("a", class_="btn-apply")
        try:
            apply_link = url + apply_button[0]["href"]
        except IndexError:
            continue
        apply_link_open = browser.get(url=apply_link, headers=headers)
        final_link = apply_link_open.url
        company_name = div_tag[0].text
        company_name_regex = re.search("(.*?) - ", company_name)[0]
        company_name = company_name_regex[:len(company_name_regex) - 2]
        location_name = div_tag[1].text
        post_count += 1

        simply_hire_post_data = [position_name, company_name, location_name, final_link]
        simply_hire_post(simply_hire_post_data)

    if post_count == 1:
        no_result_found_right()


def indeed_post(job_post):
    frame_post = ttk.Frame(divided_frame_left, padding="5 5 5 5")
    frame_post['borderwidth'] = 1
    frame_post['relief'] = 'solid'
    post_frame_list.append(frame_post)

    job_title_label = ttk.Label(frame_post, text=f"Job Title : {job_post[0]}".upper())
    job_title_label.pack(expand=True, pady=5)

    job_location_label = ttk.Label(frame_post, text=f"Location : {job_post[2]}".upper())
    job_location_label.pack(expand=True, pady=5)

    company_name_label = ttk.Label(frame_post, text=f"Company Name : {job_post[1]}".upper())
    company_name_label.pack(expand=True, pady=5)

    rating = job_post[4]
    if rating == -1:
        rating = "UNRATED"

    company_rating_label = ttk.Label(frame_post, text=f"Company Rating : {rating}".upper())
    company_rating_label.pack(expand=True, pady=5)

    view_details_button = ttk.Button(frame_post, width=60, text="View Full Details",
                                     command=partial(open_link, job_post[3]))
    view_details_button.pack(expand=True, pady=5)
    frame_post.pack(expand=True, pady=5)


def indeed_scraper(job_type, job_location):
    base_url = "https://in.indeed.com/"
    browser = mechanicalsoup.Browser()

    home_page = browser.get(base_url)
    home_page_html = home_page.soup

    job_form = home_page_html.find_all("form")[0]

    job_what_input = job_form.select("input")[0]
    job_where_input = job_form.select("input")[1]

    job_what_input["value"] = job_type
    job_where_input["value"] = job_location

    jobs_page = browser.submit(job_form, home_page.url)
    jobs_page_html = jobs_page.soup

    job_post_list = []

    get_jobs = 1
    max_jobs = 3
    
    for post in jobs_page_html.find_all("div", class_="jobsearch-SerpJobCard"):
        if get_jobs > max_jobs:
            break
        title_a_tag = post.find_all("a", class_="jobtitle")
        open_card = title_a_tag[0]["id"]
        if not open_card.startswith("jl_"):
            continue
        job_type_url = "%20".join(job_type.split())
        card_section_url = f"https://in.indeed.com/jobs?q={job_type_url}&l={job_location}&vjk={open_card[3:]}"
        get_jobs += 1
        company_span = post.find_all("span", class_="company")[0]
        job_title = title_a_tag[0]["title"].strip()
        company_name = company_span.text.strip()
        try:
            location_span = post.find_all("div", class_="location")
            location = location_span[0].text
        except IndexError:
            try:
                location_span = post.find_all("span", class_="location")
                location = location_span[0].text
            except IndexError:
                location = "Unknown Location"

        rating_a_tag = post.find_all("span", class_="ratingsContent")
        try:
            rating = rating_a_tag[0].text
        except IndexError:
            rating = -1

        job_post_list.append([job_title, company_name, location, card_section_url, float(rating)])

    def sort_custom(job):
        return job[4]

    job_post_list.sort(key=sort_custom, reverse=True)
    for job_post in job_post_list:
        indeed_post(job_post)

    if get_jobs == 1:
        no_result_found_left()


def clear_screen():
    for label in labels_list:
        label.pack_forget()
        label.destroy()

    for frame_del in post_frame_list:
        frame_del.pack_forget()
        frame_del.destroy()

    labels_list.clear()
    post_frame_list.clear()


def form_submit(*args):
    global divided_frame
    global divided_frame_left
    global divided_frame_right
    clear_screen()
    divided_frame = ttk.Frame(frame, padding="5 5 5 5")
    divided_frame.pack()
    divided_frame_left = ttk.Frame(divided_frame, padding="5 5 5 5")
    divided_frame_right = ttk.Frame(divided_frame, padding="5 5 5 5")
    divided_frame_left.pack(side="left")
    divided_frame_right.pack(side="right")
    post_frame_list.append(divided_frame)
    indeed_label = ttk.Label(divided_frame_left, text="Here are some job post from INDEED".upper())
    indeed_label.pack(expand=True, pady=5)
    indeed_scraper(user_job_title_input.get(), user_job_location_input.get())
    simply_hired_label = ttk.Label(divided_frame_right, text="Here are some job post from Simply Hired".upper())
    simply_hired_label.pack(expand=True, pady=5)
    labels_list.append(indeed_label)
    labels_list.append(simply_hired_label)
    simply_hired(user_job_title_input.get(), user_job_location_input.get())


root = Tk()

root.attributes("-fullscreen", True)

root.title("Job Search")

# size_x = 2000
# size_y = 2000
# spawn_x = 0
# spawn_y = 0
# root.wm_geometry(f"{size_x}x{size_y}+{spawn_x}+{spawn_y}")


frame = ttk.Frame(root, padding="20 20 20 20")
frame.pack(fill=Y)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label_input_1 = ttk.Label(frame, text="what type of job, are you looking for? (e.g. Software Developer)".upper())
label_input_1.pack(expand=True, pady=5)

user_job_title_input = StringVar()

user_job_title_widget = ttk.Entry(frame, width=70, justify='center',
                                  textvariable=user_job_title_input)

user_job_title_widget.pack(expand=True, pady=5)

label_input_2 = ttk.Label(frame, text="which city/country do you want the job to be in? (e.g. Ranchi)".upper())
label_input_2.pack(expand=True, pady=5)

user_job_location_input = StringVar()

user_job_location_widget = ttk.Entry(frame, width=70, justify='center',
                                     textvariable=user_job_location_input)

user_job_location_widget.pack(expand=True, pady=5)

submit_button = ttk.Button(frame, text="Search", command=form_submit)

submit_button.pack(expand=True, pady=5)

user_job_title_widget.focus()

root.bind('<Return>', form_submit)

root.mainloop()
