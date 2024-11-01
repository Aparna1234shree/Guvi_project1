"""
pim_page.py

This module defines the PIMPage class, which contains methods for interacting with
the Employee Management functionalities in the Orange HRM application. It provides
functions to navigate through the PIM module and perform actions such as adding
and viewing employee details.

Usage:
    To use this module, create an instance of the PIMPage class with a Selenium
    WebDriver instance and call the appropriate methods to interact with the
    PIM features of the application.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PIMPage:
    """Page object for the PIM (Personnel Information Management) section."""

    def __init__(self, driver):
        self.driver = driver  # Store the driver instance
        self.wait = WebDriverWait(driver, 20)  # Set up an explicit wait

    def navigate_to_pim(self):
        """Clicks on the PIM tab."""
        print("Waiting for the PIM element to be clickable...")
        pim_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))  # Wait for PIM element
        print("PIM element found, clicking...")
        pim_element.click()  # Click on PIM tab

    def click_add_employee(self):
        """Clicks on the 'Add Employee' link."""
        print("Waiting for the 'Add Employee' link to be clickable...")
        add_employee_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Employee']"))
        )  # Wait for 'Add Employee' link
        print("Add Employee tab located, attempting to click...")
        add_employee_link.click()  # Click on 'Add Employee'

    def enter_employee_details(self, first_name, middle_name, last_name, employee_id):
        """Fills in the employee details."""
        print("Entering employee details...",first_name, middle_name, last_name, employee_id)

        # Fill in first name
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        print(f"Entered First Name: {first_name}")

        # Fill in middle name
        middle_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "middleName")))
        middle_name_field.clear()
        middle_name_field.send_keys(middle_name)
        print(f"Entered Middle Name: {middle_name}")

        # Fill in last name
        last_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        print(f"Entered Last Name: {last_name}")

        # Fill in employee ID
        employee_id_field = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Employee Id']/ancestor::div[contains(@class, 'oxd-input-group')]//input"))
        )
        employee_id_field.clear()
        employee_id_field.send_keys(employee_id)
        print(f"Entered Employee ID: {employee_id}")

    def upload_employee_image(self, image_path):
        """Uploads the employee's profile image."""
        # Specify the image path
        file_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='file']")))  # Adjusted to a more general selector
        file_input.send_keys(image_path)  # Upload the image using send_keys
        print(f"Image uploaded from: {image_path}")

    def click_save(self):
        """Clicks the save button."""
        print("Save button function called")
        save_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        save_button.click()  # Click on the save button
        print("Save button clicked")

    def click_save2(self):
        save_btn = self.wait.until(
            EC.visibility_of_element_located(
                (
                    (By.CSS_SELECTOR,".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) .oxd-button--secondary")
                )
            )
        )
        save_btn.click()
    def get_toast_message(self):
        """Retrieves the success toast message after saving."""
        print("Waiting for the success toast message to be visible...")
        # Wait for the success toast to be visible using XPath
        toast = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast-content--success')]")))
        message = toast.find_element(By.XPATH, ".//p[contains(@class, 'oxd-text--p oxd-text--toast-message')]").text
        print("Toast message is", message)
        return message  # Return the text of the toast message

    def select_first_employee(self):
        """Selects the first employee in the employee list."""
        try:
            # Wait until the employee list is visible
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@role='table']/div[2]/div[1]/div[1]"))
            )

            # Locate the first employee's row using the provided XPath
            first_employee_row = self.driver.find_element(By.XPATH, "//div[@role='table']/div[2]/div[1]/div[1]")

            # Click on the first employee's row to open their details
            first_employee_row.click()

            print("Successfully selected the first employee.")
        except Exception as e:
            print(f"Error selecting the first employee: {e}")

    def clear_and_enter_text(self, locator_type, locator, text, field_name):
        """Clear existing text and enter new text."""
        field = self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        current_value = field.get_attribute("value")  # Get current value of the field
        if current_value != text:  # Only clear and enter if the current value is different
            field.clear()  # Clear the field before entering new text
            field.send_keys(text)
            print(f"Entered '{text}' in {field_name}.")
        else:
            print(f"No change needed for {field_name}. Current value is already '{current_value}'.")

    def select_marital_status(self, status):
        """Select marital status from dropdown."""

        marital_status_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-grid-item--gutters:nth-of-type(2) [tabindex]")
            )
        )
        marital_status_field.click()

        while marital_status_field.text != status:
            marital_status_field.send_keys(Keys.ARROW_DOWN)
        marital_status_field.send_keys(Keys.ENTER)
        print(f"Selected marital status: '{status}'.")

    def select_nationality(self, nationality):
        """Select nationality from dropdown."""

        print(f"Selecting nationality: {nationality}")

        # Wait for the nationality field to be visible and click it
        nationality_field =self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) .oxd-grid-item--gutters:nth-of-type(1) [tabindex]")
            )
        )
        # (By.CSS_SELECTOR,".orangehrm-edit-employee-content .orangehrm-vertical-padding:nth-of-type(1) \.oxd-grid-item--gutters:nth-of-type(1) [tabindex]")

        nationality_field.click()

        while nationality_field.text != nationality:
            nationality_field.send_keys(Keys.ARROW_DOWN)
        nationality_field.send_keys(Keys.ENTER)

        print(f"Nationality '{nationality}' selected.")

    def select_gender(self, gender):
        """Select gender radio button."""

        if gender == 'male':
            gender_option = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".--gender-grouped-field .oxd-input-field-bottom-space:nth-of-type(1) label")
                )
            )
        else:
            gender_option = self.wait.until(EC.visibility_of_element_located
                      ((By.CSS_SELECTOR, ".--gender-grouped-field .oxd-input-field-bottom-space:nth-of-type(2) label")))

        gender_option.click()

        print(f"Selected gender: '{gender}'.")

    def edit_employee_details(self, first_name, middle_name, last_name, employee_id, license_number, dob, nationality, marital_status, gender):
        """Edit employee details."""
        # Enter employee full name
        self.enter_employee_details(first_name, middle_name, last_name, employee_id)

        # Enter license number
        self.clear_and_enter_text(By.XPATH, "//label[text()=\"Driver's License Number\"]/parent::div/following-sibling::div/input", license_number, "Driver's License Number")

        # Enter license expiry date (hardcoded value)
        self.clear_and_enter_text(By.XPATH, "//label[text()='License Expiry Date']/parent::div/following-sibling::div//input", "2024-10-30", "License Expiry Date")

        # Enter Date of Birth
        self.clear_and_enter_text(By.XPATH, "//label[text()='Date of Birth']/parent::div/following-sibling::div//input", dob, "Date of Birth")

        # Select marital status
        self.select_marital_status(marital_status)

        # Select gender
        self.select_gender(gender)

    def delete_employee_details(self):
        """Selects the employee checkbox and clicks the delete button."""

        # Wait for the checkbox to be visible and click it
        checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[@role='rowgroup']/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]"))
        )
        if not checkbox.is_selected():
            checkbox.click()
        print("Employee checkbox selected.")

        # Wait for the delete button to be clickable and click it
        delete_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button--label-danger"))
        )
        delete_button.click()

        print("Delete Selected button clicked.")
        confirm_button =  self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"))
        )
        confirm_button.click()
        print("Confirmed deletion.")
