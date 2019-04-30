from django.db import models
from django_countries import countries


class LinkedinQuery(models.Model):
    """
    A Model for storing the Queries created through the form to scrape linkedin
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=200,choices=([(country.name,country.name)
                                                        for country in countries]))
    company = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.company


class LinkedinContacts(models.Model):
    """
    A Model for string the scraped contacts from queries
    """
    query = models.ForeignKey(LinkedinQuery,on_delete=models.CASCADE,related_name="contacts")
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
