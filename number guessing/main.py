import random
print('guess a number between 1 and 100, including both upper and lower limits.')
userin=input('choose your level,"easy" or "hard".')
attempts=0
if userin.lower()=='easy':
    attempts=10
else:
    attempts=5

guessed=random.randint(1,100)

while attempts!=0:
     userguess = int(input('make a guess:'))
     if userguess==guessed:
         print('you got the answer right.')
         break
     elif userguess>guessed:
         print('too high')
         attempts-=1
         print('attempts left:',attempts)
     elif userguess<guessed:
         print('too low')
         attempts-=1
         print('attempts left:',attempts)
     else:
         print('wrong input')

