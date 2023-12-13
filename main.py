backpack = []  #рюкзак
total_weight = 0  #общий вес в рюкзаке
initial_survival_points = 10 #изначальное количество очков
max_backpack = 9 #максимальный размер рюкзака (3*3)
total_survival_points = initial_survival_points  # Изначальное количество очков выживания
inventory = [['empty' for _ in range(3)] for _ in range(3)]  # Двумерный "инвентарь"


items = [
    ('r', 3, 25),
    ('p', 2, 15),
    ('a', 2, 15),
    ('m', 2, 20),
    ('i', 1, 5),
    ('k', 1, 15),
    ('x', 3, 20),
    ('t', 1, 25),
    ('f', 1, 15),
    ('d', 1, 10),
    ('s', 2, 20),
    ('c', 2, 20)
]


#сортировка предметов по их весу в возрастающем порядке и по их ценности в убывающем порядке
sorted_items = sorted(items, key = lambda x: (x[1], -x[2]))

#добавляем остальные предметы
for item in sorted_items:
    if total_weight + item[1] <= max_backpack:
        backpack.append(item)
        total_weight += item[1]
        total_survival_points += item[2]
    else:
        total_survival_points -= item[2]

#заполняем "инвентарь"
for j in range(len(backpack)):
    x = j // 3
    y = j % 3
    inventory[x][y] = backpack[j][0]
    inventory[2][0] = backpack[5][0]
    inventory[2][1] = backpack[6][0]
    inventory[2][2] = backpack[6][0]

#проверка, что итоговое количество очков выживания положительно
if total_survival_points > 0:
    print('Итоговый инвентарь (3*3):')
    for row in inventory:
        print(row)
    print(f'Итоговые очки выживания: {total_survival_points}')
else:
    print('Решений нет. Итоговое количество очков отрицательное')