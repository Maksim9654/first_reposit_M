import numpy as np
import random

def random_predict(number: int = np.random.randint(1, 101)) -> int:
    
    """ Угадываем число.
        Находим предполагаемое число, как среднее между верхней и нижней границей.
          Если предполагаемое число больше,
              то нижняя граница приравнивается предпологамому числу;
            предполагаемое число меньше,
              то верхняя граница приравнивается предпологамому числу;
            если равны - Число угадали!
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    count: int = 0 # Число попыток
    lower_bound = 1 # Нижняя граница
    upper_bound = 101 # Верхняя граница

    while True:
        count += 1
        # сумма может быть нечетная - округляем
        predict_number = int((upper_bound + lower_bound) / 2)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        if number > predict_number:
            lower_bound = predict_number
        else:
            upper_bound = predict_number

    return count
  
print(f'Количество попыток: {random_predict()}')



def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
    return score


if __name__ == "__main__":
    # RUN
  score_game(random_predict)
