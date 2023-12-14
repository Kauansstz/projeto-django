from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.chrome.service import Service
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = "chromedriver.exe"
CHROMEDRIVER_PATH = ROOT_PATH / "bin" / CHROMEDRIVER_NAME


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if os.environ.get("SELENIUM_HEADÇESS") == "1":
        chrome_options.add_argument("--headless")

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)  # type: ignore
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)  # type: ignore
    return browser


if __name__ == "__main__":
    browser = make_chrome_browser()
    browser.get("http://www.udemy.com/")
    sleep(5)
    browser.quit()
