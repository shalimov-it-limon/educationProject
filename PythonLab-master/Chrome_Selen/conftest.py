from selenium import webdriver
import pytest
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application'
    chrome_options.add_extension('C:\\Program Files\\Google\\Chrome\\Application\\103.0.5060.66\\Extensions')
    chrome_options.add_argument('--kiosk')
    return chrome_options

@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL']

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome("E:\\Work\\educationProject\\venv\\chromedriver.exe")