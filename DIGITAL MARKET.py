# DIGITAL MARKET :

from pickle import TRUE


items = []
prices = []
total =0

while TRUE:
    item = input("Enter a item to buy(q to quite):")
    if item =="q":
        break
    else:
        price = float(input(f"Enter a price of {item}:$"))
        items.append(item)
        prices.append(price)

print("----YOUR DIGITAL MARKET----")
for item in items:
    print(item, end=" ")

for price in prices:
    total += price

print()
print(f"YOUR TOTAL:$d{total}")


        

