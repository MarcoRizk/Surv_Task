import unittest
from selenium import webdriver
from django.test import  TestCase
from .models import LinkedinQuery, LinkedinContacts


# models test
class ModelTests(TestCase):
    """LinkedinQuery Model"""
    # Testing model instance creation
    def create_Linkedin_Query(self, country = "Egypt", company = "Surv", department = "Engineering"):
        return LinkedinQuery.objects.create(country=country,company=company,department=department)

    # Testing the created object
    def test_Linkedin_Query_creation(self):
        query = self.create_Linkedin_Query()
        self.assertTrue(isinstance(query, LinkedinQuery))
        self.assertEqual(query.__str__(), query.company)

    """LinkedinContacts Model"""

    # Testing model instance creation

    def create_Linkedin_Contacts(self, name="Marco", url="https://google.com"):
        query = self.create_Linkedin_Query()
        return LinkedinContacts.objects.create(query=query, name=name, url=url)

    # Testing the created object
    def test_Linkedin_Contacts_creation(self):
        contact = self.create_Linkedin_Contacts()
        self.assertTrue(isinstance(contact, LinkedinContacts))
        self.assertEqual(contact.__str__(), contact.name)


# testing workflow using Selenium

class TestingWorkFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_linkedin_scraping(self):
        self.driver.get("http://localhost:8000/linkedin-scrapper")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("country").send_keys("Egypt")
        self.driver.find_element_by_name("company").send_keys("SLB")
        self.driver.find_element_by_name("department").send_keys("Engineering")
        self.driver.find_element_by_name('submit').click()
        self.assertIn("http://localhost:8000/linkedin-scrapper/contacts/", self.driver.current_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('submit').click()
        self.assertIn("http://localhost:8000/linkedin-scrapper/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
