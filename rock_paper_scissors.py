import random

user_wins=0
computer_wins=0

options=["rock", "paper", "scissors"]
#here rock=0 paper=1 scissors=2

while True:
    user_pick=input("type rock/paper/scissors or 'q' to quit:  ").lower()
    if user_pick=="q":
        break

    if user_pick not in options:
        continue


    random_pick=random.randint(0,2)
    computer_pick=options[random_pick]
    #here rock=0 paper=1 scissors=2
    print("computer picked {}".format(computer_pick))

    if user_pick=="rock" and computer_pick=="scissors":
        print("you won!")
        user_wins+=1

    elif user_pick=="paper" and computer_pick=="rock":
        print("you won!")
        user_wins+=1

    elif user_pick=="scissors" and computer_pick=="paper":
        print("you won!")
        user_wins+=1

    else:
        print("computer won!")
        computer_wins+=1

print("you won {} times".format(user_wins))
print("computer won {} times".format(computer_wins))



    

