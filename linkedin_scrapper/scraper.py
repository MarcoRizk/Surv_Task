from googlesearch import search
import re


def scrape_linkedin(country, department, company):
    """
    Recieves three string inputs (Country,Department,Company) and returns a list of dictionaries
    each corresponds to one of the scraped contacts.
    Returned dictionary has keys ('name','url')
    """
    query_string = "%s AND %s AND %s" % (department, company, country)
    search_results = search(query_string, stop=3, pause=2, domains=["linkedin.com/in/"])
    contacts = []
    for url in search_results:
        extracted = re.search(r'linkedin.com/in/(.*)',url).group(1).split('-')
        name = ""
        if len(extracted) ==1:
            name = extracted[0].capitalize()
        else:
            for name in extracted[:-1]:
                name += name.capitalize() + " "
        contacts.append({'name': name, 'url': url})
    return contacts
