import allure
import pytest
from pages.route_selection import RouteSelection
from data import Message, SelectRouteTab

class TestRouteSelection:
    
    @allure.title('Появление блока с выбором маршрута')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута')
    def test_route_selection_section(self, driver):
        route = RouteSelection(driver)

        route.input_two_different_addresses_for_route()

        route_selection_section = route.check_route_selection_section()

        assert route_selection_section.is_displayed()
    
    
    @allure.title('Появление сообщения при вводе двух одинаковых адресов')
    @allure.description('При вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается сообщение с текстом "Авто Бесплатно В пути 0 мин."')
    def test_two_the_same_addresses_in_from_and_where_fields(self, driver):
        route = RouteSelection(driver)

        route.input_two_the_same_addresses_for_route()

        actual_message = route.check_message()
        expected_message = Message.message

        assert actual_message == expected_message


    @allure.title('Переключение между видами маршрута("Оптимальный"\"Быстрый")')   
    @allure.description('При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута')
    def test_switching_between_optimal_and_fast_route_types(self, driver):
        route = RouteSelection(driver)
        
        route.input_two_different_addresses_for_route()
        route.click_optimal_tab()

        active_tab = route.check_tab_is_active()
        expected_active_tab = SelectRouteTab.optimal_tab
        price_and_time_msg = route.check_message()
        expected_price_and_time_msg = Message.optimal_tab_msg

        assert active_tab == expected_active_tab
        assert price_and_time_msg == expected_price_and_time_msg

        route.click_fast_tab()
        active_tab = route.check_tab_is_active()
        expected_active_tab = SelectRouteTab.fast_tab
        price_and_time_msg = route.check_message()
        expected_price_and_time_msg = Message.active_tab_msg

        assert active_tab == expected_active_tab
        assert price_and_time_msg == expected_price_and_time_msg


    @allure.title('Переключение на вид маршрута "Свой"')   
    @allure.description('При переключении на вид маршрута "Свой" происходит смена активного таба и становятся активны типы передвижения ')
    @pytest.mark.parametrize("type", RouteSelection.TYPES_OF_MOVEMENT)
    def test_your_own_route_type(self, driver, type):
        route = RouteSelection(driver)
        
        route.input_two_different_addresses_for_route()
        route.click_your_own_tab()

        active_tab = route.check_tab_is_active()
        expected_active_tab = SelectRouteTab.your_own_tab

        assert  active_tab == expected_active_tab

        active_type_of_movement = route.check_types_of_movement_are_active(type)

        assert active_type_of_movement


    @allure.title('Проверка кнопки "Вызвать такси"')
    @allure.description('При выборе вида маршрута "Быстрый" активна кнопка "Вызвать такси"')
    def test_call_a_taxi_button(self, driver):
        route = RouteSelection(driver)
        
        route.input_two_different_addresses_for_route()
        route.click_fast_tab()
        
        call_a_taxi_button = route.check_call_a_taxi_button()

        assert call_a_taxi_button.is_displayed()


    @allure.title('Проверка кнопки "Забронировать"')
    @allure.description('При выборе вида маршрута "Свой" и типа передвижения "Драйв" активна кнопка "Забронировать"')
    def test_reserve_button(self,driver):
        route = RouteSelection(driver)
        
        route.input_two_the_same_addresses_for_route()
        route.click_your_own_tab()
        route.click_driver_type()
        reserve_button = route.check_reserve_button()

        assert reserve_button.is_displayed()

