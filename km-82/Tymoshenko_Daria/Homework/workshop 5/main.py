"""
 Створити dataset та працювати з ним
"""
def create_dict(lst):
    if len(lst[0]) == 2:
        return {
            'quantity': lst[0][0],
            'price': lst[0][1]
                }
    dct={}
    for elem in lst:
        key = elem[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(elem[1:])
    for key in dct:
        dct[key] = create_dict(dct[key])
    return dct
with open('orders.csv', encoding='utf-8') as f:
    f.readline()
    file = [[el.strip() for el in line.split(',')] for line in f]
    result = create_dict(file)
print(result)


# Які продукти купляли усі покупці?

all_prod = set()

for val in result.values():
    for val2 in val.values():
        all_prod = all_prod.union(set(val2.keys()))
for name in result:
    buy_products = set()
    for date in result[name]:
        buy_products = buy_products.union(set(result[name][date].keys()))
    all_prod = all_prod.intersection(buy_products)
common_products = all_prod
print("Task 2: ",common_products)


# Як змінювалась ціна на яблука? (графік)
apples = {}
for _, dates in result.items():
    for date, products in dates.items():
        for prod, prices in products.items():
            if prod == 'apple':
                apples[date] = prices['price']
print("Task 3: ",apples)

import plotly.offline as pl
import plotly.graph_objs as go
xs = sorted(list(apples.keys()))
ys = [apples[key] for key in xs]
pl.plot([go.Scatter(x=xs,y=ys)])


# Скільки грошей витрачає кожний покупець на покупки? (графік)
spending = {}
for name in result:
    spending[name] = 0
    for date in result[name]:
        for product in result[name][date]:
            spending[name] += float(result[name][date][product]['price'])*float(result[name][date][product]['quantity'])

pl.plot([go.Bar(x=list(spending.keys()),y=list(spending.values()))])


# Який найпопулярніший товар?
# Якого товару було куплено найменше?
product_popularity = dict()
for name in result:
    for date in result[name]:
        for product in result[name][date]:
            if product not in product_popularity:
                product_popularity[product] = 0
            product_popularity[product] = float(result[name][date][product]['quantity'])
products = list(product_popularity.keys())
quantities = list(product_popularity.values())
max_quantities = max(quantities)
min_quantities = min(quantities)

max_index = quantities.index(max_quantities)
min_index = quantities.index(min_quantities)

print("Task 4: ",product_popularity,products[max_index],products[min_index])


# Який найдорожчий товар?
product_price = dict()
for name in result:
    for date in result[name]:
        for product in result[name][date]:
            if product not in product_price:
                product_price[product] = 0
            product_price[product] = float(result[name][date][product]['price'])
products = list(product_price.keys())
prices = list(product_price.values())
max_price = max(prices)
max_index = prices.index(max_price)
print("Task 5: ",product_price,products[max_index], max_price)


# Якого товару, скільки покупців купляє? (графік)
product_buyers = dict()
for name in result:
    for date in result[name]:
        for product in result[name][date]:
            if product not in product_buyers:
                product_buyers[product] = 0
            product_buyers[product] += 1
pl.plot([go.Bar(x=list(product_buyers.keys()),y=list(product_buyers.values()))])


# Написати функціонал для додавання нових даних


def add_dict(dct, lst):
    if len(lst) == 3:
        dct[lst[0]] = {
            'quantity': lst[1],
            'price': lst[2]
        }
        return dct
    key = lst[0]
    if key not in dct:
        dct[key] = {}
    add_dict(dct[key], lst[1:])
    return dct
lst = ['Jane','10.11.2019','apple','1','4.5']
dct = {}
print(add_dict(dct, lst))




