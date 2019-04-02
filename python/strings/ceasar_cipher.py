'''
Ceasar Cipher
'''

import string


def build_shift_dict(shift) -> dict:
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    lower_letters = string.ascii_lowercase
    lower_dict = {}
    for i in range(1, 27):
        lower_dict[i] = lower_letters[i-1]
    lower_shifted_dict = lower_dict.copy()
    for key in lower_dict.keys():
        if shift + key > 26:
            lower_shifted_dict[key] = lower_dict[shift+key-26]
        else:
            lower_shifted_dict[key] = lower_dict[shift+key]
    for key, value in lower_dict.items():
        lower_shifted_dict[value] = lower_shifted_dict.pop(key)

    upper_letters = string.ascii_uppercase
    upper_dict = {}
    for i in range(1, 27):
        upper_dict[i] = upper_letters[i-1]
    upper_shifted_dict = upper_dict.copy()
    for key in upper_dict.keys():
        if shift + key > 26:
            upper_shifted_dict[key] = upper_dict[shift+key-26]
        else:
            upper_shifted_dict[key] = upper_dict[shift+key]
    for key, value in upper_dict.items():
        upper_shifted_dict[value] = upper_shifted_dict.pop(key)
    lower_shifted_dict.update(upper_shifted_dict)
    return lower_shifted_dict


def apply_shift(string_to_encrypt, shift) -> str:
    '''
    Applies the Caesar Cipher to the string with the input shift.
    Creates a new string that is shifted down the alphabet by some number of
    characters determined by the input shift.

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    shifted_message = []
    shifted_dict = build_shift_dict(shift)
    for char in string_to_encrypt:
        if char in shifted_dict:
            shifted_message.append(shifted_dict[char])
        else:
            shifted_message.append(char)
    return ''.join(shifted_message)


def read_and_solve():
    length_string = int(input())
    string_to_change = input()
    shift_to_apply = int(input())

    encrypted_string = apply_shift(string_to_change, shift_to_apply)
    return encrypted_string


if __name__ == '__main__':
    print(read_and_solve())
