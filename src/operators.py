from random import randint
import commons

def sbox_input():
    result = []
    for i in range(commons.sbox_rows_count):
        row = [num_to_list(int(i, 16), 32) for i in input().split()]
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
        result.append(num_to_list(keys[i], 32))
    return result
    
def module_multiply(a: int, b: int):
    return (a * b) % commons.mul_mod

def module_add(a: int, b: int):
    return (a + b) % commons.add_mod

def binlist_to_str(l: list[int]):
    return ''.join(map(str, l))

def binlist_to_int(l: list[int]):
    return int(binlist_to_str(l), 2)

def num_to_str(n: int, strlen: int):
    return bin(n)[2:].zfill(strlen)

def num_to_list(n: int, listlen: int):
    return list(map(int, list(num_to_str(n, listlen))))

def list_multiply(a: list[int], b: list[int]):
    a_num = binlist_to_int(a)
    b_num = binlist_to_int(b)
    
    mul = module_multiply(a_num, b_num)

    return num_to_list(mul, len(a))

def binlist_add(a: list[int], b: list[int]):
    a_num = binlist_to_int(a)
    b_num = binlist_to_int(b)
    
    mul = module_add(a_num, b_num)

    return num_to_list(mul, len(a))

def list_xor(a: list[int], b: list[int]):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result