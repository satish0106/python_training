int_number=int(input("enter the number"))
sum=0
while int_number!=0:
    lastdigit=int_number%10
    sum=sum+lastdigit
    if sum <= 9:
       print("lucky ",int_number)
    else:
        sum=int_number

    int_number=int_number//10
    
    