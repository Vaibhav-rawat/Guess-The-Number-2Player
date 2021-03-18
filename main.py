'''Multiplayer Game of Guess the number
Author - Vaibhav Rawat
Purpose - Python Problem Solving '''
import random

def guess(x,y):
  #Random number was generated within the function because so when next players plays the number gets generated again 
    random_num=random.randint(a,b)
    print(f'between {a}-{b}')
    p=0
    while True:
        num=int(input())
        if num==random_num:
            print('Correct')
            p+=1
            break
        elif num>random_num:
            print('Wrong! guess a smaller number')
            p+=1
        else:
            print('Wrong! guess a bigger number')
            p+=1
    return f'It took you {p} guesses'

if __name__=='__main__':
    a=int(input('Enter minimum range\n'))
    b=int(input('Enter the maximum range\n'))
    print('Player 1 please make the guess')
    guesses=guess(a,b)
    print('\nPlayer 2 please make the guess')
    guesses1=guess(a,b)
    if guesses<guesses1:
        print('Player 1 won')
    elif guesses>guesses1:
        print('Player 2 won')
    else:
        print('Tie')
