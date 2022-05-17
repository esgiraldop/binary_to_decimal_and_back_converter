import decimal
import to_binary
import to_decimal
import partitioner
import ask_input

num = 22.246

frst_usr_ans, scnd_usr_ans = ask_input.check_input()
# scnd_usr_ans can be '1' or '2'
int_part, float_part = partitioner.float_partitioner(frst_usr_ans)
if scnd_usr_ans == '1': # User wants to transform from binary to decimal
    int_dec = to_decimal.binary_2_integer(int_part)
    float_dec = to_decimal.binary_2_float(float_part)
    dec_num = decimal.Decimal(str(int_dec)+str(float_dec)[1:])
    print('The equivalent decimal number is: ', dec_num)
    # print('Functions for transforming from binary to decimal yet to be implemented')
else: # User wants to transform from decimal to binary
    int_bin = to_binary.integer_2_binary(int_part)
    float_bin = to_binary.decimal_2_binary(float_part)
    bin_num = decimal.Decimal(str(int_bin)+str(float_bin)[1:])
    print('The equivalent binary number is', bin_num)