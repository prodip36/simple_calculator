import cal as f
import os

print("Welcome to calculator->")
os.system('pause')
while True:
    os.system('cls')
    print("Please choose an option:")
    print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Power\n 6.Mod\n 0 for exit\n")
    choice= int(input("Your option:"))
    if choice==0:
     break
    else:
       f.cal(choice)