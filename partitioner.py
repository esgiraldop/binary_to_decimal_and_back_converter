import decimal

def decimal_partitioner(dec_num):
    int_part = int(dec_num)
    dec_part = None
    # Checking the input number has a float part. The first part of the conditional seem obvious,
    # but it is used because using dec_num.is_integer() produces an exception if "dec_num" is an integer
    if type(dec_num) != int and dec_num.is_integer() == False:
        # Separate "decimal" part. Here I had to use decimal because an imprecision computing float numbers
        dec_part = float(decimal.Decimal(str(dec_num)) - decimal.Decimal(str(int_part)))

    return int_part, dec_part