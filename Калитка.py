# Задача 3
with open('26-k1.txt', 'r', encoding='utf8') as file:
    data = [line.strip() for line in file]
number_prices, number_sales = [int(number) for number in data[0].split()]
prices = sorted([int(number) for number in data[1::]], reverse=True)
products_with_sales = prices[:number_sales:]
products_without_sales = prices[number_sales + 1::]
the_most_expensive_product_without_sales = products_without_sales[0]
sales_sum = int(sum([0.2 * price for price in products_with_sales]))
print(f'{the_most_expensive_product_without_sales};{sales_sum}')