# Higher Order Fubction = a function that either:
#                           1. accepts a fubction as an argument
#                               or
#                           2. return a function
#                           (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
# _____________________________________________________________

def divisor(x):
    def divident(y):
        return y / x

    return divident

divide = divisor(2)
print(divide(10))
