from django.urls import path
from .views import get_contacts,linkedin_query_view

urlpatterns = [
    path("",linkedin_query_view, name="linkedin_query"),  # url to initial form for the query
    path("contacts/",get_contacts, name="get_contacts"),  # url for recieved results and save to DB

]
