import decimal

def check_first_input(number):


def check_first_input(number):
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

    pass