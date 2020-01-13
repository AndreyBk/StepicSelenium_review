import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# https://github.com/AndreyBk/stepik_languageLesson.git


# --user_language
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    # browser_name = request.config.getoption("browser_name")
    # browser = None
    # if browser_name == "chrome":
    #     print("\nstart chrome browser for test..")
    #     browser = webdriver.Chrome()
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     browser = webdriver.Firefox()
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")
    # browser = webdriver.Chrome()

    user_language=request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
