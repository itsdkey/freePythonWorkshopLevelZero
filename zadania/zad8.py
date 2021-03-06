"""
        Temat 8: Tuples

Przykłady
1. Stwórz i wyświetl tuple,
a) za pomocą zwykłych nawiasów
b) bez nawiasów (tzw. packing)
c) za pomocą klasy tuple()
"""
print('### zadanie 1')

print('#### punkt a')

my_tuple = (1, 2)
print(my_tuple)

print('#### punkt b')
my_variable = 203
my_other_variable = 'test for tuples'
my_tuple = my_variable, my_other_variable
print(my_tuple)

print('#### punkt c')
my_iterable = [i for i in range(10, 30, 2)]
my_tuple = tuple(my_iterable)
print(my_tuple)


"""
2. Wykonaj tzw. unpacking na tupli (1, 2, 'test', {'test': 'value'})
"""
print('### zadanie 2')
my_tuple = (1, 2, 'test', {'test': 'value'})
a, b, c, d = my_tuple
print(f'{a=} {b=} {d=} {c=}')


"""
3. Scal dwie tuple
"""
print('### zadanie 3')
temp = (1, 2) + (3, 4)
print(temp)


"""
4. Stwórz tuple, która będzie zawierać 3 razy po każdym elemencie z tupli:
    (1, 'test', {'test', 'value'})
"""
print('### zadanie 4')
temp = (1, 'test', {'test', 'value'}) * 3
print(temp)


"""
5. Stwórz funkcję która zwróci więcej niż 1 wartość
"""
print('### zadanie 5')


def foo():
    return 'test', 100


print(foo())


"""
        Zadania

1. Stwórz tuple i ją wyświetl
"""


"""
2. Stwórz funkcję, która przyjmie parametr N.
    Funkcja powinna zwrócić:
        2x powielone N jeśli N jest podzielne przez 2,
        3x powielone N jeśli N jest podzielne przez 5,
        5x powielone N jeśli N jest podzielne przez 10,
Przykłady:
N = 4
wynik: 4, 4
N = 15
wynik: 15, 15, 15
N = 20
wynik: 20, 20, 20, 20, 20
"""


"""
3. Stwórz tuple i wyświetl tuple składającą się z elementów 
    pod nieparzystymi indexami
Przykład:
my_tuple = (1, 10, 23, 'test', {'test': 'value'}, 'to jest przyklad zdania')
wynik: (10, 'test', 'to jest przykład zdania')
"""


"""
4. Stwórz 3-elementową tuple i funkcję która przyjme 3 parametry.
    Następnie przekaż te elementy do funkcji za pomocą operacji unpacking
"""


"""
5. Stwórz funkcję która przyjmie nieznaną liczbę parametrów pozycyjnych
    i wypisze:
        'nieparzysta liczba parametrów' jeśli podana liczba parametrów
            jest nieparzysta
        'parzysta liczba parametrów' jeśli podana liczba parametrów
            jest parzysta
"""


"""
6. Stwórz funkcję która przyjmuje następujące parametry:
    a - tuple z elementami
    b - index
    Następnie zwróc element pod danym indexem
"""


"""
7. Stwórz tuple na podstawie danych podanych przez użytkownika oddzielonych 
    spacjami. Następnie przyjmij paramtr od użytkownika i sprawdz czy podana
    wartość jest w tupli. Wyświetl 'jest' jeśli jest, a 'nie ma' jeśli wartość
    nie została znaleziona.
"""