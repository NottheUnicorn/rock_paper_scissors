
import random 
while True:
    computer = random.randint(0,2)

    user= input('Enter your weapon, Choose Rock/Paper or Scissors, or do you want to quit: ')
    if user.lower() == 'quit':
        break

    if(computer == 0):
        computer= ('Rock')
    elif(computer==1):
        computer= ('Paper')
    elif(computer==2):
        computer= ('Scissor')

    print(('Computer Choose\t'+ computer)+ ('\nYou Choose\t'+ user))

    if(user =='Rock'):
        if(computer=='Rock'):
            print('That is a Tie')
        elif(computer=='Scissor'):
            print('You Won')
        elif(computer=='Paper'):
            print('You Lost!')


    elif(user =='Paper'):
        if(computer =='Paper'):
            print('That is a Tie')
        elif(computer =='Rock'):
            print('You win')
        elif(computer =='Scissor'):
            print('Sorry, You lost!')

    

    elif(user =='Scissor'):
        if(computer =='Scissor'):
            print('That is a Tie')
        elif(computer =='Paper'):
            print('You win')
        elif(computer =='Rock'):
            print('Sorry, you lost')
