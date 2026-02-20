from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument(
    "--disable-dev-shm-usage"
)  # Overcomes some limitations in a shared env

browser = webdriver.Chrome(options=options)

browser.get("http://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")
