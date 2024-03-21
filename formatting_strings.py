# -*- coding: utf8 -*-

# cтарый стиль: %
team1_num = 5
print("В команде Мастера кода участников - %s" % (team1_num),"!")

team2_num = 6
print("Итого сегодня в командах участников - %s" %(team1_num),"и",(team2_num),"!")


# более продвинутый метод
score_2 = 42
print("Команда Влшебники данных решила {0} задач".format(score_2))

team1_time = 18015.2
print("Волшебники данных решили {0} задачи за {1} с".format(score_2, team1_time))


# f-строки
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач")

team1_time = 1552,512
team2_time = 2153,31451
score_1 = 40
score_2 = 42
challenge_result = f'Победа команды Волшебники данных!'
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды мастеров кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды Волшебники данных!'
else:
    result = f'Ничья!'
    result = challenge_result
    print(f'Результат битвы: {result}')

time_avg = 45.2
tasks_total = 82
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу")