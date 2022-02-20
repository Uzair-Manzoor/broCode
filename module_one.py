# *********************************
# if __name__ == '__main__'
# *********************************
#
# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules
#
# Python interpreter sets "special variables", one of which is __ name__
# then python will execute the code found within __main__

# import module_two

if __name__ == '__main__':
     print('running this module directly')
else:
     print('running this module indirectly')
# print(__name__)
# print(module_two.__name__)

