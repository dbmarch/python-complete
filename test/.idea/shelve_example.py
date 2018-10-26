import shelve

#with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = ' a sweet orange citrus fruit'
#     fruit['apple'] = 'good for making cider'
#     fruit['lemon'] = 'sour yellow fruit'
#     fruit['grape'] = 'used to make wine'
#     fruit['lime'] = 'sour green fruit'
#
#
#     print (fruit['lemon'])
#     print (fruit['grape'])
#     fruit ['lime'] = 'great with tequila'
#
#     for snack in fruit:
#         print (snack + ' : ' + fruit[snack])
#
#
#     while True:
#         dict_key = input ('please enter a fruit: ')
#         if dict_key == 'quit':
#             break;
#         if dict_key in fruit:
#             description = fruit[dict_key]
#             print (description)
#         else:
#             print ("We don't have a "+ dict_key)
# print (fruit)
#

# with shelve.open('ShelfTest') as fruit:
#     ordered_keys = list(fruit.keys())
#     ordered_keys.sort()
#     for f in ordered_keys:
#         print (f + ' - ' + fruit[f])


with shelve.open('ShelfTest') as fruit:
    for v in fruit.values():
        print (v)

    print (fruit.values())

    for f in fruit.items():
        print (f)

    print (fruit.items())