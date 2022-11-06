import random

user_wins=0
computer_wins=0
options=["rock","paper","scissors"]

while True:
    user_input =input("Type rock/paper/scissors or q to quit").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    
    random_no =random.randint(0, 2)
    computer_pick = options[random_no]
    print("computer_picked",computer_pick + " . ")
    
    if user_input=="rock" and computer_pick=="scissors":
        print("YOY WON!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
            print("YOY WON!")
            user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
            print("YOY WON!")
            user_wins+=1
    else:
        print("You lost!")
        computer_wins+=1
        
print("YOU WON",user_wins,"times.")
print("the computer won",computer_wins,"times")
print("BYE,have a great day")