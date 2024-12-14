
'''
0 for rock
1 for paper
2 fro scissor
'''
import random
Bot = random.choice([0,1,2])
youstr = input("Enter you Choice: ")
youDict = {"rock" :0 ,"paper" : 1, "scissor" :2}
reverseDict = {0:"rock", 1:"paper", 2:"scissor"}
you = youDict[youstr]

print(f"Bot choose: {reverseDict[Bot]}\nyou choose: {reverseDict[you]}")

if(Bot==you):
    print("Its a draw, Try again")
else:    
    if(Bot==0 and you ==1):
        print("You win")

    elif(Bot==1 and you==0):
        print("Bot win")

    elif(Bot==0 and you==2):
        print("Bot win")

    elif(Bot==2 and you==0):
        print("You win")

    elif(Bot==1 and you==2):
        print("You win")

    elif(Bot==2 and you==1):
        print("Bot win")

    else:
        print("Something went wrong")
