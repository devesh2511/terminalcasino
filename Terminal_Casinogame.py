print('')
print('~~WELCOME TO THE CASINO TERMINAL.... '
      '\n ..THE ALL NEW GAMING PLATFORM! ')
a = str(input('\n ~~Please enter your name: '))
print("\n ~~HELLO",a,'Hope you have good luck today and return with a heavier bag :) \n ')



game=True

while game:
    choice = -1;
    print('Enter 1 for Playing the 7UP-7DOWN Game \n')
    print('Enter 2 for Playing Blackjack Game\n')
    print('Enter 3 for Playing Roulette Wheel Game\n')
    while choice>3 or choice<1:
        choice = int(input('Enter your choice:'))
        if (choice == 1):
            exec(open('SevenUP_SevenDOWN.py').read())
        if (choice == 2):
            exec(open('Blackjack.py').read())
        if (choice == 3):
                exec(open('Roulette.py').read())

    quitter = input("\nDo you want to play another game(y/n)?")
    if quitter == 'y' or quitter == 'Y':
        game = True
    elif quitter == 'n' or quitter == 'N':
        game= False
        print("\nThank you for playing with TERMINAL CASINO and hope to see you again", a)



