import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language by it's code")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    if browser_language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
        print('\nstart Chrome browser for test..')
    else:
        raise pytest.UsageError("--browser_language should exist")
    yield browser
    print("\nquit browser..")
    browser.quit()