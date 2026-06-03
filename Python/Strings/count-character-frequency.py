"""
This will count the frequeny of each character in a string

Steps
get character
add character to unique dictionary

"""

from collections import Counter

#sequence = '225283630538156616214'
sequence = 'ij/ji>/R<V'



frequencyCounter = Counter(sequence)

print(frequencyCounter)

