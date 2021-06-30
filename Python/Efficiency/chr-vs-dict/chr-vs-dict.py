"""
chr vs dict

Objective
 [ ] find out which one is faster

"""

from timeit import timeit


# Using chr() to get an ASCII character
chr_result = timeit('chr(67)', number=100000)

# Using dict to get an ASCII character
dict_result = timeit('ascii[67]', setup="ascii = {65: 'A', 66: 'B', 67: 'C'}", number=100000)


# Show results
print('Results (the lower the better):\n')
print(f'chr()  --> {chr_result}')
print(f'dict() --> {dict_result}')
print()
# Which one is the fastest?
if dict_result <= chr_result:
    diff = chr_result - dict_result
    percentage = (diff / chr_result) * 100
    print('lowest --> dict')
    print(f'faster by --> {percentage:.2f}%')
else:
    diff = dict_result - chr_result
    percentage = (diff / dict_result) * 100
    print('lowest --> chr')
    print(f'faster by --> {percentage:.2f}%')

