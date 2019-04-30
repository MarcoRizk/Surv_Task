# Linkedin Scraper
A simple django app that scrapes google for linkedin contacts through a form

### Workflow
Navigate to /linkedin-scrapper then fill the form that submits the data to the scraper function and retrieves the data in another view with option to save to database

### Important files
**scraper.py:** the script has a function that recieves three input parameters (company, country, department) searches google through "google-search" package, retrieves the top 3 urls, then uses Regex to extract Contact name from the url and returns a list of dictionaries for each user.
