import pytest


class TestExample:
    def test_tuple_len(self):
        a = (1, 2, 3, 4, 5)
        assert len(a) == 5, "Длина кортежа не равна 5"

    def test_tuple_min(self):
        a = (1, 2, 3, 4, 5)
        assert min(a) == 1, "Минимальный элемент кортежа не равен 1"

    numbers = [-10, -5, 0, 5, 10]

    @pytest.mark.parametrize("n", numbers)
    def test_tuple_max(self, n):
        a = (1, 2, 3, 4, 5)
        assert n % max(a) == 0, "Остаток деления n на максимальный элемент кортежа не равен нулю"

    def test_float_1(self):
        n = 1.25
        m = int(n)
        assert n - m == 0.25, "Дробная часть числа n не равна 0.25"

    def test_float_2(self):
        n = 2.95
        n = int(n * 10)
        assert (n % 10) == 9, "Первая цифра числа n после десятичной точки не равна 9"

    def test_float_3(self):
        a = 1.75
        b = "0.25"
        try:
            assert a + b == 2, "Сумаа чисел a и b не равна 2"
        except TypeError:
            assert a + float(b) == 2, "Сумаа чисел a и b не равна 2"
