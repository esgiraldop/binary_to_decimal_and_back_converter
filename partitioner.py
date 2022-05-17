import decimal

def negative_sign_partitioner(frst_usr_ans):
    '''
        Function for identifying if the entered number comes with a '-' or '+' sign
        :param
            frst_usr_ans: Number in decimal.Decimal format. May or may not contain a '-' or '+' sign
        :return:
            frst_usr_ans: Number in decimal.Decimal format without signs.
            sign: String containing '-' for negative sign, or empty string for positive sign
    '''
    frst_usr_ans = str(frst_usr_ans)
    if '-' in frst_usr_ans:
        sign = frst_usr_ans[0]
        frst_usr_ans = frst_usr_ans[1:]
    elif '+' in frst_usr_ans:
        sign = ''
        frst_usr_ans = frst_usr_ans[1:]
    else:
        sign = ''

    frst_usr_ans = decimal.Decimal(frst_usr_ans)
    return frst_usr_ans, sign

def float_partitioner(dec_num):
    '''
        Function for spliting the input number in two parts. The first part is the integer part,
        the second part is the float part.
        :param
            dec_num: Number in decimal.Decimal format. May contain a float part (22.0), or may not (22)
        :return:
            int_part: Number in decimal.Decimal format. Represents the integer part
            float_part: Number in decimal.Decimal format. Represents the float part. Empty string if dec_num is integer
    '''
    dec_num = str(dec_num)
    int_part = dec_num.split('.')[0]
    try:
        # Checking the input number has a float part
        float_part = dec_num.split('.')[1]
    except:
        # The user entered an integer number. '125' For example
        return decimal.Decimal(int_part), ''
    else:
        decimal.getcontext().prec = len(float_part)
        if float_part == '0':
            # In case user entered '125.0' for example, which is still an integer represented as a float
            return decimal.Decimal(int_part), ''

        # User entered a float number, and decimal part is different than '0'
        int_part = decimal.Decimal(int_part)
        float_part = decimal.Decimal('0.'+float_part)
        return int_part, float_part

if __name__ == '__main__':
    dec_num = 22.246
    int_part, float_part = float_partitioner(dec_num)
    print('int_part: ', int_part)
    print('float_part: ', float_part)