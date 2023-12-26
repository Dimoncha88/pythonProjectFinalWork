from testpage import OperationsHelper
import yaml
import time

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_about_link()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_header_size() == testdata['header_size']
