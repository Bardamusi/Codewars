"""
5 kyu - Rot13

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string,
they should be returned as they are.
Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
"""


def create_encrypt_dict(shift):
    """
    Creates dictionary for Caesar's cipher for letters
    :param shift: how much to "change" the letters by (so shift of 2 turns a -> c, z -> b)
    :return: dictionary with bindings mapping letters to encrypted letter
    """
    lower_case = "acbcdefghijklmnopqrstuvwxyz"
    asc2_a = ord("a")

    shifted_dict = {}
    for letter in lower_case:
        val_letter = ord(letter)
        shifted_val = asc2_a + ((val_letter - asc2_a + shift) % 26)
        shifted_dict[letter] = chr(shifted_val)
        shifted_dict[letter.upper()] = shifted_dict[letter].upper()

    return shifted_dict


def rot13(message):
    """
    :param message: string message, to be encrypted
    :return: encrypted string
    We encrypt using Caesar's cipher, and by creating a dictionary to map the letters
    to their "encrypted" counterpart.
    """

    encrypt_dict = create_encrypt_dict(13)
    enc_list = []
    for letter in message:
        try:
            enc_list.append(encrypt_dict[letter])  # If letter we encrypt it
        except KeyError:
            enc_list.append(letter)  # If other we keep it as is

    return "".join(enc_list)


if __name__ == "__main__":
    print(rot13("test"), "grfg")
    print(rot13("Test"), "Grfg")