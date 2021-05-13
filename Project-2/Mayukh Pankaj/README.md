
https://user-images.githubusercontent.com/40158577/118137620-083cf600-b423-11eb-95a7-5cb21a617216.mp4

# Woogle - Job & Intern scraping web application 📱

[www.woogles.herokuapp.com](https://woogles.herokuapp.com/) 
  * crashing due to heroku request timeout. 

In this pandemic, searching for job/intern is a tough task, scrolling through different platforms, what if you can have Everything at Once !
Search over 5 platforms, A google for work, Woogle.

web scraping web-app developed for LEAD 2021 organised by IEEE BIT Mesra.

**MILESTONES ACHIEVED**✔️- 
  
    1. Google search results ✔️
    2. Different parameters covered ✔️
          a. job title
          b. company name
          c. company image
          d. location  
          e. job description
          f. application link 
          e. * salary, duration, skill-set when available.
          
    4. 5 platforms scrapped ✔️
          * Google
          * Linkedin
          * Indeed
          * Internshala  
          * Times Job
          
    6. OPTIONAL MILESTONES ✔️ 
          * Flask-Jinja with bootstrap 
          * Hosted on heroku
          * company images 
          * location specific search 
          * results displayed in cards.
          * responsive-material design
          
            

 ## Tech Stack 💻 ##
 
 * Python 
 * Flask + jinja  
 * Beautiful soup 4 
 * Bootstrap 5 
   *Selenium headless for client-side rendered website ( naukri.com)

Python used with BS4 , Flask , requests , WTF form modules.
First user gives job designation / skill & location as input to rendered form. 
User input is passed to 5 functions for each platform like linkedin(input,loc): 

Each function requests search result html document with carefully constructed url 
  * for example https://www.linkedin.com/jobs/search?keywords={{ job }}&location= (( loc }}
  * spaces needs to replaced with ' + ', ' - ', '%20' depending on website.

required elements are filtered out with classnames or id_ names with function soup.select , soup.findall.

element's contents are stored in a dictionary for each job card in results page.
  * example, 
      dataframe = { 'title': job-title,
                    'company':company,
                    'a': link,
                    'img': url,
                   }

Each function then returns a List of Dictionaries containg each job data. 

which is passed to render_template function of results page where it's used to 
recursively display data with help of Jinja with bootstrap cards. 


**UNIQUE 🚀**

Searching for job/intern is a critical situation and needs on the go solution, this is the reason I went for web application, 
instead of downloading the the gui, just logon & use. 

**TAKEAWAYS 🎓 🎓 **

improved python skills
    before using a list of dictionaries , was using a tuple of lists which was bad.
learned webscraping 
    BS4 & selenium.

some new discoveries like,
    html class id's change with change in useragent, so passing headers is necessary for consistent html code.



**IMPROVEMENT 🔍**
* Heroku crashing due to process timeout.

![video](https://storezeo.000webhostapp.com/server/woogle%20v1.mp4)

![woogle homepage](https://i.imgur.com/jxThCQ1.png "woogle home") 
![woogle results](https://i.imgur.com/xkI3g6W.png "woogle results") 
![woogle mobile](https://i.imgur.com/fHS3oip.png "woogle mobile")


https://www.youtube.com/watch?v=92Rc_fnwvFg




