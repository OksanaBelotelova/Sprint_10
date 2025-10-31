import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderTaxi(BasePage):

    TARIFF_SECTION = [By. XPATH,'.//div[@class="tariff-cards"]']
    TARIFF_WORKING = [By. XPATH, '//div[text()="Рабочий" and @class = "tcard-title"]/parent::div']
    TARIFF_SLEEPY = [By. XPATH, './/div[text()="Сонный" and @class = "tcard-title"]/parent::div']
    TARIFF_HOLIDAY = [By. XPATH, './/div[text()="Отпускной" and @class = "tcard-title"]/parent::div']
    TARIFF_TALKATIVE = [By. XPATH, './/div[text()="Разговорчивый" and @class = "tcard-title"]/parent::div']
    TARIFF_CONSOLATION = [By. XPATH, './/div[text()="Утешительный" and @class = "tcard-title"]/parent::div']
    TARIFF_GLOSSY = [By. XPATH, './/div[text()="Глянцевый" and @class = "tcard-title"]/parent::div']
    TARIFF_LIST = [TARIFF_WORKING, TARIFF_SLEEPY, TARIFF_HOLIDAY, TARIFF_TALKATIVE, TARIFF_CONSOLATION, TARIFF_GLOSSY]
    I_ICON = [By. XPATH, './/div[@class = "tcard active"]/button[@class = "i-button tcard-i active"]']
    TARIFF_WORKING_DESCRIPTION = [By. XPATH, './/div[contains(text(), "Для деловых особ")]']
    TARIFF_SLEEPY_DESCRIPTION = [By. XPATH, './/div[contains(text(), "Если мысли")]']
    TARIFF_HOLIDAY_DESCRIPTION = [By. XPATH, './/div[contains(text(), "пора отдохнуть")]']
    TARIFF_TALKATIVE_DESCRIPTION = [By. XPATH, './/div[contains(text(), "кто не выспался")]']
    TARIFF_CONSOLATION_DESCRIPTION = [By. XPATH, './/div[contains(text(), "хочется свернуться")]']
    TARIFF_GLOSSY_DESCRIPTION = [By. XPATH, './/div[contains(text(), "блистать")]']
    TARIFF_DESCRIPTION_LIST = [TARIFF_WORKING_DESCRIPTION, TARIFF_SLEEPY_DESCRIPTION, TARIFF_HOLIDAY_DESCRIPTION, TARIFF_TALKATIVE_DESCRIPTION, TARIFF_CONSOLATION_DESCRIPTION, TARIFF_GLOSSY_DESCRIPTION]
    PHONE_NUMBER_FIELD = [By. XPATH, './/div[text()="Телефон"]']
    INPUT_PHONE_NUMBER_FIELD = [By. ID, "phone"]
    PAYMENT_METHOD_FIELD = [By. XPATH, './/div[@class ="pp-button filled"]']
    COMMENT_FIELD = [By. ID, "comment"]
    ORDER_REQUIREMENTS = [By. XPATH, './/div[text()="Требования к заказу"]']
    ORDER_TAXI_BUTTON = [By. XPATH, './/span[text()="Ввести номер и заказать"]']
    ELEMENTS_OF_ORDER_TAXI_FORM = [PHONE_NUMBER_FIELD, PAYMENT_METHOD_FIELD, COMMENT_FIELD, ORDER_REQUIREMENTS,  ORDER_TAXI_BUTTON]
    WAITING_FOR_A_CAR_WINDOW = [By. XPATH, './/div[@class = "order-body"]']
    CAR_SEARCH_TITLE = [By. XPATH, './/div[text()="Поиск машины"]']
    TIMER = [By. XPATH,'.//div[@class = "order-header-time"]'] 
    CANCEL_BUTTON = [By. XPATH, './/div[text() = "Отменить"]/preceding-sibling::button']
    ORDER_DETAILS = [By. XPATH, './/div[text() = "Детали"]/preceding-sibling::button']
    COMPLETED_ORDER_WINDOW = [By. XPATH, './/div[@class = "order-body"]']
    COMPLETED_ORDER_WINDOW_TITLE = [By. XPATH, './/div[@class = "order-header-title"]']
    CAR_NUMBER = [By. XPATH, './/div[@class = "number"]']
    TARIFF_IMG = [By. XPATH, './/img[@alt="Car"]']
    DRIVER_NAME = [By. XPATH, './/div[@class = "order-button"]/following-sibling::div'] 
    DRIVER_RATING = [By. XPATH, './/div[@class = "order-btn-rating"]']
    DRIVER_PHOTO = [By. XPATH, './/img[@alt="close"]']
    COMPLETED_ORDER_WINDOW_ELEMENTS = [CANCEL_BUTTON, ORDER_DETAILS, CAR_NUMBER, TARIFF_IMG, DRIVER_NAME, DRIVER_RATING, DRIVER_PHOTO]
    PRICE_IN_DETAILS_WINDOW = [By. XPATH, './/div[text() = "Еще про поездку"]/following-sibling::div']
    TARIFF_PRICE = [By. XPATH, './/div[text()="Рабочий" and @class = "tcard-title"]/following-sibling::div']

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверь форму с тарифами')
    def check_tariff_section(self):
        self.wait_until_visible(self.TARIFF_SECTION)
        return self.find_element(self.TARIFF_SECTION)
    
    @allure.step('Проверь тарифы')
    def check_tariffs(self, tariff):
        self.wait_until_visible(tariff)
        return self.find_element(tariff)
    
    @allure.step('Проверь что один тариф активный')
    def check_active_tariff(self):
        active = 0
        for tariff in self.TARIFF_LIST:
            if "active" in self.find_element(tariff).get_attribute("class"):
                return active + 1
            else:
                return active + 0
        if active == 1:
            return True
        else: 
            return False
        

    @allure.step('Выбери тариф')
    def click_tariff(self, tariff):
        self.find_element(tariff).click()

    @allure.step('Наведи курсон на иконку i')
    def hover_over_i_icon(self):
        self.hover_over(self.I_ICON)       

    @allure.step('Проверь поля формы заказа такси')
    def check_elements_of_order_taxi_form(self, element):
        self.wait_until_visible(element)
        return self.find_element(element) 

    @allure.step('Проверь описание тарифа')
    def check_tariff_description(self, description):
        self.wait_until_visible(description)
        return self.find_element(description).text

    @allure.step('Нажми на поле "Требования к заказу"')
    def click_order_requirements(self):
        self.find_element(self.ORDER_REQUIREMENTS).click()
    
    @allure.step('Нажми на кнопку "Ввести номер и заказать"')
    def order_a_taxi(self):
        self.find_element(self.ORDER_TAXI_BUTTON).click()

    @allure.step('Проверь, что появилось окно ожидания машины ')
    def get_waiting_for_a_car_window(self):
        return self.find_element(self.WAITING_FOR_A_CAR_WINDOW)

    @allure.step('Проверь заголовок окна ожидания машины Такси')
    def get_waiting_for_a_car_window_title(self):
        return self.find_element(self.CAR_SEARCH_TITLE).text
    
    @allure.step('Проверь кнопку "Отмена"')
    def get_cancel_button(self):
        return self.find_element(self.CANCEL_BUTTON)
    
    @allure.step('Проверь кнопку "Детали"')
    def get_details_button(self):
        return self.find_element(self.ORDER_DETAILS)
    
    @allure.step('Проверь Таймер')
    def get_timer(self):
        return self.find_element(self.TIMER)

    @allure.step('Проверь, что появилось окно совершенного заказа')
    def get_completed_order_window(self):
        self.wait_until_visible(self.CAR_NUMBER, time = 40)
        return self.find_element(self.COMPLETED_ORDER_WINDOW)

    @allure.step('Проверь заголовок окна совершенного заказа')
    def get_completed_order_window_title(self):
        return self.find_element(self.COMPLETED_ORDER_WINDOW_TITLE).text
    
    @allure.step('Проверь элементы окна совершенного заказа')
    def get_completed_order_window_elements(self, element):
        self.wait_until_visible(self.CAR_NUMBER, time = 40)
        return self.find_element(element)
    
    @allure.step('Нажми на кнопку Детали')
    def click_details_button(self):
        self.wait_until_visible(self.CAR_NUMBER, time = 40)
        self.find_element(self.ORDER_DETAILS).click()

    @allure.step('Проверь стоимость поездки в блоке "Еще про поездку"')
    def get_price(self):
        return self.find_element(self.PRICE_IN_DETAILS_WINDOW).text

    @allure.step('Проверь стоимость поездки при выборе тарифа')
    def get_tariff_price(self):
        return self.find_element(self.TARIFF_PRICE).text
     
    @allure.step('Нажми на кнопку Отмена')
    def click_cancel_button(self):
        self.wait_until_visible(self.CAR_NUMBER, time = 40)
        self.find_element(self.CANCEL_BUTTON).click()
    
    @allure.step('Проверь, что окно совершенного заказа закрылось')
    def get_completed_order_window_is_closed(self):
        return self.find_element(self.COMPLETED_ORDER_WINDOW)