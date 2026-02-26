def get_grade():
    amount = int(input('How much grades do you want to enter?: '))
    while not isinstance(amount, int):
        try:
            amount = int(input('How much grades do you want to enter?: '))

        except ValueError:
            print('Please input an integer.')

    total = 0
    number = 0
    while amount != number:
        try:   
            grade = float(input(f'Enter your grade: '))

            if grade < 0 or grade > 100:
                while grade < 0 or grade > 100:
                    print('Invalid input. Please enter a grade from 0 to 100')
                    grade = float(input(f'Enter your grade: '))
                
            number += 1
            total += grade

        except ValueError:
            print('Please input an integer or a float.')

    return total, number

total, number = get_grade()
average = total / number
averagerounded = round(average, 2)

print(f'Your average grade is: {averagerounded}')

if average >= 100:
    print('Grade: S')
    print('Perfect!')
elif average >= 95:
    print('Grade: A')
    print('Well Rounded!')
elif average >= 90:
    print('Grade: B')
    print('Great!')
elif average >= 85:
    print('Grade: C')
    print('Nice!')
elif average >= 80:
    print('Grade: D')
    print('You can do it!')
else:
    print('Grade: F')
    print('Keep studying to improve!')


