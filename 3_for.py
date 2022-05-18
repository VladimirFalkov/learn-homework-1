"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sold_items = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def total_sold(phones_sold):
    items_sum = 0
    for solds in phones_sold:
        items_sum += solds
    return items_sum

total_all_phones = 0
count_all_phones = 0
for items  in sold_items:
    total = total_sold(items['items_sold'])
    total_all_phones += total
    count_all_phones += len(items["items_sold"])
    print(f'Cуммарное количество продаж {items["product"]}: {total}')
    print(f'Cреднее количество продаж для {items["product"]}: {round(total / len(items["items_sold"]), 2)} ')
print(f"Cуммарное количество продаж всех товаров: {total_all_phones}")
print(f'Cреднее количество продаж всех товаров: {total_all_phones/count_all_phones}')
