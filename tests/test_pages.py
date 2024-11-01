"""
test_pages.py

This module contains test cases for the Orange HRM login and PIM functionalities
using the pytest framework. It utilizes the Page Object Model (POM) design pattern
to separate the page interactions from the test logic, enhancing code organization
and maintainability.

Usage:
    To run the tests, execute the pytest command on this file. The tests will verify
    login capabilities, check for valid and invalid credentials, and ensure proper
    navigation within the PIM module.
"""

import pytest
import pandas as pd
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from datetime import datetime
from data.data_generators import generate_random_name, generate_random_employee_id

# Load login credentials from CSV
def load_login_data():
    """Loads login data from a CSV file."""
    print("Loading login data from CSV...")
    return pd.read_csv("data/login_data.csv")

# Set up the source URL for the application
src_url = "https://opensource-demo.orangehrmlive.com/"

# Screenshot utility with timestamp
def capture_screenshot(driver, prefix):
    """Captures a screenshot with a timestamp."""
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)  # Create screenshots directory if it doesn't exist
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Generate a timestamp for uniqueness
    screenshot_path = os.path.join(screenshot_dir, f"{prefix}_{timestamp}.png")  # Define screenshot path
    driver.save_screenshot(screenshot_path)  # Save screenshot
    print(f"Screenshot saved at: {screenshot_path}")  # Log the screenshot path

@pytest.fixture(scope="function")
def driver():
    """Sets up and tears down the Chrome driver for each test."""
    print("Setting up the Chrome driver...")
    driver = webdriver.Chrome()  # Initialize the Chrome driver
    driver.get(src_url)  # Navigate to the source URL
    print("Navigated to the source URL.")
    yield driver  # Yield the driver for use in tests
    print("Quitting the driver...")
    driver.quit()  # Clean up and close the driver
 """
 <--------------------------------------------Login module starts------------------------------------------------------>
 
                    Test case 1: Login with valid credentials
                    Test case 2: Login with invalid credentials and capture error message
 """

# Test case 1: Login with valid credentials
def test_login_with_valid_credentials(driver):
    """Tests the login functionality with valid credentials."""
    login_data = load_login_data()  # Load login data
    valid_data = login_data[login_data['expected'] == 'pass'].iloc[0]  # Get valid data
    username, password = valid_data['username'], valid_data['password']  # Extract credentials

    print(f"Logging in with username: {username} and password: {password}")
    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(username, password)  # Perform login

    assert login_page.is_logged_in(), f"Login failed for {username}"  # Verify login success
    print("Login successful.")
    capture_screenshot(driver, "login_success")  # Capture screenshot of successful login

# Test case 2: Login with invalid credentials and capture error message
def test_login_with_invalid_credentials(driver):
    """Tests the login functionality with invalid credentials."""
    login_data = load_login_data()  # Load login data
    invalid_data = login_data[login_data['expected'] == 'fail'].iloc[0]  # Get invalid data
    username, password = invalid_data['username'], invalid_data['password']  # Extract credentials

    print(f"Attempting to login with invalid username: {username} and password: {password}")
    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(username, password)  # Attempt login

    wait = WebDriverWait(driver, 10)  # Create WebDriverWait for explicit waits
    error_message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
    ).text  # Wait for the error message to be visible

    print(f"Received error message: {error_message}")
    assert error_message == "Invalid credentials", "Unexpected error message"  # Validate the error message
    capture_screenshot(driver, "invalid_credentials")  # Capture screenshot of the error
"""
 <--------------------------------------------Login module ends-------------------------------------------------------->

 <--------------------------------------------PIM module starts-------------------------------------------------------->
 
                    Test case 1: Login, navigate to PIM, and add employee
                    Test case 2: Login, navigate to PIM, and update employee details
                    Test case 3: Login, navigate to PIM, and delete an employee detail
"""
# Test case 1: Login, navigate to PIM, and add employee
def test_add_employee(driver):
    """Tests the addition of an employee after a successful login."""
    login_data = load_login_data()  # Load login data
    valid_username = login_data[login_data['expected'] == 'pass'].iloc[0]['username']
    valid_password = login_data[login_data['expected'] == 'pass'].iloc[0]['password']

    # Generate random employee details
    first_name, middle_name, last_name = generate_random_name()
    employee_id = generate_random_employee_id()
    image_path = r"C:\PycharmProjects\Guvi_project1\data\profileimage.jpeg"  # Specify the image path

    login_page = LoginPage(driver)  # Initialize the LoginPage object
    login_page.login(valid_username, valid_password)  # Log in with valid credentials

    pim_page = PIMPage(driver)  # Initialize the PIMPage object
    pim_page.navigate_to_pim()  # Navigate to PIM
    pim_page.click_add_employee()  # Click on the 'Add Employee' link
    pim_page.enter_employee_details(first_name, middle_name, last_name, employee_id)  # Fill in employee details
    pim_page.upload_employee_image(image_path)  # Upload employee image
    pim_page.click_save()  # Click the save button

    toast_message = pim_page.get_toast_message()  # Get the success message after saving
    print(toast_message)
    capture_screenshot(driver, "employee_added_success")  # Capture screenshot of employee addition success
    assert "successfully saved" in toast_message.lower(), "Employee was not saved successfully"  # Validate the success message

# Test case 2: Login, navigate to PIM, and update employee details

def test_edit_employee(driver):
    """Tests editing an existing employee's details in the PIM module."""
    login_data = load_login_data()  # Load login data
    valid_username = login_data[login_data['expected'] == 'pass'].iloc[0]['username']
    valid_password = login_data[login_data['expected'] == 'pass'].iloc[0]['password']

    # Randomly generate new details for editing
    new_first_name, new_middle_name, new_last_name = generate_random_name()
    new_employee_id = generate_random_employee_id()
    new_license_number = "DL" + generate_random_employee_id()
    print("license_no",new_license_number)
    new_dob = "2002-01-01"
    print("new_dob",new_dob)

    login_page = LoginPage(driver)
    login_page.login(valid_username, valid_password)

    pim_page = PIMPage(driver)
    pim_page.navigate_to_pim()
    pim_page.select_first_employee()

    pim_page.edit_employee_details(
        first_name=new_first_name,
        middle_name=new_middle_name,
        last_name=new_last_name,
        employee_id=new_employee_id,
        license_number=new_license_number,
        dob=new_dob,
        nationality="Indian",
        marital_status="Single",
        gender="Female"
    )
    pim_page.click_save2()  # Click the save button
    # Verify if changes are successfully saved
    toast_message = pim_page.get_toast_message()
    print(toast_message)
    capture_screenshot(driver, "employee_edit_success")
    assert "successfully updated" in toast_message.lower(), "Employee details were not updated successfully"


# Test case 3: Login, navigate to PIM, and update employee details

def test_delete_employee(driver):
    login_data = load_login_data()  # Load login data
    valid_username = login_data[login_data['expected'] == 'pass'].iloc[0]['username']
    valid_password = login_data[login_data['expected'] == 'pass'].iloc[0]['password']
    login_page = LoginPage(driver)
    login_page.login(valid_username, valid_password)

    pim_page = PIMPage(driver)
    pim_page.navigate_to_pim()  # Navigate to PIM
    pim_page.delete_employee_details()
    toast_message = pim_page.get_toast_message()
    print(toast_message)
    capture_screenshot(driver, "employee_edit_success")
    assert "successfully deleted" in toast_message.lower(), "Employee details were not deleted successfully"

"""
 <--------------------------------------------PIM module ends-------------------------------------------------------->
 
"""