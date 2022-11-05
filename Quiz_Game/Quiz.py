print("welcome to the Quiz game guys!")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
print("okay then lets start  :) ")
score = 0
sol = input("what is CPU stand for? ")
if sol.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
sol = input("what is GPU stand for? ")
if sol.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
sol = input("what is RAM stand for? ")
if sol.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
sol = input("what is GUI stand for? ")
if sol.lower() == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
    sol = input("what is UID stand for? ")
if sol.lower() == "user interface design":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
print(' you got' + str(score)+'questions correct!!!')
print(' you got' + str((score/4)*100)+'%.')
