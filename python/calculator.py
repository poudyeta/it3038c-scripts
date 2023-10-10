end = False
while not end:
    operations = ('+', '-', '/', '*')
    operation = input('Please Select Operation: +, -, /, or *: ')

    if operation not in operations:
        print('Invalid Operataion')
        continue

    number_1 = int(input('Enter first Number: '))
    number_2 = int(input('Enter second Number: '))
    if operation == '+':
        answer = number_1 + number_2
        print(f'{number_1} + {number_2} = {answer}')

    elif operation == '-':
        answer = number_1 - number_2
        print(f'{number_1} - {number_2} = {answer}')

    elif operation == '*':
        answer = number_1 * number_2
        print(f'{number_1} * {number_2} = {answer}')

    elif operation == '/':
        answer = number_1 / number_2
        print(f'{number_1} / {number_2} = {answer}')

    again = input('Would you like to do another operation (Y/N): ').lower()
    if  again == 'n':
        end = True