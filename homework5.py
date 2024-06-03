immutable_var = (1, 2, "name", False)
print('Есть кортеж:', immutable_var)
print('Попробуем изменить значение последнего элемента в кортеже на True командой immutable_var[3] = True')
try:
    immutable_var[3] = True
except:
    print('Нельзя изменить часть кортежа, операция не выполнена!')
    print('Кортеж остался неизменным, вывожу на экран:', immutable_var)

mutable_list = [1, 'string', True, 56]
print('Есть список:', mutable_list)
new_element = input('Введите любое слово:')
mutable_list.append(new_element)
print('Добавляю ваш элемент в конец списка, получаем:', mutable_list)