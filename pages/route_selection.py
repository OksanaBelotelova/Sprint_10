import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RouteSelection(BasePage):

    ROUTE_SELECTION_SECTION = [By. XPATH, './/div[@class = "type-picker shown"]']
    PRICE_MESSAGE = [By. XPATH, './/div[@class = "results-text"]/div[@class = "text"]'] 
    TIME_MESSAGE = [By. XPATH, './/div[@class = "results-text"]/div[@class = "duration"]']
    ACTIVE_TAB = [By. XPATH, './/div[@class ="mode active"]']
    OPTIMAL_TAB = [By. XPATH,'.//div[text() = "Оптимальный"]']
    FAST_TAB = [By. XPATH,'.//div[text() = "Быстрый"]']
    YOUR_OWN_TAB = [By. XPATH,'.//div[text() = "Свой"]']
    CAR = [By. XPATH,'.//div[@class = "types-container"]/div[1]']
    ON_FOOT = [By. XPATH,'.//div[@class = "types-container"]/div[2]']
    TAXI = [By. XPATH,'.//div[@class = "types-container"]/div[3]']
    BICYCLE = [By. XPATH,'.//div[@class = "types-container"]/div[4]']
    SCOOTER = [By. XPATH,'.//div[@class = "types-container"]/div[5]']
    DRIVER = [By. XPATH,'.//div[@class = "types-container"]/div[6]']
    TYPES_OF_MOVEMENT = [CAR, ON_FOOT, TAXI, BICYCLE, SCOOTER, DRIVER]
    CALL_A_TAXI_BUTTON = [By. XPATH, './/button[text() = "Вызвать такси"]']
    RESERVE_BUTTON = [By. XPATH, './/button[text() = "Забронировать"]']
   
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
    
    @allure.step('Проверить активность таба при переключении')
    def check_tab_is_active(self):
        self.wait_until_visible(self.TIME_MESSAGE)
        return self.find_element(self.ACTIVE_TAB).text

    @allure.step('Перейди на вкладку "Оптимальный"')
    def click_optimal_tab(self):
        self.find_element(self.OPTIMAL_TAB).click()

    @allure.step('Перейди на вкладку "Быстрый"')
    def click_fast_tab(self):
        self.find_element(self.FAST_TAB).click()

    @allure.step('Перейди на вкладку "Свой"')
    def click_your_own_tab(self):
        self.find_element(self.YOUR_OWN_TAB).click()

    @allure.step('Проверь активность видов движения')
    def check_types_of_movement_are_active(self, element):
        if "disabled" not in self.find_element(element).get_attribute("class"):
            return True
        else:
            return False
        
    @allure.step('Проверь кнопку "Вызвать такси"')
    def check_call_a_taxi_button(self):
        self.wait_until_clickable(self.CALL_A_TAXI_BUTTON)
        return self.find_element(self.CALL_A_TAXI_BUTTON)
    
    @allure.step('Выбери "Драйв"')
    def click_driver_type(self):
        self.wait_until_clickable(self.DRIVER)
        self.find_element(self.DRIVER).click()

    @allure.step('Проверь кнопку "Забронировать"')
    def check_reserve_button(self):
        self.wait_until_clickable(self.RESERVE_BUTTON)
        return self.find_element(self.RESERVE_BUTTON)
    
    @allure.step('Нажми на кнопку "Вызвать такси"')
    def click_call_a_taxi_button(self):
        self.wait_until_clickable(self.CALL_A_TAXI_BUTTON)
        self.find_element(self.CALL_A_TAXI_BUTTON).click()

    