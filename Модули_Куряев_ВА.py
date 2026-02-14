# Задание 1
from datetime import datetime

current_time=datetime.now()
print(current_time)

# Задание 2
import random

random_list=[]
random_list=[random.randint(1,101) for i in range(101)]
randomer_number=random.choice(random_list)
print(randomer_number)

# Задание 3 
import random

from matplotlib import pyplot as plt

number_a=range(1,13)
number_b=[random.randint(0,1000) for i in range(1,13)]
plt.plot(number_a,number_b)
plt.show()

# Задание 4
# не получилось сделать

# Задание 5
# не получилось сделать 

# Задание 6
# не получилось сделать

# Задание 7
# не получилось сделать

# Задание 8
import random

lowercase_letters=["a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p","q","r","s","t","u","v","w","x","y","z"]
uppercase_letters=["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
pass_len=int(input("Какую длину пароля вы хотите? "))
password=[]
# дальше не получилось