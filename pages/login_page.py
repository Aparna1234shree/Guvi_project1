"""
login_page.py

This module defines the LoginPage class, which encapsulates the login functionality
of the Orange HRM application. It includes methods for entering user credentials,
submitting the login form, and checking the login status based on the page title.

Usage:
    Instantiate the LoginPage class with a Selenium WebDriver instance to use its
    methods for logging into the application and verifying the login status.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page object for the login functionality of the Orange HRM application."""

    def __init__(self, driver):
        """Initializes the LoginPage with a Selenium WebDriver instance.
        Args:
            driver: A Selenium WebDriver instance used to interact with the web application.
        """

        self.driver = driver  # Store the WebDriver instance
        self.wait = WebDriverWait(driver, 10)  # Set up an explicit wait for elements

    def login(self, username, password):
        """Logs in to the application using provided username and password."""
        print("Waiting for the username field to be visible...")
        username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.clear()  # Clear the field before entering new data
        username_field.send_keys(username)  # Enter the username
        print(f"Entered Username: {username}")

        print("Waiting for the password field to be visible...")
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.clear()  # Clear the field before entering new data
        password_field.send_keys(password)  # Enter the password
        print(f"Entered Password: {password}")

        print("Waiting for the login button to be clickable...")
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()  # Click the login button
        print("Clicked on the login button.")

    def is_logged_in(self):
        """
        Checks if the user is logged in by verifying the page title.

        Returns:
               bool: True if the user is logged in (i.e., the page title contains "OrangeHRM"), otherwise False.

        """
        title = self.driver.title  # Get the current page title
        print(f"Current page title: {title}")
        return "OrangeHRM" in title  # Return True if logged in, else False
