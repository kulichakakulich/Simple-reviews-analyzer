# WebMonitoring
WebMonitoring is a Python script that automates the login process to the 21-school educational platform, and checks if a code review is available.

### Prerequisites
Before running the script, make sure that you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Selenium WebDriver](https://selenium-python.readthedocs.io/installation.html#introduction)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
- [telebot](https://pypi.org/project/pyTelegramBotAPI/)
### Usage
1. Clone the repository to your local machine
2. Install the prerequisites
3. Create a file named personal_data.py with the following variables:
    - login: your login name for the 21-school educational platform
    - password: your password for the 21-school educational platform
    - user_id: your telegram user id
    - token: your telegram bot token
4. Run the script using the command python web_monitoring.py

### How it works
The script opens a headless Chrome browser and logs in to the 21-school educational platform using the credentials provided in personal_data.py. It then navigates to the code review page and checks if a code review is available. If a code review is available, it sends a notification to the telegram user with the user id provided in personal_data.py.

The script continuously checks for code reviews every 50 seconds. If a code review is not available, it refreshes the page and checks again.

### Disclaimer
This script was created for educational purposes only. The authors are not responsible for any misuse or damage caused by this script. Use at your own risk.
