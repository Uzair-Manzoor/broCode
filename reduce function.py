# reduce() = apply a function to an iteriable and reduce it in to a single cumulative value.
#            performs function on first two elements and repeats process untill 1 value remains.
#
# reduce(function, iterables)

import functools

#letter = ["H","E","L","L","O"]
#word = functools.reduce(lambda x, y,:x + y,letter)
#print(word)

factorial = [120,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)