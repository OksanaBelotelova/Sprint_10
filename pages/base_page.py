import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Addresses

class BasePage:
    FROM_FIELD = [By.ID, "from"]
    WHERE_FIELD = [By.ID, "to"]
    POINTS = [By. XPATH, './/ymaps[contains(text(), "{}")]']

    def __init__(self, driver):
            self.driver = driver
            self.actions = ActionChains(driver)

    def wait_until_clickable(self,element, time = 10 ):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element))

    def wait_until_visible(self,element, time = 15):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located((element)))

    def find_element(self, element):
        return self.driver.find_element(*element)
    
    def execute_script(self, script):
        self.driver.execute_script(script) 
    
    def hover_over(self,element):
        icon = self.find_element(element)
        self.actions.move_to_element(icon).click_and_hold(icon).perform()
    
    @allure.step('Заполни поле "Откуда"')
    def enter_from_address(self):
        self.find_element(self.FROM_FIELD).send_keys(Addresses.first_address)

    @allure.step('Заполни поле "Куда"')
    def enter_where_address(self):
        self.find_element(self.WHERE_FIELD).send_keys(Addresses.second_address)

    @allure.step('Введи одинаковые адреса в поля "Откуда" и "Куда"')
    def  input_two_the_same_addresses_for_route(self):
        self.find_element(self.FROM_FIELD).send_keys(Addresses.first_address)
        self.find_element(self.WHERE_FIELD).send_keys(Addresses.first_address)

    @allure.step('Ввести два разных адреса в поля "Откуда" и "Куда"')
    def input_two_different_addresses_for_route(self):
        self.find_element(self.FROM_FIELD).send_keys(Addresses.first_address)
        self.find_element(self.WHERE_FIELD).send_keys(Addresses.second_address)

    @allure.step('Проверь точку "Начала маршрута"')
    def check_point_A(self):
        point_A = str(self.POINTS).format(Addresses.first_address)
        return point_A
    
    @allure.step('Проверь точку "Конца маршрута"')
    def check_point_B(self):
        point_B = str(self.POINTS).format(Addresses.second_address)
        return point_B
    
    