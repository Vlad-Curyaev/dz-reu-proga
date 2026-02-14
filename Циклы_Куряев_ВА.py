# Задание 1
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
print("="*20)    
for game in sport_games:
    print(game)

# Задание 2
promise="I will not chew gum in class"
for i in range(5):
    print(promise)

# Задание 3
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    print(student)
    students_period_B.append(student)
print(students_period_B)


# Задание 4
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dogs in dog_breeds_available_for_adoption:
    print(dogs)
    if dogs==dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break

# Задание 5 
scoops_sold = 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for sales in sales_data:
    for sale in sales:
        scoops_sold+=sale
print(scoops_sold)

# Задание 6
single_digits=range(0,10)
squares=[]
for digit in single_digits:
    print(digit)
    squares.append(digit**2)
    cubes=[digit**3 for digit in single_digits]
print(squares)
print(cubes)

