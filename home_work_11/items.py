class Item:
    """
        Суперкласс Item с основными параметрами:
        --- name : имя товара
        --- price : цена товара
        --- quantity : количество товара
        --- additional_data : словарь с дополнительными параметрами для дочерних классов
    """


    def __init__(self, name: str, price: float, quantity: int, additional_data: dict):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.additional_data = additional_data

    def __str__(self):
        additional_data_str = ""
        if self.additional_data != {}:
            for item, value in self.additional_data.items():
                additional_data_str += f"{item.title()}: {value}\n"
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity} \n{additional_data_str}"

    def return_filter_print(self):

        """
            Функция возврата словаря со список возможный типов для фильтра.

            return : список, ключ - имя параметра класса, значение - типом данных значения этого параметра
        """

        filters_list = {
            "Price": type(self.price),
            "Quantity": type(self.quantity)
        }

        if self.additional_data != {}:
            for item, value in self.additional_data.items():
                filters_list[item.title()] = type(value)

        return filters_list


class Pan(Item):
    def __init__(self, name: str, price: float, quantity: int, additional_data: dict):
        super().__init__(name, price, quantity, additional_data)
        self.size = additional_data['size']
        self.material = additional_data['material']
        self.coating = additional_data['coating']

        self.additional_data = {
            "Size": self.size,
            "Material": self.material,
            "Coating": self.coating
        }


class Pot(Item):
    def __init__(self, name: str, price: float,
                 quantity: int, additional_data: dict):
        super().__init__(name, price, quantity, additional_data)
        self.size = additional_data['size']
        self.capacity = additional_data['capacity']
        self.material = additional_data['material']
        self.cover_included = additional_data['cover_included']

        self.additional_data = {
            "Size": self.size,
            "Capacity": self.capacity,
            "Material": self.material,
            "Cover included": self.cover_included
        }


class Knife(Item):
    def __init__(self, name: str, price: float, quantity: int,
                 additional_data: dict):
        super().__init__(name, price, quantity, additional_data)
        self.material = additional_data['material']
        self.length = additional_data['length']
        self.handle_material = additional_data['handle_material']

        self.additional_data = {
            "Material": self.material,
            "Length": self.length,
            "Handle material": self.handle_material
        }


class Plate(Item):
    def __init__(self, name: str, price: float, quantity: int, additional_data: dict):
        super().__init__(name, price, quantity, additional_data)
        self.size = additional_data['size']
        self.material = additional_data['material']

        self.additional_data = {
            "Size": self.size,
            "Capacity": self.material,
        }


class Cup(Item):
    def __init__(self, name: str, price: float, quantity: int, additional_data: dict):
        super().__init__(name, price, quantity, additional_data)
        self.capacity = additional_data['capacity']
        self.material = additional_data['material']

        self.additional_data = {
            "Capacity": self.capacity,
            "Material": self.material
        }
