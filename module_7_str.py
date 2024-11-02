team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_num = 5
string1 = "В команде %s участников %s!" % (team1, team1_num)
print(string1)

team2_num = 6
string2 = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)
print(string2)

score_2 = 42
string3 = "Команда {} решила задач: {}!".format(team2, score_2)
print(string3)

team1_time = 18015.2
string4 = "{} решили задачи за: {} c!".format(team2, team1_time)
print(string4)

score_1 = 40
score_2 = 42
string5 = f"Команды решили {score_1} и {score_2} задач."
print(string5)

if score_1 > score_2:
    challenge_result = team1
elif score_2 > score_1:
    challenge_result = team2
else:
    challenge_result = "Draw"

string6 = f"Результат битвы: победа команды {challenge_result}"
print(string6)

tasks_total = score_1 + score_2
time_avg = 350.4
string7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(string7)