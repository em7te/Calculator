
while True:
    def fun_sum():
        try:
            x = int(input('input1: '))
            y = int(input('input2: '))
        except Exception as er:
            ex_err = str(er).split("invalid literal for int() with base 10: ")[1].split("'")[1]
            print(er.args)
            if ex_err == 'end':
                return 'end'
            return 'ERROR: incorrect input'

        z = input('input sing: ')


        if z == '+':
            result = x + y
        elif z == '-':
            result = x - y
        elif z == '*':
            if x == 0 or y == 0:
                result = 0
            else:
                result = x * y
        elif z == '/':
            if x == 0:
                result = 0
            elif y == 0:
                return 'ERROR: division by zero is not possible'
            else:
                result = x / y
        else:
            return 'ERROR: incorrect input sing'

        return f'RESULT: {str(result)}'
    
    x_fun = str(fun_sum())
    if x_fun == 'end':
        break
    else:
        print(x_fun + '\n')
