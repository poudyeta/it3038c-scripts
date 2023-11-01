end = False
while not end:
    operations = ('+', '-', '/', '*', '^')
    equation = input('Enter an equation (e.g., 2+3): ')

    parts = None
    for op in operations:
        parts = equation.split(op)
        if len(parts) == 2:
            operation = op
            break

    if parts is None or len(parts) != 2:
        print('Invalid input. Please enter an equation in the format: number operator number')
        continue

    number_1 = float(parts[0])
    number_2 = float(parts[1])

    if operation == '+':
        answer = number_1 + number_2
    elif operation == '-':
        answer = number_1 - number_2
    elif operation == '*':
        answer = number_1 * number_2
    elif operation == '/':
        answer = number_1 / number_2
    elif operation == '^':
        answer = number_1 ** number_2

    print(f'{number_1} {operation} {number_2} = {answer}')

    with open('log.txt', 'a') as log_file:
        log_file.write(f'{number_1} {operation} {number_2} = {answer}\n')

    again = input('Would you like to do another operation (Y/N): ').lower()
    if again != 'y':
        end = True
