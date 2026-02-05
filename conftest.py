import pytest
from selenium import webdriver
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    browser.config.driver = webdriver.Chrome(options=options)

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10.0

    yield 

    browser.quit() 
