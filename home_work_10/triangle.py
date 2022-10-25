# Класс треугольника. Методы:
#   __init__            : инициализация функции, имеется 3 стороны, провера на существование проходит автоматически.
#   __str__             : возвращает строку с проверкой на треугольник.
#   exists              : проверка на существование треугольника
#   type_of_triangle    : возвращает тип треугольника: равносторонний, равнобедренный, прямоугольный и обычный.
#   perimeter           : выводит периметр треугольника.


class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        """
            Инициализация треугольника. Параметры класса:
            --- side1, side2, side3 - float, 3 стороны треугольника.
            --- exists : проверка на существование треугольника, значение  метода self.exists()
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.exists = self.exists()

    def __str__(self):

        """
            Метод возврата описания объекта после проверки на существование треугольника.

            return : строка в зависимости от проверки. Если это треугольник - дополнительно выводится его тип.
        """

        if self.exists:
            return f"Triangle with sides: {self.side1}, {self.side2}, {self.side3}. {self.type_of_triangle()}"

        else:
            return f"Triangle does not exist."

    def exists(self):

        """
            Метод проверки на существование треугольника.

            return : boolean, результат проверки.
        """

        if self.side1 + self.side2 > self.side3 \
                and self.side1 + self.side3 > self.side2 \
                and self.side2 + self.side3 > self.side1:
            return True
        else:
            return False

    def type_of_triangle(self):

        """
            Метод вывода типа треугольника, если он существует.

            return : строка с названием типа треугольника.
        """

        if self.side1 == self.side2 == self.side3:
            return "Your triangle is equilateral."

        elif self.side1 == self.side2 or self.side1 == self.side3  or self.side2 == self.side3:
            return "Your triangle is isosceles."

        elif pow(self.side1, 2) + pow (self.side2, 2) == pow(self.side3, 2) or \
                pow(self.side1, 2) + pow(self.side3, 2) == pow(self.side1, 2) or \
                pow(self.side3, 2) + pow(self.side2, 2) == pow(self.side1, 2):
            return "Your triangle is rectangular."

        else:
            return "Your triangle is simple."

    def perimeter(self):

        """
            Метод вывода периметра треугольника.
        """

        if self.exists:
            perimeter = self.side1 + self.side2 + self.side3
            print(f'Perimeter: {perimeter}')
