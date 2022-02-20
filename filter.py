# filter() = creates a collection of elements from an iterable for which a function returns true.
#
# filter(function, iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Naima",17),
           ("Iqra",21),
           ("Maria",31)]

age = lambda data:data[1] >=18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)