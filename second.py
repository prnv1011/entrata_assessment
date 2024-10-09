import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    # Setup: Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_homepage_validation(driver):
    driver = driver
    driver.get("https://www.entrata.com")
    driver.maximize_window()
    time.sleep(3)
    # Validate page title
    actual_title = driver.title
    expected_title = "Property Management Software | Entrata"
    assert driver.title == expected_title, f"Expected title: '{expected_title}', but got: '{actual_title}'"


def test_watch_demo(driver):
    driver = driver
    driver.get("https://www.entrata.com")
    time.sleep(3)

    watch_demo = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/nav/div[5]/a[1]/div")
    watch_demo.click()
    time.sleep(3)

    # we will collect all the xpaths here for better dynamics

    xpath_first_name = "FirstName"
    xpath_last_name = "LastName"
    xpath_email = "Email"
    xpath_company_name = "Company"
    xpath_phone_number = "Phone"
    xpath_unit_count = "Unit_Count__c"
    xpath_job_title = "Title"
    xpath_demo_request = "demoRequest"
    xpath_submit_watchdemo = "mktoForm_1108"

    # here we will fill all the fields
    driver.find_element(By.ID, xpath_first_name).send_keys("Pranav")
    driver.find_element(By.ID, xpath_last_name).send_keys("Patil")
    driver.find_element(By.ID, xpath_email).send_keys("testemail@xyz.com")
    driver.find_element(By.ID, xpath_company_name).send_keys("TestCompany")
    driver.find_element(By.ID, xpath_phone_number).send_keys("9876543210")
    driver.find_element(By.ID, xpath_job_title).send_keys("TestJobTitle")

    # for unit count dropdown, we will use select class
    select_unitcount = driver.find_element(By.ID, xpath_unit_count)
    select = Select(select_unitcount)

    # Select an option by visible text
    select.select_by_visible_text("1 - 10")

    # select demo request
    select_demorequest = driver.find_element(By.ID, xpath_demo_request)
    select = Select(select_demorequest)

    # Select an option by visible text
    select.select_by_visible_text("a Resident")

    # since we are told to not submit any forms, we will not click on watch demo but
    print("driver.find_element(By.ID, xpath_submit_watchdemo).click")



# How it works > Watch now > Play video > url verify or play video

# links /a after how it work > open in new tab > verify title

