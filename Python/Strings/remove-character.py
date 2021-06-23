# This file will attempt to remove a specific character in a string
#
# Usage:
#   >>> remove_character(',' '', '403,687,366')
#   403687366

def remove_character(old_character, new_character, text):

    return text.replace(old_character, new_character)


def remove_multiple_characters(excluded_characters, new_character, text):

    for character_to_remove in excluded_characters:
        text = remove_character(character_to_remove, new_character, text)

    return text


# test
a = '403,687,366'
b = '(PostgreSQL) 12.7'
c = 'aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbb'
excluded_characters = ['(', ')', 'a']

# OK: Remove single character
result = remove_character(',', '', a)
print(result)

# OK: Remove multiple characters
# result = remove_multiple_characters(excluded_characters, '', c)
# print(result)
