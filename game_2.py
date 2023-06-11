"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np
def random_predict(number:int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count
print(f"Количество попыток: {random_predict()}")

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 попыток 
    угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_list = []
    random_array = np.random.randint(1,101, size = 1000)
    
    for number in random_array:
        count_list.append(random_predict(number))
    score = int(np.mean(count_list))
    return score

if __name__ == '__main__':
    score_game(random_predict)