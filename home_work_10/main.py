# --------- Work with class Triangle --------- #

# Класс треугольника импортируется из файла "triangle.py". Детали класса написаны в его файле.

from triangle import Triangle


def input_value(name: str):

    """
        Функция проверки введенного значения пользователем на число. Функция не вернём число до тех пор, пока не будет
        введено число. Параметры:
        --- name : строка, которая обозначает название переменной, в данном примере - название стороны

        return : число
    """

    num = input(f'Enter {name}: ')
    while True:
        try:
            num = float(num)
            if num > 0:
                return num
        except Exception:
            num = input(f'It is not a wrong value! Enter {name}: ')


if __name__ == "__main__":

    side1 = input_value("first side")
    side2 = input_value("second side")
    side3 = input_value("third side")

    object1 = Triangle(side1=side1, side2=side2, side3=side3)

    print(object1)

    if object1.exists:
        object1.perimeter()
