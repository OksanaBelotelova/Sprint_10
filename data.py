class URLs:
    base_url = 'https://ez-route.stand.praktikum-services.ru/'


class Addresses:
    first_address = 'Хамовнический Вал, 34'
    second_address = 'Зубовский бульвар, 37'

class Message:
    message = 'Авто Бесплатно В пути 0 мин.'
    optimal_tab_msg = 'Авто ~ 40 руб. В пути 3 мин.'
    active_tab_msg = 'Такси ~ 181 руб. В пути 3 мин.'

class SelectRouteTab:
    optimal_tab = 'Оптимальный'
    fast_tab = 'Быстрый'
    your_own_tab = 'Свой'

class TypesOfMovement:
    car = 'Машина'
    on_foot = 'Пешком'
    taxi = 'Такси'
    bicycle = 'Велосипед'
    scooter = 'Самокат'
    drive = 'Драйв'

class TariffCards:
    tariff_working = 'Рабочий'
    tariff_sleepy = 'Сонный'
    tariff_holiday = 'Отпускной'
    tariff_talkative = 'Разговорчивый'
    tariff_consolation = 'Утешительный'
    tariff_glossy = 'Глянцевый'
    tariff_working_description = 'Для деловых особ, которых отвлекаю'
    tariff_sleepy_description = 'Для тех, кто не выспался'
    tariff_holiday_description = 'Если пришла пора отдохнуть'
    tariff_talkative_description = 'Если мысли не выходят из головы'
    tariff_consolation_description = 'Если хочется свернуться калачиком'
    tariff_glossy_description = 'Если нужно блистать'
    Tariff_cards_description = {
                                'Рабочий' : 'Для деловых особ, которых отвлекают',
                                'Сонный' : 'Для тех, кто не выспался',
                                'Отпускной' : 'Если пришла пора отдохнуть',
                                'Разговорчивый' : 'Если мысли не выходят из головы',
                                'Утешительный' : 'Если хочется свернуться калачиком',
                                'Глянцевый' : 'Если нужно блистать'
                                }
    
class OrderTaxiElements:
    waiting_for_a_car_title = 'Поиск машины'
    completed_order_window_title = 'мин. и приедет'
    

