import decimal

def integer_2_binary(int_part):
    '''
        Function for trasforming an integer decimal number into a binary number
        :param
            int_part: Integer number in decimal.Decimal format.
        :return:
            int_bin: Binary number in integer format.
    '''
    if int_part == 0:
        return 0
    quotient = int_part
    int_bin = list()
    while quotient / 2 >= 0.5:
        # print('quotient: ', quotient)
        remaining = quotient % 2
        quotient = int(quotient / 2)
        # print('remaining: ', remaining)
        int_bin.append(str(remaining))
        # print('\n')

    int_bin.reverse()
    int_bin = int(''.join(int_bin))
    return int_bin


def decimal_2_binary(float_part):
    '''
        Function for trasforming the float part of decimal number into a float binary number
        :param
            float_part: Float decimal in decimal.Decimal format.
        :return:
            dec_bin: Float binary number in decimal.Decimal format.
    '''
    if float_part == '':
        return ''

    mult_reslt = float_part
    dec_bin = list()
    count = 0
    decimal.getcontext().prec = len(str(float_part)[2:]) + 1
    dec_bin.append('.')
    while True:
        # print('count: ', count)
        mult_reslt = decimal.Decimal(mult_reslt) * 2
        int_part = int(mult_reslt)
        if mult_reslt > 1:
            mult_reslt = decimal.Decimal(mult_reslt) - int_part
        # print('mult_reslt: ', mult_reslt)
        # print('int_part: ', int_part)
        if mult_reslt == 0:
            break
        dec_bin.append(str(int_part))
        count += 1
        # print('\n')
        if count > 18:
            break
    dec_bin = decimal.Decimal(''.join(dec_bin))

    # It makes no sense to return a decimal binary number whose last number is zero
    if str(dec_bin)[-1] == '0':
        dec_bin = str(dec_bin)[:-1] + '1'
        dec_bin = decimal.Decimal(dec_bin)

    return dec_bin