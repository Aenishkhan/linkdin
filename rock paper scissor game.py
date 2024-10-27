print("======rock-paper-scissor-game======")
'''
rock= 1
paper=  -1
scissor= 0
'''
import random
computer= random.choice([1, -1, 0])
youstr= input("enter a string: ")
youdict= {"r":1, "p": -1, "s": 0}
reversedict= {1: "rock", -1: "paper", 0:"scissor"}

you= youdict[youstr]

print(f"you inputted {reversedict[you]}\n computer inputted {reversedict[computer]}")


if(computer == you):
    print("its a draw")
    
else:
    if(computer== 1 and you== 0):
        print("you lose!")
    elif(computer== 1 and you == -1):
        print("you win!")
    elif(computer== 0 and you== -1):
        print("you lose!")
    elif(computer == 0 and you == 1):
        print("you win!")
    elif(computer== -1 and you== 1):
        print("you lose!")
    elif(computer== -1 and you== 0):
        print("you win!")


