import random
# START MENUE
print(" ")
print(" ~~GET THE FEEL OF CASINO AT YOUR TERMINAL.. TRY HACKING IT!!~~")
print("         THE GAMBLING BOT      ")
print(" ")
print("  Red       DIAMOND      Black  ")
print("         |           |         ")
print(" 2    3  |           |  8    9 ")
print("         |           |         ")
print("    4    |     7     |    10    ")
print("         |           |         ")
print(" 5    6  |           |  11    12")
print("-- HEY GUYS -- !! \n  WE ARE PRESENTING THE MOST SURPRISING AND INNOVATIVE \n"
      "    GAMBLING GAME OF ALL TIMES FOR YOU"
      "\n   RULES OF THE GAME "
      "\n 1] There are 3 Categories namely.. 'Red', 'DIAMOND', and 'Black' .. As shown above "
      "\n 2] Two dice are rolling simultaneously .. "
      "\n 3] Dice rolling will stop once you choose a Category to bid in"
      "\n 4] Sum of the numbers shown by the dice will be the 'Lucky Number"
      "\n 5] Choose any one Category that you predict can contain the 'Lucky Number' "
      "\n 6] Enter the amount of money you like to bid in a Category"
      "\n 7] If you predicted the right Category containing the Lucky Number .. 'Your money will be DOUBLED' .. "
      "\n or else you will loose your money.. Special Case for 7 as here your money gets TRIPLED"
      "\n GET STARTED !! HOPE YOU LIKE IT!!"
      "\n -----------------------------------"
    )
# THE MAIN CODE OF GAME
game_on=True


while game_on:
    Money=int(input("Enter the amount of money you would like to bid:"))
    print("Choose any one Category from the below three as 'r-for red' or 'd- for diamond' or 'b- for black' ")
    print(" g) RED  \n d) DIAMOND \n s) BLACK")
    r="Category RED"
    d="Category DIAMOND"
    b="Category BLACK"
    print(" ")
    print("  RED       DIAMOND      BLACK ")
    print("         |           |         ")
    print(" 2    3  |           |  8    9 ")
    print("         |           |         ")
    print("    4    |     7     |    10    ")
    print("         |           |         ")
    print(" 5    6  |           |  11    12")
    options=input("Enter the option number you want to take :")
    number=random.choice([2,3,4,5,6,7,8,9,10,11,12])
    print("The lucky number is",number)
    if options== "r" or options=="R":
      if number <= 6:

            print("YAY!! Your Money is Doubled!!:" ,Money*2)
      else:
             print("OOPS! Your Money is Lost :" ,Money*0)

    if(options=="d" or options=="D"):
     if(number==7):
          print("YAY!! Your Money is Doubled:" ,Money*3)
     else:
          print("OOPS! Your Money is Lost:" ,Money*0)

    if(options=="b" or options=="B"):
     if(7<number<=12):
          print("YAY!! Your money is Doubled:" ,Money*2)
     else:
          print("OOPS! Your money is Lost:" ,Money*0)

    quitter = input("\nDo you want to quit the game(y/n)?")
    if quitter == 'n' or quitter == 'N':
        game_on = True
    elif quitter == 'y' or quitter == 'Y':
        game_on=False
        print("\nThank you for playing 7UP 7 DOWN")