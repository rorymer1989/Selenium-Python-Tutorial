from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class PageFlight(unittest.TestCase):
    def __init__(self,myDriver):
        self.driver = myDriver

    def select_country_by_index(self,index):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(index)
    def select_country_by_value(self,value):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_value(value)

    def select_country_by_name(self,name):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_visible_text(name)

    def verify_country(self,country):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        assertEquals(countryDropDown.first_selected_option.text.strip(), country)

    def verify_not_country(self,country):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        self.assertNotEquals(countryDropDown.first_selected_option.text.strip(), country)
    #self.assertEquals(countryDropDown.first_selected_option.text.strip(), "CONGO")
    #self.assertNotEquals(countryDropDown.first_selected_option.text.strip(), "ITALY")
    #self.assertTrue(countryDropDown.first_selected_option.text.strip() == "CONGO")
    #self.assertFalse(countryDropDown.first_selected_option.text.strip() == "ARGENTINA")
    #self.assertFalse(countryDropDown.first_selected_option.text.strip() != "CONGO")