# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)
# PKR to USA

store = [("shirt",1800.00),
         ("pants",2000.00),
         ("jacket",9800.00),
         ("socks", 890.00)]

to_euros = lambda data: (data[0],data[1]*178.88)
to_dollars = lambda data: (data[0],data[1]/178.88)

store_dollars = list(map(to_dollars,store))

for i in store_dollars:
              print(i)