import os
import sys
import shutil
import django
import numpy

FILE_NAME = 'schet.txt'
FILE_NAME_1 = 'spisok.txt'

# Инициализация начального счета пользователя
account_balance = 0
purchase_history = []
orders = []
spisok = []

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. рабочая дериктория')
    print('13. выход')
    print('14. добавить покупку')
    print('15. История покупок')
    print('16. Сохранить содержимое рабочей директории в файл')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        folder_name = input('Введите имя новой папки: ')
        folder_path = os.path.join(os.getcwd(), folder_name)
        try:
            os.mkdir(folder_path)
            print(f'Папка "{folder_name}" создана успешно.')
        except FileExistsError:
            print(f'Папка "{folder_name}" уже существует.')

    elif choice == '2':
        target_name = input('Введите имя файла или папки для удаления: ')
        target_path = os.path.join(os.getcwd(), target_name)
        if os.path.exists(target_path):
            if os.path.isdir(target_path):
                os.rmdir(target_path)
                print(f'Папка "{target_name}" удалена успешно.')
            else:
                os.remove(target_path)
                print(f'Файл "{target_name}" удален успешно.')
        else:
            print(f'"{target_name}" не существует.')

    elif choice == '4':
        print(os.listdir())


    elif choice == '5':
        # Получаем список элементов в текущей директории
        items = os.listdir()
        # Фильтруем только папки (директории)
        folders = [item for item in items if os.path.isdir(item)]
        # Выводим список папок
        for folder in folders:
            print(folder)


    elif choice == '6':
        # Получаем список элементов в текущей директории
        items = os.listdir()
        # Фильтруем только файлы (не папки)
        files = [item for item in items if os.path.isfile(item)]
        # Выводим список файлов
        for file in files:
            print(file)

    elif choice == '7':
        if os.name == 'posix':
            # Получение информации об операционной системе на UNIX-подобных системах
            print('Операционная система: UNIX-подобная')
        elif os.name == 'nt':
            # Получение информации об операционной системе на Windows
            print('Операционная система: Windows')
        else:
            print('Неизвестная операционная система.')

    elif choice == '8':
        creator = "Теодор Страбенгальский"
        print(f'Программа создана {creator}.')

    elif choice == '9':
        import random
        from datetime import datetime

        # Известные люди и их даты рождения
        people = {
            'John': '02.01.1988',
            'Alice': '15.04.1992',
            'Bob': '30.07.1985',
            'Emma': '18.12.1976',
            'Mike': '09.06.1999',
            'Kate': '21.03.1983',
            'Tom': '11.11.1990',
            'Linda': '25.09.1979',
            'David': '07.05.1981',
            'Sophia': '29.08.1995'
        }

        while True:
            # Выбираем 5 случайных людей
            random_people = random.sample(list(people.keys()), 5)

            correct_count = 0  # Счетчик правильных ответов

            for person in random_people:
                birthday = datetime.strptime(people[person], '%d.%m.%Y')
                formatted_birthday = birthday.strftime('%d %B %Y')

                user_input = input(f"Введите дату рождения {person}: ")

                try:
                    user_birthday = datetime.strptime(user_input, '%d.%m.%Y')
                    formatted_user_birthday = user_birthday.strftime('%d %B %Y')

                    if user_birthday == birthday:
                        correct_count += 1
                    else:
                        print(f"Неверно. Правильная дата рождения {person}: {formatted_birthday}")
                except ValueError:
                    print("Ошибка: неверный формат даты. Введите дату в формате 'dd.mm.yyyy'.")

            incorrect_count = 5 - correct_count
            print(f"\nПравильных ответов: {correct_count}, Неправильных ответов: {incorrect_count}\n")

            restart = input("Хотите начать снова? (да/нет): ")
            if restart.lower() != 'да':
                break

    if choice == '10':
        amount = float(input('Введите сумму для пополнения счета: '))
        account_balance += amount
        print(f'Счет пополнен на {amount} рублей. Текущий баланс: {account_balance} рублей.')

        # Добавляем информацию о пополнении в список orders
        orders.append(f'Пополнение на {amount} рублей. Текущий баланс: {account_balance} рублей.')


    elif choice == '11':
        new_directory = input("Введите путь к новой рабочей директории: ")
        if os.path.exists(new_directory):
            os.chdir(new_directory)
            print(f'Текущая рабочая директория изменена на: {new_directory}')
        else:
            print(f'Директории "{new_directory}" не существует.')

    elif choice == '12':
    # Получение текущего рабочего каталога
        current_directory = os.getcwd()
        print(f"Текущий рабочий каталог: {current_directory}")


    elif choice == '13':
        with open(FILE_NAME, 'a') as f: # Открываем файл в режиме дозаписи ('a')
            for order in orders:
                f.write(f'{order}\n')

        # После сохранения в файл, можно выйти из программы
        break

    elif choice == '14':
        name = input('Введите название покупки: ')
        with open(FILE_NAME_1, 'a') as f:
            f.write(f'{name}\n')
        print(f'Покупка "{name}" добавлена в историю.')


    elif choice == '15':
        if os.path.exists(FILE_NAME_1):
            with open(FILE_NAME_1, 'r') as f:
                spisok = f.readlines()
                if spisok:
                    print("История покупок:")
                    for purchase in spisok:
                        print(purchase.strip())
                else:
                    print("История покупок пуста.")
        else:
            print("История покупок пуста.")

    elif choice == '16':
        # Создаем файл listdir.txt и сохраняем содержимое рабочей директории
        with open('listdir.txt', 'w') as f:
            files = []
            dirs = []
            for item in os.listdir():
                if os.path.isfile(item):
                    files.append(item)
                elif os.path.isdir(item):
                    dirs.append(item)
            f.write('files: ' + ', '.join(files) + '\n')
            f.write('dirs: ' + ', '.join(dirs) + '\n')
        print('Содержимое рабочей директории сохранено в файл listdir.txt.')

    else:
        print('Неверный пункт меню')