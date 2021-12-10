# Тестируем функции из модулей
# Модуль 1
def f(a, b):
    summ = a + b
    return summ


# Тест 1
def test_f():
    assert f(15, 30) == 45


# Модуль 2
def f2(a, b):
    return a * b


# Тест 2
def test_f2():
    assert f2(10, 5) == 50


# Модуль 2
def f3(a, b):
    return a - b


# Тест 3
def test_f3():
    assert f3(10, 20) == -10


# Модуль 3
lst = [3, 5, 6, 8, 10, 245, 310]
new_lst = list(map(lambda x: x * 5 if x <= 10 else x + 5, lst))


# Тест 4
def test_lst():
    assert new_lst == [15, 25, 30, 40, 50, 250, 315]


def dev(a,b):
    return a ** b


# Тест 5
def test_dev():
    assert dev(4, 2) == 16
