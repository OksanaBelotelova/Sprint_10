import allure
import pytest
from pages.route_selection import RouteSelection
from pages.order_taxi_form import OrderTaxi
from data import TariffCards, OrderTaxiElements


class TestOrderTaxi:

    @allure.title('Тарифы заказа такси')
    @allure.description('После нажатия кнопки "вызвать такси" открывается форма заказа со всеми 6 тарифами, один из них активный')
    @pytest.mark.parametrize("tariff", OrderTaxi.TARIFF_LIST)
    def test_tariff_section(self, driver, tariff):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)
        
        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()

        tariff_section = taxi.check_tariff_section()

        assert tariff_section.is_displayed()

        tariff = taxi.check_tariffs(tariff)

        assert tariff.is_displayed()

        One_active_tariff = taxi.check_active_tariff()

        assert One_active_tariff

    @pytest.mark.xfail(reason = 'AssertionError Описания для двух тарифов перепутаны, this a bug')
    @allure.title('Всплывающее окно с описание тарифа')
    @allure.description('При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа')
    @pytest.mark.parametrize("tariff, description, expected", zip(OrderTaxi.TARIFF_LIST, OrderTaxi.TARIFF_DESCRIPTION_LIST, list(TariffCards.Tariff_cards_description.values()) ))
    def test_tariff_information_popup(self, driver, tariff, description, expected):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()
        taxi.click_tariff(tariff)
        taxi.hover_over_i_icon()
        actual_description = taxi.check_tariff_description(description)
        
        assert actual_description == expected

    
    @allure.title('Форма данных о заказе такси')  
    @allure.description('Под тарифами отображается блок с полями и кнопкой заказа')
    @pytest.mark.parametrize("elements", OrderTaxi.ELEMENTS_OF_ORDER_TAXI_FORM)
    def test_elements_of_order_taxi_form(self, driver, elements):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()
        
        element = taxi.check_elements_of_order_taxi_form(elements)

        assert element.is_displayed()

    
    @allure.title('Oкно ожидания машины')
    @allure.description('После  нажатия "Ввести номер и заказать", появляется окно ожидания машины со всеми элементами')
    def test_waiting_for_a_car_window(self, driver):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()
        taxi.order_a_taxi()

        waiting_for_car_window = taxi.get_waiting_for_a_car_window()

        assert waiting_for_car_window.is_displayed()

        actual_title = taxi.get_waiting_for_a_car_window_title()
        expected_title = OrderTaxiElements.waiting_for_a_car_title
        timer = taxi.get_timer()
        cancel_button = taxi.get_cancel_button()
        details_button = taxi.get_details_button()
       
        assert actual_title == expected_title
        assert timer.is_displayed()
        assert cancel_button.is_displayed()
        assert details_button.is_displayed()

    

    @allure.title('Oкно совершенного заказа')
    @allure.description('После окончания таймера поиска машины, oтображается окно совершенного заказа')
    def test_completed_order_window(self, driver):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()
        taxi.order_a_taxi()
        
        completed_order_window = taxi.get_completed_order_window()
        title = taxi.get_completed_order_window_title()
        text_of_title = OrderTaxiElements.completed_order_window_title

        assert completed_order_window.is_displayed()
        assert text_of_title in title

    @allure.title('Элементы Oкна совершенного заказа')
    @allure.description('Окно совершенного заказа содержит все необходимые элементы')
    @pytest.mark.parametrize("element", OrderTaxi.COMPLETED_ORDER_WINDOW_ELEMENTS)
    def test_completed_order_window_elements(self, driver, element):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()
        taxi.order_a_taxi()
        
        element = taxi.get_completed_order_window_elements(element)

        assert element.is_displayed()


    @allure.title('Стоимость поездки')
    @allure.description('В блоке "Еще про поездку", указана стоимость, которая была при выборе тарифа')
    def test_tariff_price_and_price_in_details_are_the_same(self, driver):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.input_two_different_addresses_for_route()
        route.click_call_a_taxi_button()
        tariff_price = taxi.get_tariff_price()
        taxi.order_a_taxi()
        taxi.click_details_button()
        price_in_details_window = taxi.get_price()

        assert tariff_price in price_in_details_window

    @pytest.mark.xfail(reason='completed_order_window.is_displayed(), this a bug')
    @allure.title('Кнопка oтмены заказа')
    @allure.description('При нажатии кнопки "Отмена", окно закрывается')
    def test_cancel_button(self, driver):
        route = RouteSelection(driver)
        taxi = OrderTaxi(driver)

        route.enter_from_address()
        route.enter_where_address()
        route.click_call_a_taxi_button()
        taxi.order_a_taxi()

        completed_order_window = taxi.get_completed_order_window()
        
        taxi.click_cancel_button()

        assert completed_order_window.is_displayed() is False
        