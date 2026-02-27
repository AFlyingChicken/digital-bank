def bank():
    balance = 500
    
    while True:
        try:   
            pick = int(input('Would you like to: 1. Deposit, 2. Withdraw, or 3. Check Balance? [Input: 1, 2, or 3] '))

            if pick == 1:
                deposit = float(input('How much would you like to deposit?: '))
                if deposit <= 0:
                    print('Deposit must be positive.')
                else:
                    balance += deposit
                    print(f'Your balance is now ${balance}.')
            
            elif pick == 2:
                withdraw = float(input('How much would you like to withdraw?: '))
                if withdraw > balance:
                    print('Insufficient balance!')
                else:
                    balance -= withdraw
                    print(f'Your balance is now ${balance}')
            
            elif pick == 3:
                print(f'Your balance is ${balance}.')
            
            else:
                while pick not in (1, 2, 3):
                    print('Please input either: 1, 2, or 3.')
                    pick = int(input('Would you like to: 1. Deposit, 2. Withdraw, or 3. Check Balance? [Input: 1, 2, or 3] '))
                
        except ValueError:
                print('Please do not input strings or floats.')

        while True:
            again = input('Would you like to do another transaction? (y/n): ')
            
            if again in ('y', 'n'):
                break
                
            print('Please input either "y" or "n".')

        if again == 'n':
            break
    return balance

pin = '1234'
attempts = 4

guess = input('Please enter your pin: ')

if guess == pin:
    print('You\'re in!')
    bank()
else:
    while attempts != 1:
        attempts -= 1
        guess = input(f'Please try again, you have {attempts} attempts left: ')

        if guess == pin:
            print('You\'re in!')
            bank()
            break

        elif attempts == 1:
            print('You are no longer authorized to enter this account.')

