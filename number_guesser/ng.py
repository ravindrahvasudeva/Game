import random as r
 
top_of_the_range=input("type a number:")

if top_of_the_range.isdigit():
  top_of_the_range=int(top_of_the_range)
  
  if top_of_the_range<=0:
      print('can to you pls type a numb greater than 0')
      quit()
else:
    print('please entera valid number next time')
    quit()

random_no = r.randint(0, top_of_the_range)
guess=0

while True:
    guess+=1
    user_guess =input("Guess a number:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('pls enter a valid  number next time !')
        continue
    if user_guess ==random_no:
        print("YOU GOT IT CORRECT")
        break
    elif user_guess>random_no:
        print("The number u guessed is greater !")
    else:
        print ('Your  guessed number is below the actual number  !')
    
print("Youre total guesses are",guess)