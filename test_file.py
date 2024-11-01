import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Path to the employee image
image_path = r"C:\PycharmProjects\Guvi_project1\data\profileimage.jpeg"

# Setup Chrome WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    # Load login details and log in
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")
    print("Entered Username: Admin")

    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_field.send_keys("admin123")
    print("Entered Password: admin123")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    print("Clicked on the login button.")

    # Navigate to the PIM section
    pim_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")))
    pim_element.click()
    print("Clicked on PIM element.")

    # Wait for the "Add Employee" link to be present and clickable
    add_employee_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'addEmployee')]")))
    add_employee_link.click()
    print("Clicked on Add Employee link.")

    # Fill in employee details
    first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    first_name_field.send_keys("John")
    print("Entered First Name: John")

    middle_name_field = wait.until(EC.presence_of_element_located((By.NAME, "middleName")))
    middle_name_field.send_keys("A")
    print("Entered Middle Name: A")

    last_name_field = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
    last_name_field.send_keys("Doe")
    print("Entered Last Name: Doe")

    employee_id_field = wait.until(EC.presence_of_element_located((By.NAME, "employeeId")))
    employee_id_field.clear()  # Clear any auto-generated ID
    employee_id_field.send_keys("123456")
    print("Entered Employee ID: 123456")

    # Upload employee image
    upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'employee-image-action')]")))
    upload_button.click()
    print("Upload button clicked.")

    # Wait for the file input to be present and send the image path
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(image_path)
    print(f"Image uploaded from: {image_path}")

    # Click on the 'Save' button to add the employee
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(text(), 'Save')]")))
    save_button.click()
    print("Clicked on the Save button.")

    # Wait for a moment to observe the result (optional)
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()
    print("Driver closed.")
