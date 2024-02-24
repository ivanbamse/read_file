def scather_string(cook_book, striped_line, index):
    match index:
        case 1:
            cook_book[striped_line] = []
        case 2:
            pass
        case _:
            keys_list = list(cook_book.keys())
            ingredient = striped_line.split(' | ')
            recipe_ingredient = {}
            recipe_ingredient['ingredient_name'] = ingredient[0]
            recipe_ingredient['quantity'] = int(ingredient[1])
            recipe_ingredient['measure'] = ingredient[2]
            cook_book[keys_list[len(keys_list)-1]].append(recipe_ingredient)

def get_recipes_from_file(file_name):
    cook_book = {}
    try:
        with open(file_name, "r", encoding='utf-8') as cook_book_file:
            recipe_description_index = 0
            end_of_file = False
            while not end_of_file:
                file_string = cook_book_file.readline()
                striped_line = file_string.strip()
                if file_string:
                    in_the_recipe = True if striped_line else False
                    if in_the_recipe:
                        recipe_description_index += 1
                        scather_string(cook_book, striped_line, recipe_description_index)
                    else:
                        recipe_description_index = 0
                else:
                    end_of_file = True
    except NameError:
        print(f"Неверное имя файла {file_name}")
    except FileNotFoundError:
        print(f"Файл не найден {file_name}")
    except OSError:
        print(f"Невозможно открыть файл {file_name}")
    finally:
        cook_book_file.close()
    return cook_book

def print_dishes_dict(cook_book):
    for dish, ingredients in cook_book.items():
        print(dish)
        for ingredient in ingredients:
            print(f"\t{ingredient}")

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += (ingredient['quantity'] * person_count)
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cook_book = get_recipes_from_file('recipes.txt')
    print_dishes_dict(cook_book)

    person_count = 2
    foods = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], person_count)
    print(f"\nСписок продуктов для {person_count} персон:\n")
    for food, volume in foods.items():
        print(f"{food}: {volume}")
