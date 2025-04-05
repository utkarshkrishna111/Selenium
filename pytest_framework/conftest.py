import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

#request is a default fixture available for framework used
# when options passed through command line
@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
#browser_name = browser_name.capitalize()
    if browser_name == "chrome":
        service_obj = Service(r"C:\Users\utkar\Downloads\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--ignore-certificate-errors")
#driver = webdriver.Chrome(service=service_obj, options = chrome_options)
    elif browser_name == "firefox":
        service_obj = Service(r"C:\Users\utkar\Downloads\geckodriver.exe")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(service=service_obj,options= firefox_options)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close() #post test function execution

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
