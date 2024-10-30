# Модуль 9_6. Генераторы.
# =====================================================
'''Функция-генератор all_variants(text),принимает строку text
и возвращает объект-генератор, при каждой итерации которого будет возвращаться
подпоследовательности переданной строки.'''
def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j + i + 1]

a = all_variants("abc")
for i in a:
    print(i)