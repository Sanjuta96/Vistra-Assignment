
# DemoQA Playwright Automation

![Python](https://img.shields.io/badge/Python-3.13-blue) 
![Pytest](https://img.shields.io/badge/Pytest-8.3.5-orange) 
![Playwright](https://img.shields.io/badge/Playwright-Yes-brightgreen) 
![Allure](https://img.shields.io/badge/Allure-Reports-purple)

This repository contains **automation tests for the DemoQA website** using **Python**, **Playwright**, and **Pytest**.  
Reports are generated using **Allure**.

## Features

- Student Registration form automation
- Bookstore API automation: add and delete books
- Modular Page Object Model (POM) design
- Allure reports for test results
- Configurable credentials via `config.py` (excluded from Git)

## Technologies Used

- Python 3.13
- Playwright
- Pytest
- Allure
- Requests (for API testing)

## Project Structure

- `pages/` – Page object classes  
- `tests/` – Test cases  
- `utils/` – Helper modules  
- `reports/` – Allure results  
- `config.py` – Credentials (ignored in Git)  
- `.github/workflows/` – GitHub Actions workflows (CI/CD)

## CI/CD / Workflows

- GitHub Actions are used for running tests automatically on push.  
- Workflow files:
  - `ci.yaml` – Continuous integration pipeline
## Author

**Sanjuta Tidke**  
[GitHub](https://github.com/Sanjuta96)
