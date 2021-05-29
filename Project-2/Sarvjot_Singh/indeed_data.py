import mechanicalsoup
from bs4 import BeautifulSoup


def indeed_fun(job_name, job_location):

    indeed_url = "https://in.indeed.com/"

    browser = mechanicalsoup.StatefulBrowser()

    page = browser.get(indeed_url)
    soup = page.soup

    form = soup.find_all("form")[0]

    what_input = form.select("#text-input-what")[0]
    where_input = form.select("#text-input-where")[0]

    what_input["value"] = job_name
    where_input["value"] = job_location

    final_html = browser.submit(form, page.url)
    final_soup = BeautifulSoup(final_html.text, "html.parser")

    # job titles

    job_titles_a = final_soup.find_all("a", class_="jobtitle")
    titles = []

    for title_a in job_titles_a:
        title = title_a["title"]
        titles.append(title)

    # job container

    job_cont = final_soup.find_all("div", class_="sjcl")

    # job rating

    ratings = []

    for cont in job_cont:
        rating_span = cont.select(".ratingsContent")
        if(len(rating_span) != 0):
            rating = rating_span[0].text
            rating = rating.replace("\n", "")
            ratings.append(rating)
        else:
            ratings.append("Unrated")

    # company name

    company = []

    for cont in job_cont:
        company_cont = cont.select(".turnstileLink")
        if(len(company_cont) != 0):
            company_name = company_cont[0].text
            company_name = company_name.replace("\n", "")
            company.append(company_name)
        else:
            company_cont = cont.select(".company")
            company_name = company_cont[0].text
            company_name = company_name.replace("\n", "")
            company.append(company_name)

    # company location

    location = []

    for cont in job_cont:
        location_span = cont.select(".location")
        company_location = location_span[0].text
        company_location = company_location.replace("\n", "")
        location.append(company_location)

    # company vjk/link

    links = []
    link_cont = final_soup.find_all(
        "div", class_="jobsearch-SerpJobCard unifiedRow row result")

    for cont in link_cont:
        vjk = cont["data-jk"]
        link = f"https://in.indeed.com/jobs?q={job_name}&l={job_location}&vjk={vjk}"
        link = link.replace(" ", "%20")
        links.append(link)

    indeed_obj = {
        'titles': titles,
        'ratings': ratings,
        'company': company,
        'location': location,
        'links': links
    }

    return indeed_obj

    # Financial Analyst I
    # HP
    # Bengaluru, Karnataka
    # https://in.indeed.com/jobs?q=financial%20analyst&l=India&vjk=d11c3adfb6e87081
    # 4.0
