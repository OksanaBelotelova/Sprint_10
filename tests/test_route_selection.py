import allure
from pages.route_selection import RouteSelection
from data import Message

class TestRouteSelection:
    
    @allure.title('Появление блока с выбором маршрута')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута')
    def test_route_selection_section(self, driver):
        route = RouteSelection(driver)

        route.enter_from_address()
        route.enter_where_address()

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