import decimal
import to_binary
import partitioner

num = 22.246
int_part, dec_part = partitioner.decimal_partitioner(num)
int_bin = to_binary.integer_2_binary(int_part)
dec_bin = to_binary.decimal_2_binary(dec_part)
bin_num = decimal.Decimal(str(int_bin)+str(dec_bin)[1:])
print(bin_num)