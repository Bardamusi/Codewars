"""
5 kyu - int32 to IPv4

Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python
"""


def int32_to_ip2(int32):
    """
    :param int32: 32 bit number
    :return: the integer representation of the 1,2,3,4 octets in binary separated by .

    """
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))


def int32_to_ip(int32):
    """
    :param int32: 32 bit number
    :return: the integer representation of the 1,2,3,4 octets in binary separated by .
    """
    bin_num = "{:032b}".format(int32)  # makes sure the binary number is 32 digits long
    oct1 = bin_num[:8]
    oct2 = bin_num[8:16]
    oct3 = bin_num[16:24]
    oct4 = bin_num[24:32]

    oct1 = str(int(oct1, 2))
    oct2 = str(int(oct2, 2))
    oct3 = str(int(oct3, 2))
    oct4 = str(int(oct4, 2))

    return f"{oct1}.{oct2}.{oct3}.{oct4}"


if __name__ == "__main__":
    print(int32_to_ip2(0))
    print(int32_to_ip2(2154959208))