# Задание №1
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Задание №2
# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

from typing import List

# Запись информации справочника
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print("Файл не найден. Введите данные в справочник\n")
        return []

# Просмотр данных в справочнике
def show_data_edit(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        print(data.read())

def show_data(data: list):
    for line in data:
        print(line)

# Сохранение данных в справочник
def save_data(file):   
    print("Введите данных контакта ")
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f"{surname}, {name}, {patronymic}, {phone_number}\n")

# Поиск по справочнику
def search_data(contacts: List[str]):
    search_str = input("Введите имя для поиска: ")
    founted = []
    for contact in contacts:
        if search_str.lower() in contact.split(", ")[1].lower():
            founted.append(contact)
    return founted

# Редактирование справочника
def edit_data(file):
    with open(file, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
        print("")
        index_delete_data = int(input("Введите номер строки для редактирования: "))
        tel_book_lines = tel_book.split("\n")
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(", ")
        print(elements, tel_book)
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        surname = elements[0]
        if len(surname) == 0:
            surname = elements[1]
        if len(name) == 0:
            surname = elements[2]
        if len(patronymic) == 0:
            surname = elements[3]
        if len(phone_number) == 0:
            phone_number = elements[4]
            edited_line = (f"{surname}, {name}, {patronymic}, {phone_number}")
            tel_book_lines[index_delete_data] = edited_line
            print(f"Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n")
            with open(file, "w", encoding='utf-8') as f:
                f.write('\n'.join(tel_book_lines))

# Удаление позиции в справочнике
def delete_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
        index_delete_data = int(input('Введите номер строки для удаления: '))
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f'Удалена запись: {del_tel_book_lines}\n')
        with open(file_name, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))

    
# Клонирование позиции
def clone_data(file, file_name_clone):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_number = int(input("\nВведите номер строки для копирования: "))
        if 0 < line_number <= len(lines):
            with open(file_name_clone, 'w', encoding='utf-8') as f_clone:
                f_clone.write(lines[line_number - 1])
                print("\nСтрока успешно скопирована в другой файл.\n")
        else:
            print("\nНекорректный номер строки.")

def main():
    file_name = "phone_directory.txt"
    file_name_clone = "phone_directory_clone.txt"
    
    flag = True
    while flag:
        
        print('\n0 - Выход')
        print('1 - Запись в файл')
        print('2 - Показать записи')
        print('3 - Найти запись')
        print('4 - Изменить запись')
        print('5 - Удалить запись')
        print('6 - Копирование данных')
        print("")
        answer = input("Выберите действия: ")
        
        if answer == "0":
            flag = False
        
        elif answer == "1":
            save_data(file_name)
        
        elif answer == "2":
            show_data_edit(file_name)
        
        elif answer == "3":
            data = read_file(file_name)
            founted_data = search_data(data)
            show_data(founted_data)
        
        elif answer == "4":
            edit_data(file_name)
        
        elif answer == "5":
            delete_data(file_name)
        
        elif answer == "6":
            clone_data(file_name, file_name_clone)
            data = read_file(file_name_clone)
            show_data(data)
            
if __name__ == '__main__':
    main()