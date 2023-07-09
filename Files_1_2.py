from pprint import pprint

file_path = "recipes.txt"


def get_shop_list_by_dishes(dishes,person_count):
    order_sheet = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                ing["кол-во"] *= person_count
                pop_key = ing.pop("Ингридиент")
                order_sheet[pop_key] = ing

    return order_sheet


with open(file_path,'r',encoding = "utf-8" ) as f:
    cook_book = {}
    for line in f:
        name_recipe = line.strip()
        emp_count = int(f.readline())
        employ = []
        for i in range(emp_count):
            emp = f.readline().strip()
            ingridient,qual,uom, = emp.split(' | ')

            employ.append({
                       'Ингридиент': ingridient,
                       'кол-во': int(qual),
                       'ед.изм': uom

                           })
        f.readline()
        cook_book[name_recipe] = employ

print("--------------------Task_1--------------------\n")
pprint(cook_book)
print("--------------------Task_2------------------------\n")
pprint(get_shop_list_by_dishes(['Омлет','Запеченный картофель'],2))

