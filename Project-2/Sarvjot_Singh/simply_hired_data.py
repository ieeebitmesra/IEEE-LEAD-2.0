import mechanicalsoup
from bs4 import BeautifulSoup

def sh_fun(job_name, job_location):

    simply_hired_url = "https://www.simplyhired.co.in"
    # job_name = "Financial Analyst"
    # job_location = "India"

    browser = mechanicalsoup.StatefulBrowser()

    page = browser.get(simply_hired_url)
    soup = page.soup


    form = soup.find_all("form")[0]

    what_input = form.select("#SearchForm-whatInput")[0]
    where_input = form.select("#SearchForm-whereInput")[0]

    what_input["value"] = job_name
    where_input["value"] = job_location

    final_html = browser.submit(form, page.url)
    final_soup = BeautifulSoup(final_html.text, "html.parser")

    # print(final_soup.prettify())

    # job titles and links

    job_titles_a = final_soup.find_all("a", class_="SerpJob-link")
    titles = []
    links = []

    for title_a in job_titles_a:
        title = title_a.text
        link = title_a["href"]
        link = simply_hired_url+link
        titles.append(title)
        links.append(link)

    # company name
    company_list = final_soup.find_all("span", class_="jobposting-company")
    company = []

    for comp in company_list:
        company_name = comp.text
        company.append(company_name)

    # company location

    location_list = final_soup.find_all(
        "span", class_="JobPosting-labelWithIcon jobposting-location")
    location = []

    for loc in location_list:
        company_location = loc.text
        location.append(company_location)

    simply_hired_obj = {
        'titles' : titles,
        'company' : company,
        'location' : location,
        'links' : links
    }

    return simply_hired_obj

    # https://www.uber.com/careers/list/102947/?rx_campaign=indeed22&rx_group=124698&rx_job=102947&rx_r=none&rx_source=Indeed&rx_ts=20210512T055126Z&iis=marketing&iisn=indeed&iisp=organic&rx_viewer=20df04e5b2ea11eb890931dce5552136ac852a55d31445f7bc0c2440efb03d57
    # Associate Risk Analyst I
    # Uber
    ## Hyderabad, Telangana
