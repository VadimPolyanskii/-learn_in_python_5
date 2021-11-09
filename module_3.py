# Модуль 3


lst = [3, 5, 6, 8, 10, 245, 310]

new_lst = list(map(lambda x: x * 5 if x <= 10 else x + 5, lst))