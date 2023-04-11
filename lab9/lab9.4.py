def calculate_delivery_cost(street, price):
    # Список улиц в квадрате
    square_streets = ["Аль-Фараби", "Саин", "Райымбек", "Достык"]
    # Проверяем, находится ли улица в квадрате
    if street in square_streets:
        # Если стоимость товара меньше 10 тыс., то стоимость доставки равна 500 тг
        if price < 10000:
            delivery_cost = 500
        # Иначе доставка бесплатна
        else:
            delivery_cost = 0
    # Если улица за пределами квадрата
    else:
        # Если стоимость товара меньше 10 тыс., то стоимость доставки равна 1000 тг
        if price < 10000:
            delivery_cost = 1000
        # Иначе стоимость доставки тоже 1000 тг
        else:
            delivery_cost = 1000
    # Возвращаем общую стоимость доставки
    return delivery_cost


street = "Толе Би"
price = 7100

delivery_cost = calculate_delivery_cost(street, price)
print(f"Стоимость доставки для улицы {street} и товара стоимостью {price} тг: {delivery_cost} тг")