import random

computer = random.choice([-1,0,1])
youstr = input("Enter the charackter you want: ")
youdict = { "w" : 1 , "g" : 0 , "s" : -1}
reversedict = { 1 : "water" , 0:"gun" , -1 : "snake"}

you = youdict[youstr]

print(f"you chose {reversedict[you]} and computer chose {reversedict[computer]}")



if computer == you :
    print("Its A Draw!")

else:
    if computer==0 and you==-1:
        print("you Lose!")

    elif computer==0 and you==1:
        print("you won!")

    elif computer==-1  and you==1:
        print("you won!")

    elif computer==-1 and you==0:
        print("you lose!")

    elif computer==1 and you==0:
        print("you won!")

    elif computer==1 and you==-1:
        print("you lose!")

