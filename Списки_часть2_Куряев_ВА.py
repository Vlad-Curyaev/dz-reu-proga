# Задание 1
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)
# длина изменилась на 3

# Задание 2
employees = ["Майкл", "Дуайт", "Джим", "Пэм", "Райан", "Энди", "Роберт"]
index4 = employees[4]
print(len(employees))
print(employees[5])

# Задание 3
shopping_list = ["яйца", "масло", "молоко", "огурцы", "сок", "хлопья"]
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5)
print(last_element)

# Задание 4
suitcase = ["рубашка", "рубашка", "брюки", "брюки", "пижамы", "книги"]
beginning = suitcase[0:2]
print(beginning)
# в списке 2 элемента
beginning = suitcase[0:4]
middle = suitcase[2:4]
print(beginning)
print(middle)

# Задание 5
suitcase = ["рубашка", "футболка", "носки", "очки", "пижама", "книги"]
start = suitcase[:3]
print(start)

# Задание 6
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake','Jake', 'Cassie', 'Laurie']
jake_votes=votes.count('Jake')
print(jake_votes)

# Задание 7
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace' , '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

# Задание 8
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
sorted_games=sorted(games)
print(sorted_games)

# Задание 9
inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двуспальная кровать', 'двуспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка', 'королевский кровать', 'двуспальная кровать', 'односпальная кровать','односпальная кровать','односпальная кровать','односпальная кровать', 'простыни', 'простыни', 'подушка', 'подушка']
inventory_len=len(inventory)
first=inventory[0]
last=inventory[-1]
inventory_2_6=inventory[2:6]
first_3=inventory[:3]
twin_beds=inventory.count('односпальная кровать')
inventory.sort()
print(inventory_len)
print(first)
print(last)
print(inventory_2_6)
print(first_3)
print(twin_beds)
print(inventory)

