from roman import *
t = input('Введите числа и программа перведёт их ').split(' ')
print(t)
for i in t:
    try:
        i=int(i)
        print(i, '->',int_to_roman(i))
    except ValueError:
        print(i, '->' ,roman_to_int(i))

