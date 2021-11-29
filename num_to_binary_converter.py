import math

# for given number from 0 to 15 function returns binary value as array[4]
# from biggest to smallest
# ex.
# for number 4 function returns:
# [0, 1, 0, 0]
# and for 11 returns:
# [1, 0, 1, 1]
def convert(num):
    number_binary = [int(x) for x in list('{0:0b}'.format(num))]
    if len(number_binary) != 4:
        for i in range(4-len(number_binary)):
            number_binary.insert(0, 0)
            
    return number_binary
