#1. Создайте функцию, принимающую на вход имя,
# возраст и город проживания человека. Функция
# должна возвращать строку вида «Василий, 21 год(а),  проживает в городе Москва»

def info():
    name = input('Введите имя?')
    age = input ('Сколько Вам лет?')
    city = input ('Откуда Вы?')
    information = (name +',' +age+' года'+', проживает в городе '+ city)
    return information
print (info())
