# DemoQA Playwright Automation

![Python](https://img.shields.io/badge/Python-3.13-blue)  
![Pytest](https://img.shields.io/badge/Pytest-8.3.5-orange)  
![Playwright](https://img.shields.io/badge/Playwright-Yes-brightgreen)  
![Allure](https://img.shields.io/badge/Allure-Reports-purple)

This repository contains **automation tests for the DemoQA website** built using  
**Python**, **Playwright**, and **Pytest**.  
Test execution and reporting are intended to be run **locally only**.

---

## ✨ Features

- Student Registration Form automation
- Bookstore API automation (add & delete books)
- Page Object Model (POM) architecture
- Allure test reports
- Secure handling of credentials using a local `config.py`

---

## 🛠 Technologies Used

- Python 3.13
- Playwright
- Pytest
- Allure
- Requests (for API testing)

---

## 📁 Project Structure

.
├── pages/ # Page Object classes
├── tests/ # Test cases
├── utils/ # Helper and utility modules
├── reports/ # Allure test results
├── config.py # Local credentials (git-ignored)
├── .gitignore
└── README.md


---

## 🔐 Configuration (`config.py`)

The project uses a **local configuration file** named `config.py` to store sensitive information such as **username and password**.

This file is:
- **Required to run the tests**
- **Ignored by Git** (`.gitignore`)
- **Not committed to the repository**

### Example `config.py`

Create a file named `config.py` in the project root:

```python
USERNAME = "your_username"
PASSWORD = "your_password"
```


## 👤 Author

- Sanjuta Tidke
- GitHub: https://github.com/Sanjuta96