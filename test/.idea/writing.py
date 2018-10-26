# cities = ["St Louis", "Kansas City", "Columbia", "Jonesberg" ]
#
# with open ("cities.txt", "w") as city_file:
#     for city in cities:
#         print (city, file=city_file)
#
#
# cities = []
# with open ("cities.txt", "r") as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print (cities)
# for city in cities:
#     print (city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "pulling the rug"), (2, "Psycho"), (3, "mayhem"), (4, "kentish town waltz")
# )
#
#
# with open ("imelda3.txt", 'w') as imleda_file:
#     print (imelda, file=imleda_file)


with open ("imelda3.txt", "r") as imelda_file:
    contents = imelda_file.readline()
imelda = eval(contents)

print (imelda)
title,artist,year,tracks = imelda
print (title)
print (artist)
print (year)