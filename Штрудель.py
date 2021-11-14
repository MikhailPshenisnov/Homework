# Задача 4
with open('26-s1.txt', 'r', encoding='utf8') as file:
    data = [int(line.strip()) for line in file]
number_prices = data[0]
prices = sorted([int(number) for number in data[1::]], reverse=True)
products_without_sales = [price for price in prices if price <= 200]
products_with_sales = [price for price in prices if price > 200]
index_1, index_2 = 0, -1
new_products_with_sales = []
while True:
    if len(products_with_sales) - index_1 != -index_2 and \
            (index_1 >= len(products_with_sales) or index_2 < len(products_with_sales)):
        new_products_with_sales.append(products_with_sales[index_1])
        new_products_with_sales.append(products_with_sales[index_2])
        index_1 += 1
        if len(products_with_sales) - index_1 != -index_2 and \
                (index_1 >= len(products_with_sales) or index_2 < len(products_with_sales)):
            index_2 -= 1
        else:
            the_most_expensive_product_with_sales = products_with_sales[index_2]
            break
    else:
        new_products_with_sales.append(products_with_sales[index_1])
        the_most_expensive_product_with_sales = products_with_sales[index_2 + 1]
        break
new_products_with_sales_with_sales = [new_products_with_sales[i] if i % 2 == 0
                                      else (int(0.7 * new_products_with_sales[i])
                                            if 0.7 * new_products_with_sales[i] == int(0.7 * new_products_with_sales[i])
                                            else int(0.7 * new_products_with_sales[i]) + 1)
                                      for i in range(len(new_products_with_sales))]
full_sum = sum(products_without_sales) + sum(new_products_with_sales_with_sales)
print(f'{full_sum};{the_most_expensive_product_with_sales}')
