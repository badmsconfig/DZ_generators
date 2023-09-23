import os
import random
from datetime import datetime
import shutil

FILE_NAME = 'schet.txt'
FILE_NAME_1 = 'spisok.txt'

# Инициализация начального счета пользователя
account_balance = 0
purchase_history = []
spisok = []
orders = []
total_balance = 0

while True:
    menu = """
    1. создать папку
    2. удалить (файл/папку)
    3. копировать (файл/папку)
    4. просмотр содержимого рабочей директории
    5. посмотреть только папки
    6. посмотреть только файлы
    7. просмотр информации об операционной системе
    8. создатель программы
    9. играть в викторину
    10. мой банковский счет
    11. смена рабочей директории (*необязательный пункт)
    12. рабочая директория
    13. выход
    14. добавить покупку
    15. История покупок
    16. Сохранить содержимое рабочей директории в файл
    """

    print(menu)

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
            os.rmdir(target_path) if os.path.isdir(target_path) else os.remove(target_path)
            print(f'Папка "{target_name}" удалена успешно.' if os.path.isdir(target_path) else f'Файл "{target_name}" удален успешно.')
        else:
            print(f'"{target_name}" не существует.')


    elif choice == '3':

        source_name = input('Введите имя файла или папки для копирования: ')

        source_path = os.path.join(os.getcwd(), source_name)

        if os.path.exists(source_path):

            destination_name = input('Введите путь для сохранения копии: ')

            destination_path = os.path.join(os.getcwd(), destination_name)

            try:

                if os.path.isdir(source_path):

                    if os.path.exists(destination_path):
                        # Если целевая папка уже существует, добавьте уникальное имя копии

                        destination_path = os.path.join(destination_path, f'copy_{source_name}')

                    shutil.copytree(source_path, destination_path)

                    print(f'Папка "{source_name}" успешно скопирована в "{destination_name}".')

                else:

                    shutil.copy2(source_path, destination_path)

                    print(f'Файл "{source_name}" успешно скопирован в "{destination_name}".')

            except Exception as e:

                print(f'Ошибка при копировании: {str(e)}')

        else:

            print(f'"{source_name}" не существует.')

    elif choice == '4':
        print(os.listdir())

    elif choice == '5' or choice == '6':
        items = os.listdir()
        is_dir = choice == '5'
        items_filtered = [item for item in items if os.path.isdir(item) == is_dir]
        print('\n'.join(items_filtered))

    elif choice == '7':
        print(f'Операционная система: {"UNIX-подобная" if os.name == "posix" else "Windows" if os.name == "nt" else "Неизвестная"}')

    elif choice == '8':
        creator = "Теодор Страбенгальский"
        print(f'Программа создана {creator}.')

    elif choice == '9':
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

        for _ in range(5):
            random_people = random.sample(list(people.keys()), 5)
            correct_count = 0

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



    elif choice == '10':

        try:

            amount = float(input('Введите сумму для пополнения счета: '))

            account_balance += amount

            total_balance += amount  # Обновление итоговой суммы

            print(f'Счет пополнен на {amount} рублей. Текущий баланс: {account_balance} рублей.')

            orders.append(
                f'Пополнение на {amount} рублей. Текущий баланс: {account_balance} рублей. Итоговый баланс: {total_balance} рублей.')

        except ValueError:

            print("Ошибка: введите корректную сумму для пополнения.")

    elif choice == '11':
        new_directory = input("Введите путь к новой рабочей директории: ")
        if os.path.exists(new_directory):
            os.chdir(new_directory)
            print(f'Текущая рабочая директория изменена на: {new_directory}')
        else:
            print(f'Директории "{new_directory}" не существует.')

    elif choice == '12':
        current_directory = os.getcwd()
        print(f"Текущий рабочий каталог: {current_directory}")

    elif choice == '13':
        with open(FILE_NAME, 'a') as f:
            for order in orders:
                f.write(f'{order}\n')
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

        with open('listdir.txt', 'w') as f:

            files = [item for item in os.listdir() if os.path.isfile(item)]

            dirs = [item for item in os.listdir() if os.path.isdir(item)]

            f.write('files: ' + ', '.join(files) + '\n')

            f.write('dirs: ' + ', '.join(dirs) + '\n')

        print('Содержимое рабочей директории сохранено в файл listdir.txt.')


    else:

        print('Неверный пункт меню')