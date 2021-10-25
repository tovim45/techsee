import logging

import allure
from allure_commons.types import AttachmentType
from infra.utils.selenium_utils import init_driver
from src.pages.login.login_page import MainPage

base_url = base_url = "https://fakercloud.com/api#Internet "
# username = "system"
# password = "system"


def login_to_intel360():
    """
    login
    :return: driver
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    driver = init_driver()
    driver.get(base_url)
    mp = MainPage(driver)
    # mp.enter_username(username)
    # mp.enter_password(password)
    # mp.click_login()
    mp.wait_for_loader(driver)
    page_tiele = mp.test_title()
    if page_tiele == 'intel360':
        # driver.close()
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="test_login_screen", attachment_type=AttachmentType.PNG)
        # driver.close()
        assert False
    return driver
