# Orange HRM Login Module Automation

## Project Overview
This project automates the login functionality of the Orange HRM web application using Selenium in Python. It follows the Page Object Model (POM) pattern and Data-Driven Testing Framework (DDTF) for maintainable test code.

### Features
- **Page Object Model (POM)** for modular and reusable components.
- **Data-Driven Testing (DDTF)** using CSV for multiple test cases.
- **Exception Handling and Explicit Waits** instead of time.sleep().
- **Detailed Test Report** generated with pytest-html.
- **Screenshots** of test cases saved in case of failure for debugging.

### Prerequisites
- Python 3
- ChromeDriver

### Setup
1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
### Project Structure
* pages/: Contains Page Object classes.
* tests/: Test scripts.
* data/: Test data files.
* screenshots/: Stores screenshots of test runs.
* reports/: Contains pytest reports in HTML .
### Running Tests
* Execute the test suite with HTML reporting:
 ```bash
pytest --html=reports/login_test_report.html
