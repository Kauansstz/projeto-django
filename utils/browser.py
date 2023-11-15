from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = "chromedriver.exe"
CHROMEDRIVER_PATH = ROOT_PATH / "bin" / CHROMEDRIVER_NAME

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=CHROMEDRIVER_PATH)  # type: ignore
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)  # type: ignore

browser.get("https://www.google.com.br")

# chrome_options.add_argument()
