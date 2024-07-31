import os
from pprint import pprint

print('TASK1\n')

file_name = "recipes.txt"

def get_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        while True:
            meal = file.readline().strip()
            if not meal:  # Если достигли конца файла
                break
            cook_book[meal] = []
            ingredients_quantity = int(file.readline().strip())
            for item in range(ingredients_quantity):
                ingredient_dict = {}
                ingredient = file.readline().strip().split(' | ')
                ingredient_dict['ingredient_name'] = ingredient[0]
                ingredient_dict['quantity'] = int(ingredient[1])
                ingredient_dict['measure'] = ingredient[2]
                cook_book[meal].append(ingredient_dict)
            file.readline()  # Пропускаем пустую строку
    return cook_book

outcome = get_cook_book(file_name)
pprint(outcome)

print('TASK2\n')

from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо {dish} отсутствует в кулинарной книге")
    return shop_list

cook_book = get_cook_book(file_name)

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

pprint(shop_list)

print('TASK3')

def read_files_in_directory(files):
    file_contents = {}
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()
            file_contents[filename] = content
    return file_contents

def write_combined_file(output_file, file_contents):
    sorted_files = sorted(file_contents.items(), key=lambda item: len(item[1]))  # Сортируем файлы по количеству строк
    with open(output_file, 'w', encoding='utf-8') as out_file:  # Открываем результирующий файл для записи
        for filename, content in sorted_files:  # Проходим по каждому файлу в отсортированном порядке
            out_file.write(f"{filename}\n")  # Записываем имя файла
            out_file.write(f"{len(content)}\n")  # Записываем количество строк в файле
            out_file.writelines(content)  # Записываем все строки файла
            out_file.write("\n")  # Добавляем пустую строку между файлами

files = ["1.txt", "2.txt", "3.txt"]
output_file = "result.txt"

file_contents = read_files_in_directory(files)
write_combined_file(output_file, file_contents)

print(f"Содержимое файлов объединено в файл {output_file}")

