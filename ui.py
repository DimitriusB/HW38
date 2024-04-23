from logger import *


def user_interface():
    with open('Phonebook.txt', 'a', encoding='utf-8'):  # создаем файл если его нет
        pass
    cmd = None
    while cmd != '6':
        print('Меню:\n'
              '1. Запись контакта\n'
              '2. Вывести данные на экран\n'
              '3. Поиск контакта\n'
              '4. Изменение контакта\n'
              '5. Удаление контакта\n'
              '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        if cmd == '1':
            add_contact()
        elif cmd == '2':
            print_contacts()
        elif cmd == '3':
            search_contact()
        elif cmd == '4':
            change_contact()
        elif cmd == '5':
            delete_contact()
        elif cmd == '6':
                print('До свидания))')
