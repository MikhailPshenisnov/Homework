# Задача 1
with open('26-3.txt', 'r', encoding='utf8') as file:
    data = [int(line.strip()) for line in file]
people = data[0]
rich = int(0.2 * people)
money = sorted(data[1::], reverse=True)
full_sum = int(0.6 * sum(money))
rich_money = money[:rich:]
rich_sum = int(0.8 * sum(rich_money))
poor = people - rich
poor_sum = full_sum - rich_sum
poor_money = money[rich + 1::]
poor_percent = poor_sum / sum(poor_money)
the_smallest_contribution = int(min(money) * poor_percent)
print(f'{rich_sum};{the_smallest_contribution}')
