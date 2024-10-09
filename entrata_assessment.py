import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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


def test_accept_cookies(driver):
    driver = driver
    driver.get("https://www.entrata.com")
    driver.maximize_window()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()


def test_schedule_your_demo_navigation(driver):
    driver.get("https://www.entrata.com/")
    driver.maximize_window()
    button_schedule_your_demo = "/html/body/section[1]/div[1]/div/div/div[2]/a"
    driver.find_element(By.XPATH, button_schedule_your_demo).click()
    driver.switch_to.window(driver.window_handles[1])

    # Verify the URL of the new tab
    expected_url = 'https://go.entrata.com/schedule-demo.html'
    assert driver.current_url == expected_url, "URL did not match!"

    # Verify the title of the new tab
    expected_title = "Entrata | Property Management the Way It Should Be"
    assert driver.title == expected_title, "Title did not match!"

    xpath_first_name = "FirstName"
    xpath_last_name = "LastName"
    xpath_email = "Email"
    xpath_company_name = "Company"
    xpath_phone_number = "Phone"
    xpath_unit_count = "Unit_Count__c"
    xpath_job_title = "Title"
    xpath_demo_request = "demoRequest"
    xpath_submit_watchdemo = "mktoForm_1108"

    first_name_field = driver.find_element(By.ID, xpath_first_name)
    last_name_field = driver.find_element(By.ID, xpath_last_name)
    email_field = driver.find_element(By.ID, xpath_email)
    company_name_field = driver.find_element(By.ID, xpath_company_name)
    phone_number_field = driver.find_element(By.ID, xpath_phone_number)
    job_title_field = driver.find_element(By.ID, xpath_job_title)
    unit_count_field = driver.find_element(By.ID, xpath_unit_count)
    demo_request_field = driver.find_element(By.ID, xpath_demo_request)
    submit_watchdemo_button = driver.find_element((By.ID, xpath_submit_watchdemo))

    fields = [first_name_field, last_name_field, email_field, company_name_field, phone_number_field, job_title_field,
              unit_count_field, demo_request_field, submit_watchdemo_button]

    for field_id in fields:
        try:
            element = driver.find_element(By.ID, field_id)
            assert element.is_displayed(), f"{field_id} is not displayed"
            print(f"{field_id} is present.")
        except NoSuchElementException:
            print(f"{field_id} not found.")


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
    check_watchdemo_is_present = driver.find_element(By.ID, xpath_submit_watchdemo)
    assert check_watchdemo_is_present.is_displayed()
