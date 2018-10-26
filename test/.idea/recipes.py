import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beans_on_toast = [ 'beans', 'bread']
# scrambled_eggs = ['eggs', 'butter', 'milk']
# soup = ['tin of soup']
# pasta = ['pasta', 'cheese']
#
# with shelve.open('recipes') as recipes:
#     recipes['blt'] = blt
#     recipes['beans on toast'] = beans_on_toast
#     recipes ['scrambled_eggs'] = scrambled_eggs
#     recipes ['pasta'] = pasta
#     recipes ['soup'] = soup

dessert  = ['ice cream', 'whipped cream']
with shelve.open('recipes', writeback=True) as recipes:
     # recipes['dessert'] = dessert
    # recipes['blt'].append('butter')
    # recipes['pasta'].append('tomato')
    # temp_list = recipes['blt']
    # temp_list.append('butter')
    # recipes['blt'] = temp_list

    recipes['soup'].append('crackers')
    for snack in recipes:
         print (snack, recipes[snack])


