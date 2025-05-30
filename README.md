# DemoQA Selenium Automation

This project is an automated test suite for the [demoqa.com](https://demoqa.com/) website, using Python, Selenium, and Pytest. It covers navigation and form submission scenarios, generating random user data with Faker and producing Allure reports.

## Getting Started

### Prerequisites

- Python 3.8+
- Google Chrome browser

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/FilimonovKirill/demoqa-automation-project.git
   cd demoqa
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Running Tests

To run all tests and generate Allure results:

```sh
pytest
```

Allure results will be saved in the `reports/` directory.

### Viewing Allure Reports

1. Install Allure commandline (if not already installed):

   - Download from [Allure Releases](https://github.com/allure-framework/allure2/releases)
   - Or install via [Scoop](https://scoop.sh/) (recommended for Windows):

     ```sh
     scoop install allure
     ```

2. Generate and open the report:

   ```sh
   allure serve reports
   ```

## Project Structure

- `pages/` — Page Object Model classes for each tested page
- `tests/` — Test cases
- `constants/objects/` — Data models (e.g., User)
- `utils/` — Helper functions
- `conftest.py` — Pytest fixtures (e.g., Selenium WebDriver setup)
- `requirements.txt` — Python dependencies

## Notes

- ChromeDriver is managed automatically by `webdriver-manager`.
- Test data is generated dynamically using the `faker` library.
- Allure reports provide detailed test results and logs.

---