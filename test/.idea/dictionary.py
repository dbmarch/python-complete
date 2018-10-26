fruit = {"orange": "a sweet, orange citrus fruit",
        "apple": "good for making cider",
        "lemon": "sour yellow citrus",
        "grape": "small sweet fruit growing in bunches",
         "lime":  "sour green citrus fruit"}
#
# # print (fruit)
#
# print (fruit["lemon"])
#
# fruit ["pear"]  = "an odd shaped fruit"
#
# # print (fruit)
# # del fruit ["lemon"]
# # print (fruit)
#
# fruit_keys = fruit.keys();
# print (fruit_keys)
# # print (fruit.values())
# fruit["tomato"] = "not nice with ice cream"
#
# print (fruit_keys)

print (fruit.items())
f_tuple = tuple(fruit.items())
print (f_tuple)

for snack in f_tuple:
    item,description = snack
    print (item + " is " + description)


print (dict(f_tuple))