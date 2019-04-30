from django.shortcuts import render,redirect
from .forms import LinkedinQueryForm
from .scraper import scrape_linkedin
from .models import LinkedinQuery,LinkedinContacts


def linkedin_query_view(request):
    """
    creates an empty form to get the query parameters from the user
    (the form only sends GET requests)
    """
    form = LinkedinQueryForm()

    return render(request,"linkedin_scrapper/Query_Form.html",{"form":form})


def get_contacts(request):
    """
    recieves the data from the linkedin query view (GET Request)
    then it performs the web scrapping process and views the results
    has the ability to save the data to DB (POST Request)

    **In case of a bad request it redirects the user to the original query form
    """
    company = request.GET.get('company')
    country = request.GET.get('country')
    department = request.GET.get('department')
    contacts = scrape_linkedin(country, department, company)
    if request.method == 'GET':
        return render(request,"linkedin_scrapper/contacts.html",{"contacts":contacts})

    elif request.method == 'POST':
        query = LinkedinQuery.objects.create(company=company,country=country, department=department)
        for contact in contacts:
            LinkedinContacts.objects.create(query=query,name=contact["name"], url=contact["url"])

        return redirect("linkedin_query")
    else:
        return redirect("linkedin_query")


