from random import randint
import commons

def sbox_input():
    result = []
    for i in range(commons.sbox_rows_count):
        row = [int_to_listbin(int(i, 16), 32) for i in input().split()]
        result.append(row)
    return result

def key_maker():
    keys = [
        0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344,
        0xA4093822, 0x299F31D0, 0x082EFA98, 0xEC4E6C89,
        0x452821E6, 0x38D01377, 0xBE5466CF, 0x34E90C6C,
        0xC0AC29B7, 0xC97C50DD, 0x3F84D5B5, 0xB5470917,
        0x9216D5D9, 0x8979FB1B, 0x38D01377, 0xA4093822,
        0xEC4E6C89, 0x243F6A88, 0x13198A2E, 0x85A308D3,
        0x082EFA98, 0x85A308D3, 0xBE5466CF, 0x03707344,
        0x243F6A88, 0x452821E6, 0x85A308D3, 0x38D01377,
    ]
    result = []
    for i in range(len(keys)):
        result.append(int_to_listbin(keys[i], 32))
    return result

def mod_add(a: int, b: int):
    return (a + b) % commons.add_mod
    
def mod_mul(a: int, b: int):
    return (a * b) % commons.mul_mod

def listbin_add(a: list[int], b: list[int]):
    a_num = listbin_to_int(a)
    b_num = listbin_to_int(b)
    
    mul = mod_add(a_num, b_num)

    return int_to_listbin(mul, len(a))

def listbin_mul(a: list[int], b: list[int]):
    a_num = listbin_to_int(a)
    b_num = listbin_to_int(b)
    
    mul = mod_mul(a_num, b_num)

    return int_to_listbin(mul, len(a))

def listbin_xor(a: list[int], b: list[int]):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result

def listbin_to_str(l: list[int]):
    return ''.join(map(str, l))

def listbin_to_int(l: list[int]):
    return int(listbin_to_str(l), 2)

def int_to_listbin(n: int, listlen: int):
    return list(map(int, list(int_to_strbin(n, listlen))))

def int_to_strbin(n: int, strlen: int):
    return bin(n)[2:].zfill(strlen)
