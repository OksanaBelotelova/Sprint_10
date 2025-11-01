import allure
from pages.base_page import BasePage

class TestWayPoints:

    @allure.title('Отрисовка маршрута')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" на карте отображаются две точки начала и конца маршрута')
    def test_waypoints_are_shown_after_entering_addresses(self, driver):
        point = BasePage(driver)

        point.enter_from_address()
        point.enter_where_address()

        point_A = point.check_point_A()
        point_B = point.check_point_B()

        assert point_A
        assert point_B

        

