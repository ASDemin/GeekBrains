'''
2. Создайте модуль. В нем создайте функцию,
которая принимает список и возвращает из него случайный элемент.
Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
'''
import random
list =[1,2,3,4]
def rnd():
    dlina=len(list)
    number=random.randint(1,dlina)
    if list==null:
        e='None'
    else:    
        e=(list[number-1])
    
    return e

print (rnd())
