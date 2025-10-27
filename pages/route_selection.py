import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class RouteSelection(BasePage):

    ROUTE_SELECTION_SECTION = [By. XPATH, './/div[@class = "type-picker shown"]']
    PRICE_MESSAGE = [By. XPATH, './/div[@class = "results-text"]/div[@class = "text"]'] 
    TIME_MESSAGE = [By. XPATH, './/div[@class = "results-text"]/div[@class = "duration"]']
    MESSAGE = [By. XPATH, './/div[@class = "results-text"]/div[@class = "text"].text() || .//div[@class = "results-text"]/div[@class = "duration"].text()']

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверь появление блока с выбором маршрута')
    def check_route_selection_section(self):
        return self.find_element(self.ROUTE_SELECTION_SECTION)
    
    @allure.step('Проверь сообщение')
    def check_message(self):
        self.wait_until_visible(self.PRICE_MESSAGE)
        price_message = self.find_element(self.PRICE_MESSAGE).text
        time_message = self.find_element(self.TIME_MESSAGE).text
        message = f"{price_message} {time_message}"
        return message