intput_num=int(input("enter the number"))
result=0
for i in range(1,21):
    print('%d * %02d =%0`3d' % (intput_num,i,intput_num*i))
