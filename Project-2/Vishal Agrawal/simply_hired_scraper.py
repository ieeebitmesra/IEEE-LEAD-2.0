import mechanicalsoup
import re


def simply_hire():
    browser = mechanicalsoup.Browser()
    url = "https://www.simplyhired.co.in"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    job_type = "Financial Analyst"
    # "Financial Analyst"
    job_location = "India"

    home_page = browser.get(url=url, headers=headers)
    home_page_html = home_page.soup

    job_form = home_page_html.find_all("form")[0]

    job_what_input = job_form.select("input")[1]
    job_where_input = job_form.select("input")[2]

    # for input_job in job_form.select("input"):
    #     print(input_job)

    # print(job_form)

    job_what_input["value"] = job_type
    job_where_input["value"] = job_location

    jobs_page = browser.submit(job_form, home_page.url)
    # print(jobs_page.url)
    jobs_page_html = jobs_page.soup

    post_count = 1
    for article in jobs_page_html.select("article", class_="SerpJob"):
        if post_count > 5:
            break
        anchor_tag = article.select("a")[0]
        card_link = anchor_tag["href"]
        position_name = anchor_tag.text

        card_complete_link = url + card_link
        card = browser.get(url=card_complete_link, headers=headers)
        card_html = card.soup
        div_tag = card_html.find_all("div", class_="viewjob-labelWithIcon")
        apply_button = card_html.find_all("a", class_="btn-apply")
        apply_link = url + apply_button[0]["href"]
        apply_link_open = browser.get(url=apply_link, headers=headers)
        final_link = apply_link_open.url
        company_name = div_tag[0].text
        company_name_regex = re.search("(.*?) - ", company_name)[0]
        company_name = company_name_regex[:len(company_name_regex) - 2]
        location_name = div_tag[1].text
        post_count += 1

        print(final_link)
        print(position_name)
        print(company_name)
        print(location_name)
        print()
    if post_count == 1:
        print("No Results Found")


simply_hire()
