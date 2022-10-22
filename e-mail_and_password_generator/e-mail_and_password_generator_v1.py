import re
import random

# file have invisible symbols move to the next line
# в файле есть невидимые символы переноса строки
text_open = open('task_test.txt', 'r')

text = text_open.read()

# convert string to list, separator = , and space
# конвертируем строку в список, разделитель запятая и пробел после нее
list1 = text.split(', ')

# delete headline from list1 and save in var
# удаляем заголовки и сохраняем их в переменную
headline = list1.pop(0), list1.pop(0), list1.pop(0), list1.pop(0), list1.pop(0)

# convert tuple to list for add elements
# конвертируем кортеж в список, чтобы потом добавлять в него элементы
headline = list(headline)

# save in var 4 elem without symbol move to the next line
# сохраняем в переменную 4 элемент заголовка без символа переноса строки
headline[4] = 'CITY'

# add to end list elem PASSWORD and symbol move to the next line
# добавляем в конец списка элемент PASSWORD и символ переноса строки
headline.append('PASSWORD\n')

# empty list for add name and last name
# список имен и фамилий, который будем набивать и потом подадим в функцию
list_input = []

# add name and last name to list_input
# набиваем список имен и фамилий
j = 0
while j < len(list1):
    current_name = list1[j]
    last_name = list1[j + 1]

    # phone number current person
    # номер телефона текущего человека
    current_number = list1[j + 2]

    current_city = list1[j + 3]

    # conditions: phone number = 7 numeral, name, last name, city not empty
    # условия - номер из 7 цифр, имя, фамилия и город не пустые
    if re.findall(r'\d{7}', current_number) and current_name and last_name \
            and current_city:

        # second check - if name or last name = N0_NAME - delete?
        # вторая проверка - если имя или город = N0_NAME - убрать?
        if current_name == 'NO_NAME' or current_city == 'NO_NAME' or \
                current_name.islower() or last_name.islower():

            # if no then save to var 'qwerty' + str(j)
            # если нет, то записываем вместо фио человека данные
            current_person = ['qwerty' + str(j), 'qwerty' + str(j)]

        # if all right, then save to var name current person
        # если все в порядке, то мы записываем в переменную фио текущего чела
        else:
            current_person = [list1[j], list1[j + 1]]
    else:
        # if no, then save to var qwerty
        # если нет, то записываем вместо фио чела данные для заглушки
        current_person = ['qwerty' + str(j), 'qwerty' + str(j)]

    # add name and laast name current person to list_input
    # добавляем имя и фамилию текущего человека в общий список
    list_input.append(current_person)

    # name person repeat every 4 elem
    # у нас имя каждого человек повторяется через 4 элемента
    j += 4


# to test - list name and last name for generate e-mail
# для теста - список фио, по которым будут генериться e-mail
# print(list_input)

def email_gen(list_input2):
    # func for generate e-mail
    # функция, которая генерирует e-mail
    emails = []
    for i in list_input2:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


# save to var result func, input = list with name and last name, output -
# list with generate e-mail
# записываем в переменную результат работы функции, в которую подали
# список ФИО, а на выходе будет список сгенеренных e-mail
all_emails = email_gen(list_input)


def generate_password():
    """func for generate password with conditions:
    1) password length >= 12 symbols
    2) password have 1 Uppercase char
    3) password have 1 lowercase char
    4) password have 1 digit
    5) password have 1 special char"""

    '''Функция, которая генерирует пароль со следующими условиями:
    1) Пароль содержит не менее 12 символов
    2) Пароль содержит хотя бы одну заглавную букву
    3) Пароль содержит хотя бы одну строчную букву
    4) Пароль содержит хотя бы одну цифру
    5) Пароль содержит хотя бы один спецсимвол'''

    # base for work
    # Базы, которые будем использовать

    numeral = '1234567890'
    lower_char = 'abcdefghijklmnopqrstuvwxyz'
    upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_char = '!@#$%^&*()-+'
    all_symbols = numeral + lower_char + upper_char + special_char

    pass_len = 12

    """1 symbol = random from numeral, 2 symbol = random from lower_char, 
    3 symbol = random from upper_char, 4 symbol = random from special_char, 
    other symbols = random from all_symbols"""
    ''' логика следующая: первым символом делаем случайный символ из цифр, 
    второй из строчных букв, третий из заглавных букв, четвертый из 
    спецсимволов, а остальные 8 делаем так - суммируем все базы в одну и 
    оттуда берем случайный символ '''
    password = random.choice(numeral) + random.choice(
        lower_char) + random.choice(upper_char) + random.choice(
        special_char)

    # до тех пор, пока длина пароля меньше, чем надо
    while len(password) < pass_len:
        # add to password random symbol
        # добавляем к нему случайные символы из суммарной базы
        password += random.choice(all_symbols)
    return password


# add elements in result_list, 1, 4 etc. elem = e-mail and name and last
# name from all_emails, other elements from list1
# далее будем набивать наш итоговый список - первый, 4 и т.д. элемент это 
# мыло из сгенеренного списка, остальное из начального файла 
result_list = []

# add headline
# добавляем заголовки
for n in range(0, 6):
    result_list.append(headline[n])

# count for input list
# счетчик для изначального списка
j = 0

# count for e-mail
# счетчик для e-mail
k = 0

while j < len(list1):
    result_list.append(all_emails[k])
    result_list.append(list1[j])
    result_list.append(list1[j + 1])
    result_list.append(list1[j + 2])

    # delete latest symbol = \n
    # убираем последний символа из элемента - это символ переноса строки \n
    list1[j + 3] = list1[j + 3][:-1]

    # add city
    # теперь уже добавляем - это у нас город
    result_list.append(list1[j + 3])

    # add latest password and symbol \n
    # добавляем в конце пароль и символ переноса строки
    result_list.append(generate_password() + '\n')

    k += 1
    j += 4

# check all elements to result_list, if e-mail have qwerty, then this e-mail
# and next 5 elem delete from result_list and add in error_list
# пробегаеся по элементам итогового списка и если у нас в e-mail есть
# qwerty, то мы этот e-mail и 5 последующих элементов удаляем из этого
# списка и добавляем в список с ошибочными

# list with error string
# список ошибочных строк
error_list = []
m = 0
while m < len(result_list):
    current_elem = result_list[m]

    # if current element have qwerty
    # если в текущем элементе есть qwerty
    if re.search(r'qwerty', current_elem):
        # print for test
        # выводим его для теста
        # print(current_elem)

        # then current element (e-mail) = empty
        # тогда у нас текущий элемент (это e-mail), он пустой
        result_list[m] = ''

        # and element after 4 (password) too empty
        # и элемент, который идет через 4 после него (это пароль) тоже пустой
        result_list[m + 5] = '\n'

        n = 0
        # repeat 5 iter, for add to error_list next 5 error elements
        # повторяем 5 раз, чтобы добавить в список следующие 5 ошибочных элем
        while n < 6:
            # add element to error_list
            # заносим элемент в список с ошибочными
            error_list.append(result_list[m])

            # delete to result_list
            # удаляем из основного списка
            result_list.pop(m)
            n += 1

    m += 1

# convert list to string
# переводим список в строку
itog_str = ", ".join(result_list)

# replace \n,space to \n
# заменяем символ переноса строки, запятую после него и пробел на символ
# переноса строки
itog_str = itog_str.replace('\n, ', '\n')

# close txt
# закрываем наш файл с исходными данными
text_open.close()

# write to result.txt
# записываем инфу в файл result
open_result = open('result.txt', 'w')  # записываем инфу в файл
open_result.write(itog_str)
open_result.close()

# print to test result.txt
# печатаем для теста содержимое файла result

# file have invisible symbols move to the next line
# открываем файл - в нем есть невидимые символы переноса строки
open_result = open('result.txt', 'r')
result_text = open_result.read()
open_result.close()

# convert error_list to string
# переводим список с ошибочными в строку
error_str = ", ".join(error_list)

# replace \n,space to \n
# заменяем символ переноса строки, запятую после него и пробел на символ
# переноса строки
error_str = error_str.replace('\n, ', '\n')

# write to error_list
# записываем инфу в файл error_list
open_error_list = open('error_list.txt', 'w')
open_error_list.write(error_str)
open_error_list.close()
