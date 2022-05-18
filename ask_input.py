import decimal

def validate_binary(frst_usr_ans, scnd_usr_ans):
    '''
            Function for asking the user a number and asking if the number is decimal or binary.
            The function also checks if correct values are entered by the user.
            :param
                frst_usr_ans: Float number with the number the user entered
                scnd_usr_ans: String with two possible answers (b/d) representing the type of numnbered
                            entered by the user. '1' for binary, '2' for decimal.
            :return:
                Boolean variable.
                    False value allows to end the outer while loop in parent function check_input() and
                    occurs in three scenarios:
                        1. The user indicated the number is not binary,
                        2. The number is binary and indeed contains 1's and 0's only
                        3. The use indicated the number is binary, it is actually not,
                            but the user now wants to use it as decimal

                    True value represents the number is not a binary number and then it is needed to ask to the user for
                        another number
        '''
    if scnd_usr_ans == '1':
        for i in range(2,10):
            # print(f'{i} in decimal number: {str(i) in str(frst_usr_ans)}')
            if str(i) in str(frst_usr_ans):
                print('This is not actually a binary number, but a decimal number.\nPlease choice an option')
                ans = '0'
                while ans not in ['1', '2']:
                    ans = input('1. Enter another number\n2. Use the number as decimal:')
                    if ans not in ['1', '2']:
                        print('Please enter a valid answer')

                if ans == '1':
                    return True
                else:
                    return False
        return False
    else:
        return False

def check_input():
    '''
        Function for asking the user a number and asking if the number is decimal or binary.
        The function also checks if correct values are entered by the user.
        :return:
        frst_usr_ans: Float number with the number the user entered
        scnd_usr_ans: String with two possible answers (1/2) representing the type of number
                        entered by the user. '1' for binary, '2' for decimal.
    '''
    ans = True
    while ans:
        frst_usr_ans = input('Please input an integer or float number: ').lower()
        ans_2 = any([frst_usr_ans == 'nan', frst_usr_ans == '-nan', frst_usr_ans == 'inf', frst_usr_ans == '-inf'])
        if ans_2:
            print('Please input a valid number')
            continue

        try:
            frst_usr_ans = decimal.Decimal(frst_usr_ans)
        except:
            print('Please input a valid number')
        else:
            scnd_usr_ans = '0'
            while scnd_usr_ans not in ['1', '2']:
                print('Please choice and option to transform: ')
                scnd_usr_ans = input('1. From binary to decimal\n2. From decimal to binary: ')
                if scnd_usr_ans not in ['1', '2']:
                    print('Please input a valid answer')

            ans = validate_binary(frst_usr_ans, scnd_usr_ans)

    return frst_usr_ans, scnd_usr_ans

if __name__ ==  '__main__':
    frst_usr_ans, scnd_usr_ans = check_input()
    print('frst_usr_ans: ', frst_usr_ans)
    print('scnd_usr_ans: ', scnd_usr_ans)