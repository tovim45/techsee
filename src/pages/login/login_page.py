from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E


class MainPage:
    title = 'intel360'
    wait_time_out = 20
    username_id = '//*[@id="root"]/div/div/div/input[1]'
    password_id = '//*[@id="root"]/div/div/div/input[2]'
    login_btn = "//*[@id=\"root\"]/div/div/div/div/button"
    login_failed_text = "//*[@id='root']/div/div/div/span"
    # vector_logo = "//*[@id='root']/div/div[1]/div[1]/div[1]/h3"
    active_mission_left_bar = "//*[@id='root']/div/div[2]/div[1]/div/div[3]/div[1]/div/div/div[1]/div"

    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = W(self.drv, self.wait_time_out)

    def test_title(self):
        print(self.title + " page title is the OK and equal to: " + self.drv.title)
        assert self.title in self.drv.title
        return self.drv.title

    def enter_username(self, username):
        self.wait_variable.until(E.presence_of_element_located((By.XPATH, self.username_id))).send_keys(username)

    def enter_password(self, password):
        self.wait_variable.until(E.presence_of_element_located((By.XPATH, self.password_id))).send_keys(password)

    def click_login(self):
        self.wait_variable.until(E.element_to_be_clickable((By.XPATH, self.login_btn))).click()

    def get_text_login_failed(self):
        elem = self.wait_variable.until(E.element_to_be_clickable((By.XPATH, self.login_failed_text))).text
        print(elem)
        return elem

    def wait_for_loader(self, driver):
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.active_mission_left_bar)))
        self.wait_variable.until(E.presence_of_element_located((By.XPATH, self.active_mission_left_bar)))
