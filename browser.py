from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Browser(object):
    base_url = 'https://sprinkle-burn.glitch.me'
    driver = webdriver.Chrome("C:/Users/clamba/ChromeDriver/chromedriver.exe")
    driver.implicitly_wait(3)
    wait = WebDriverWait(driver, 2)

    def close(self):
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector,value):
       return self.driver.find_element_by_css_selector(selector).send_keys(value)

    def click_by_id(self,selector):
       return self.driver.find_element_by_css_selector(selector).click()

    def check_message(self,value):

        if value in self.driver.page_source:
            return True
        return False

    def credential_error(self,selector,value):
           if self.driver.find_element_by_css_selector(selector).text==value:
               return True
           return False
