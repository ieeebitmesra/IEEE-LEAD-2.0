import webbrowser
import mechanicalsoup


def indeed_scraper():
    # job_type = input("What type of job are your seeking: ")
    # job_location = input("Where do you want to work: ")

    job_type = "Financial Analyst"
    # "Financial Analyst"
    job_location = "India"

    base_url = "https://in.indeed.com/"
    browser = mechanicalsoup.Browser()

    home_page = browser.get(base_url)
    home_page_html = home_page.soup

    job_form = home_page_html.find_all("form")[0]

    job_what_input = job_form.select("input")[0]
    job_where_input = job_form.select("input")[1]

    # print(job_what_input)
    # print(job_where_input)

    job_what_input["value"] = job_type
    job_where_input["value"] = job_location

    jobs_page = browser.submit(job_form, home_page.url)
    jobs_page_html = jobs_page.soup

    job_post_list = []

    get_jobs = 5
    for post in jobs_page_html.find_all("div", class_="jobsearch-SerpJobCard"):
        if get_jobs == 0:
            break
        # print(post)
        title_a_tag = post.find_all("a", class_="jobtitle")
        open_card = title_a_tag[0]["id"]
        if not open_card.startswith("jl_"):
            continue
        # print(open_card)
        job_type_url = "%20".join(job_type.split())
        card_section_url = f"https://in.indeed.com/jobs?q={job_type_url}&l={job_location}&vjk={open_card[3:]}"
        # card_open_page = browser.get(card_section_url)
        # card_section_url = base_url[:-1] + title_a_tag[0]["href"]
        # card_open_page = browser.get(card_section_url)
        # card_open_html = card_open_page.soup
        # print(card_open_html)
        # print(card_open_page.url)
        # print(card_open_page.soup.find_all("table", id_="resultsBody"))
        # card_section = card_open_page.soup.find_all("div", id_="apply-button-container")
        # print(card_section)
        # card_apply_anchor = card_open_page.soup.find_all("a", class_="view-apply-button")[0]["href"]
        # print(card_apply_anchor)
        get_jobs -= 1
        company_span = post.find_all("span", class_="company")[0]
        job_title = title_a_tag[0]["title"].strip()
        company_name = company_span.text.strip()
        try:
            location_span = post.find_all("div", class_="location")
            location = location_span[0].text
            # print(location)
        except IndexError:
            try:
                location_span = post.find_all("span", class_="location")
                location = location_span[0].text
                # print(location)
            except IndexError:
                location = "Unknown Location"
                # print("Unknown Location")

        rating_a_tag = post.find_all("span", class_="ratingsContent")
        try:
            rating = rating_a_tag[0].text
        except IndexError:
            rating = -1

        # print(rating)
        job_post_list.append([job_title, company_name, location, card_section_url, float(rating)])

    def sort_custom(job):
        return job[4]

    job_post_list.sort(key=sort_custom, reverse=True)
    for job_post in job_post_list:
        for i in range(4):
            print(job_post[i])
        if job_post[4] == -1:
            print("UNRATED")
        else:
            print(job_post[4])

    if get_jobs == 5:
        print("No Results Found")


indeed_scraper()
