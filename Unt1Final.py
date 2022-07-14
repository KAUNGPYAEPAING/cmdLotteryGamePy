import secrets
import sys

secureNumber = secrets.SystemRandom()

while True:
    print('___Welcome to our game___')
    press1 = int(input('Press 1 to Read Rule or Press 2 to play game:>'))
    if press1 == 1:
        print('>Age must be more than 18:')
        print('>Show money more than 5000')
        print('>You must use more than 1000 each time')
    if press1 == 2:
        uName = input('Please enter your name')
        uAge = int(input("Please enter your age"))

        while len(uName) > 2 and uAge >17:
            print("You can play game now")
            print("Welcome :> ", uName)
            while True:
                sMoney = int(input("Please enter your show money :> "))
                while sMoney > 4999:
                    while True:
                        print("This is your money :> ", sMoney)
                        inputMoney = int(input("Please enter money to play :> "))
                        luckyMoney = int(input("Please enter your lucky number :> "))
                        systemNumber = secureNumber.randint(10, 99)

                        if luckyMoney == systemNumber:
                            print('You win mate... Congrate')
                            sMoney = (inputMoney*10) + (sMoney-inputMoney)
                            print("You win $ {}. You current money is {}". format(inputMoney*10, sMoney))
                            toQuit = int(input("Press 0 to Play again and Press any key to quit"))
                            if toQuit != 0:
                                sys.exit('Bye Bye')
                            else:
                                continue


                        print('Try again.... Lucky number is ', systemNumber)
                        sMoney = sMoney - inputMoney

                        if sMoney< 1000:
                            print("You don't have enough money $", sMoney)
                            break
                print("Please add more money")

        print('Please read the rules again')