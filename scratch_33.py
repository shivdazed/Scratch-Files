#nested list elements
optionlist_items_dict = [
    ["Rava Dosa",70],
    ["Masala Dosa",75],
    ["Sada Dosa",60],
    ["Idli Plate", 40],
    ["Vada Plate", 50],
    ["Chinese Bhel", 25],
    ["Manhurian Soup", 50],
    ["Singapore Soup", 75],
    ["Chicken 65", 120],
    ["Chicken Crispy", 135],
    ["Chicken Manchurian", 130],
    ["Egg Fried Rice", 85],
    ["Egg Fried Noodles", 90],
    ["Chicken Fried Rice", 100],
    ["Chicken Fried Noodles", 110],
    ["Chicken Triple Rice", 130],
    ["Chicken Triple Noodles", 150],
    ["Veg Triple Rice", 110],
    ["Veg Triple Noodles", 124],
]
prices = []
i=0
j=0
n= len(optionlist_items_dict)
for price in optionlist_items_dict:
    if i in range(n):
        prices.append(optionlist_items_dict[i][1])
    i=i+1
print(prices)
items = []
for item in optionlist_items_dict:
    if j in range(n):
        items.append(optionlist_items_dict[j][0])
    j=j+1
print(items)