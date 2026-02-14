# Задание 1
def f_to_c(f_temp):
    c_temp=(f_temp-32)*(5/9)
    return c_temp
print(f_to_c(100))

def c_to_f(c_temp):
    f_temp=c_temp*(9/5)+32
    return f_temp
c0_in_farenheit=c_to_f(0)
print(c0_in_farenheit)

# Задание 2
def get_force(train_mass,train_acceleration):
    force=train_mass*train_acceleration
    return force
train_force=get_force(10000,20)
print("Поезд GE поставляет "+str(train_force)+" ньютонов силы")

def get_energy(bomb_mass,c=3*10**8):
    energy=bomb_mass*c**2
    return energy
bomb_energy=get_energy(1)
print("1 кг бомбы составляет "+str(bomb_energy)+" Джоулей")

def get_work(train_mass,train_acceleration,train_distance):
    work=get_force(train_mass,train_acceleration)*train_distance
    return work
train_distance=100
train_work=get_work(22680,10,train_distance)
print("Поезд выполняет "+str(train_work)+" Джоулей за "+str(train_distance)+" метров")

# Задание 3
def clothes(time):
    if time == "Утром":
        cloth = "домашняя одежда"
    elif time == "Днём":
        cloth = "уличная одежда"
    elif time == "Вечером":
        cloth = "теплая одежда"
    else:
        cloth = "домашняя одежда"
    return "У меня большой гардероб. " + time + " лучше всего подходит " + cloth+"."

print(clothes("Утром"))
print(clothes("Днём"))
print(clothes("Вечером"))
print(clothes("Ночью"))

def meal(time):
    if time=="На завтрак":
        dish="Йогурт"
    elif time=="На обед":
        dish="Суп"
    else:
        dish="Котлеты с гарниром"
    return "Мои предпочтения в еде. "+time+" лучше всего подходит " +dish+"."
print(meal("На завтрак"))
print(meal("На обед"))
print(meal("На ужин"))

# Задание 4
user_name = input("Введите свое имя!")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
greeting = "Добро пожаловать!"
error = "Логин или пароль не верный, попробуйте еще раз"
# Dmitriy_APM=1
# Angelina_APM=2
# Vasiliy_APM=3
# Ekaterina_APM=4
ARM = input("Введите свой APM!")


def workspace(ARM, user_name):
    if user_name == "Дмитрий":
        return Dmitriy_check
    if (
        (ARM == "2" and user_name == "Ангелина")
        or (ARM == "3" and user_name == "Василий")
        or (ARM == "4" and user_name == "Екатерина")
    ):
        return greeting
    else:
        return error


print(workspace(ARM, user_name))

# Задание 5
mark=input("Введите вашу оценку!")
def grade(mark):
    if 5.0>float(mark)>=4.0:
        return "Вы должны вернуть \"A\""
    elif  4.0>float(mark)>=3.0:
        return "Вы должны вернуть \"B\""
    elif  3.0>float(mark)>=2.0:
        return "Вы должны вернуть \"C\""
    elif  2.0>float(mark)>=1.0:
        return "Вы должны вернуть\"D\""
    elif 1.0>float(mark)>=0.0:
        return "Вы должны вернуть\"F\""
    else:
        return "Ошибка"
print(grade(mark))
