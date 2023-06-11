import numpy as np
number = np.random.randint(1,101) #Загадываем число от 1 до 101
count = 0 #Вводи счётчик
while True:
    count += 1 #Подсёт попыток
    predict_number = int(input("Угадай число от 1 до 101")) #Ввод с  клавиатуры
    if predict_number > number:
        print('Число должно быть меньше')
    elif predict_number < number:
        print('Число должно быть больше')
    else:
        print(f'Вы угадали число! Это число {number}, за {count} попыток')
        break