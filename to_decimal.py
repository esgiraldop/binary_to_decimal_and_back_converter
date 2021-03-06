def binary_2_integer(int_part):
    '''
        Function for trasforming an integer decimal number into a binary number
        :param
            int_part: Integer number in decimal.Decimal format.
        :return:
            int_bin: Binary number in integer format.
    '''
    int_part = list(str(int_part))
    int_part.reverse()
    sum = 0
    expo = 0
    for digit in int_part:
        if digit == '1':
            sum += 2**expo
        expo += 1

    return sum

def binary_2_float(float_part):
    '''
        Function for trasforming the float part of a binary number into a float decimal number
        :param
            float_part: Float binary number in decimal.Decimal format.
        :return:
            sum: Float decimal number in decimal.Decimal format.
    '''
    float_part = list(str(float_part)[2:]) # From position 2 onwards to ignore the '0.'
    sum = 0
    expo = -1
    for digit in float_part:
        if digit == '1':
            sum += 2**expo
        expo -= 1

    return sum

if __name__ == '__main__':
    import decimal
    int_part = 10110
    ans = input('Please enter a binary number: ')
    decimal.getcontext().prec = len(ans[2:])
    float_part = decimal.Decimal(ans)
    dec_int = binary_2_integer(int_part)
    dec_float = binary_2_float(float_part)
    print('dec_int: ', dec_int)
    print('dec_float: ', dec_float)