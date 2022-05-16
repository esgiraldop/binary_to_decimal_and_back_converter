import decimal

def validate_binary(number):
    pass

def check_input():
    # Check with a while loop, the input number is a float or an integer
    while True:
        frst_usr_ans = input('Please input an integer or float number: ')
        try:
            frst_usr_ans = decimal.Decimal(frst_usr_ans)
        except:
            print('Please input a valid number')
        else:
            break

    scnd_usr_ans = 'a'
    while scnd_usr_ans not in ['b', 'd']:
        scnd_usr_ans = input('Is it a binary (b) or decimal number (d)? (b/d): ')
        if scnd_usr_ans not in ['b', 'd']:
            print('Please input a valid answer')

    return frst_usr_ans, scnd_usr_ans

if __name__ ==  '__main__':
    frst_usr_ans, scnd_usr_ans = check_input()
    print('frst_usr_ans: ', frst_usr_ans)
    print('scnd_usr_ans: ', scnd_usr_ans)