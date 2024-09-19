#Accept a number from the user and check if it is a Perfect Square
import math
input_num=int(input("enter num"))
root= math.sqrt(input_num)
floor_num=math.floor(root)
if floor_num*floor_num==input_num:
    print(f'{input_num} Perfect Nmuber')
else:
    print(f'{input_num} not Perfect Number')
