# Задача 2
with open('26-k2.txt', 'r', encoding='utf8') as file:
    data = [line.strip() for line in file]
people, winners, awardees = [int(number) for number in data[0].split()]
results = sorted([int(number) for number in data[1::]], reverse=True)
winners_list = results[:winners:]
awardees_list = results[winners + 1:awardees + winners:]
print(f'{awardees_list[-1]};{winners_list[-1]}')
