name = input("hay there! Enter your name: ")
print("welcome", name,"find the Queen if possible")

answer = input("you are on a mud road you have 2 options (left/right) ").lower()

if answer == "left":
    answer = input("your found a river! will you walk around or swim (walk/swim) ").lower()
    
    if answer == "swim":
        print("Opps! alligator ate You")
    elif answer == "Walk":
        print("sorry you lost the route!")
    else :
        print('Not a valid option !',name)
elif answer == "right":
     answer = input("your found a  old  bridge! will you walk or goback (walk/goback) ").lower()
     if answer == "walk":
        answer = input("your found a Stranger! will you talk or pick a weapon yes or no (talk/weapon)) ").lower()
        
    
        if answer == "weapon":
            print(" He's suppresed by you,finally found Queen !!!! ")
        elif answer == "talk":
            print("he killed you!")
        else :
            print('Not a valid option !',name)
     elif answer == "goback":
        print("you gave up too early!")
     else :
        print('Not a valid option !',name)
else :
    print('Not a valid option !',name)
     