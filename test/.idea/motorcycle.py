import shelve

with shelve.open ('bike2') as bike:
    bike['make'] = 'Honda'
    bike['model'] = '250 dream'
    bike['color'] = 'red'
    bike['enginesize'] = 250

    print (bike['engine_size'])
    print (bike['color'])