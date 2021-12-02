from pprint import pprint
import os

def get_cook_book_from_file(file):
      
    with open(file, 'r', encoding='cp1251') as f:
        cook_book = dict()
        for recipe_name in f:
            recipe = recipe_name.strip()
            counter = int(f.readline())
            food_list = []
            for lines in range(counter):
                name, quantity, item = f.readline().strip().split("|")
                food_list.append(
                    {'ingredient_name': name.strip(), 'quantity': int(quantity), 'measure': item.strip()}
                )
            cook_book[recipe] = food_list
            f.readline()
        return cook_book
def get_shop_list_by_dishes(dishes, person_count, recipe_book='recipes.txt'):

    cook_book = get_cook_book_from_file(recipe_book)
    ingredient_dict = {}
    for recipe in dishes:
        if recipe in cook_book.keys():
            for food_dict in cook_book[recipe]:
                key = food_dict['ingredient_name']
                temp = food_dict['quantity'] * person_count
                temp_dict = {'measure': food_dict['measure'], 'quantity': temp}
                if key in ingredient_dict.keys():
                    exist_dict = ingredient_dict[key]
                    temp_dict['quantity'] += exist_dict['quantity']
                ingredient_dict[key] = temp_dict
    return ingredient_dict

pprint(get_shop_list_by_dishes(['Запеченый картофель', 'Омлет'], 2))