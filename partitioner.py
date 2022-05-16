import decimal

def float_partitioner(dec_num):
    dec_num = str(dec_num)
    int_part = dec_num.split('.')[0]
    try:
        # Checking the input number has a float part
        dec_part = dec_num.split('.')[1]
    except:
        # The user entered an integer number. '125' For example
        return decimal.Decimal(int_part), None
    else:
        decimal.getcontext().prec = len(dec_part)
        if dec_part == '0':
            # In case user entered '125.0' for example, which is still an integer represented as a float
            return decimal.Decimal(int_part), None

        # User entered a float number, and decimal part is different than '0'
        return decimal.Decimal(int_part), decimal.Decimal('0.'+dec_part)

if __name__ == '__main__':
    dec_num = 22.246
    int_part, dec_part = float_partitioner(dec_num)
    print('int_part: ', int_part)
    print('dec_part: ', dec_part)