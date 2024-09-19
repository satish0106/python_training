input_num=int(input("enter the number"))
large=0
secondlarge=0
while input_num!=0:
   lastdigit=input_num%10
   input_num =input_num//10  
   if large <lastdigit:
      secondlarge=large
      large=lastdigit
   if lastdigit <secondlarge:  
       secondlarge=lastdigit
   
      
print(secondlarge)