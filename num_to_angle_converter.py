angles = ["-pi", "-7/8 pi", "-3/4 pi", "-5/8 pi", "-1/2 pi", "-3/8 pi", "-1/4 pi", "-1/8 pi", "0", "1/8 pi", "1/4 pi", "3/8 pi", "1/2 pi", "5/8 pi", "3/4 pi", "7/8 pi"]

# for given number from 0 to 15 function returns angle as text
# value of angles depends on program run on machine
def convert(num):
    return angles[num]

def get_angles():
    return angles