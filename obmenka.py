import csv

obmens = [
    [currency, int(quantity), float(price)]
    for currency, quantity, price in csv.reader(open("obmenka.txt"))
]

d = {}

for c, q, p in obmens:
    if c not in d:
        d[c] = []
    d[c].append([q, p])
print(d)

print(list(d.items()))

print(max([p for c, q, p in obmens]))

# ('usd', [[100, 89.6], [-100, 90.0], [100, 89.5], [-100, 90.0]])

for cur, arr in d.items():
    # print(arr)
    quantity_buy = sum([q for q, p in arr if q > 0])
    quantity_sell = sum([abs(q) for q, p in arr if q < 0])
    cost_buy = sum([q * p for q, p in arr if q > 0])
    cost_sell = sum([q * p for q, p in arr if q < 0])
    avg_buy = cost_buy / quantity_buy
    avg_sell = cost_sell / quantity_sell
    print(cur)
    print(
        f"""Quantity buy: {quantity_buy}\tCost buy: {cost_buy}\tAverage buy: {avg_buy}
Quantity sell: {quantity_sell} \tCost sell: {cost_sell}\tAverage sell: {avg_sell}"""
    )

di = {
    "usd": [[100, 89.6], [-100, 90.0], [100, 89.5], [-100, 90.0]],
    "euro": [[100, 90.0], [-100, 92.0]],
}

# print(di["usd"][0][1])
