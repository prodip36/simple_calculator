import os
def cal(x):
    if x>6:
     print("Please choose a valid option)")
     os.system('pause')
     return
    os.system('cls')
    print("Please Enter Two Number:")
    a=int(input("Value1: "))
    b=int(input("Value2: "))
    if x==1:
     ans=a+b
    elif x==2:
      ans=a-b
    elif x==3:
      ans=a*b
    elif x==4:
      if b!=0:
       ans=a/b
      else:
       print("undefined")
       os.system('pause')
       return
    elif x==5:
      ans=pow(a,b)
    elif x==6:
      if b!=0:
       ans=a%b
      else:
       print("undefined")
       os.system('pause')
       return
    print("Answer:",ans)
    os.system('pause')
    return