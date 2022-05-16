import decimal
import to_binary
import partitioner
import ask_input

num = 22.246

frst_usr_ans, scnd_usr_ans = ask_input.check_input()
# scnd_usr_ans can be '1' or '2'
int_part, dec_part = partitioner.float_partitioner(frst_usr_ans)
if scnd_usr_ans == '1': # User wants to transform from binary to decimal
    print('Functions for transforming from binary to decimal yet to be implemented')
else: # User wants to transform from decimal to binary
    int_bin = to_binary.integer_2_binary(int_part)
    dec_bin = to_binary.decimal_2_binary(dec_part)
    bin_num = decimal.Decimal(str(int_bin)+str(dec_bin)[1:])
    print(bin_num)