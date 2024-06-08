import helper
import commons
import sbox
from keys import keys

def hasht(plaintext: list[int], salt: list[int], work_factor: int) -> list[int]:
    '''
    - len(plaintext) = commons.block_len
    - len(salt) = commons.block_len
    - len(output) = commons.block_len
    '''
    result = plaintext
    for i in range(2**work_factor):
        result = work_factor_func(result, keys, salt)
    return result

def work_factor_func(fin: list[int], key: list[int], salt: list[int]) -> list[int]:
    '''
    - len(fin) = commons.block_len
    - len(key) = commons.block_len
    - len(salt) = commons.block_len
    - len(output) = commons.block_len
    '''
    result = box(fin, key)
    result = helper.listbin_xor(salt, result)
    return result

def box(fin: list[int], key: list[list[int]]) -> list[int]:
    '''
    - len(fin) = commons.block_len
    - len(key) = commons.box_round_count
    - len(output) = commons.block_len
    '''
    result = fin
    for i in range(commons.box_rounds_count):
        result = round(result, key[i])
    
    result = last_round(result, key[-2], key[-1])

    return result

def round(fin: list[int], key: list[int]) -> list[int]:
    '''
    - len(fin) = commons.block_len
    - len(key) = commons.block_len // 2
    - len(output) = commons.block_len
    '''
    half = len(fin) // 2
    left_half = fin[:half]
    right_half = fin[half:]
    left_result = helper.listbin_xor(left_half, key)
    left_result = w(left_result)
    left_result = helper.listbin_xor(left_result, right_half)

    return left_result + left_half

def last_round(fin: list[int], p_left: list[int], p_right: list[int]) -> list[int]:
    '''
    - len(fin) = commons.block_len
    - len(p_left) = len(p_right) = commons.block_len // 2
    - len(output) = commons.block_len
    '''
    half = len(fin) // 2
    left_half = fin[:half]
    right_half = fin[half:]

    right_result = helper.listbin_xor(left_half, p_left)
    left_result = helper.listbin_xor(right_half, p_right)

    return left_result + right_result


def w(fin: list[int]) -> list[int]:
    '''
    - len(fin) = commons.block_len // 2
    - len(output) = commons.block_len // 
    - TODO: sbox count always are 4
    '''
    sbox_input_len = len(fin) // 4
    first_8_bit = fin[:sbox_input_len]
    second_8_bit = fin[sbox_input_len:sbox_input_len*2]
    third_8_bit = fin[sbox_input_len*2:sbox_input_len*3]
    forth_8_bit = fin[sbox_input_len*3:sbox_input_len*4]

    r0 = sbox_func(first_8_bit, 0)
    r1 = sbox_func(second_8_bit, 1)
    r2 = sbox_func(third_8_bit, 2)
    r3 = sbox_func(forth_8_bit, 3)

    result = helper.listbin_add(r0, r1)
    result = helper.listbin_xor(result, r2)
    result = helper.listbin_add(result, r3)

    return result

def sbox_func(fin: list[int], which: int) -> list[int]:
    '''
    - len(fin) = commons.block_len // 8
    - len(output) = commons.block_len // 2
    '''
    row_index = helper.listbin_to_int(fin[1:6])
    col_index = helper.listbin_to_int([fin[0], fin[6], fin[7]])
    if which == 0:
        return sbox.sbox1[row_index][col_index]
    elif which == 1:
        return sbox.sbox2[row_index][col_index]
    elif which == 2:
        return sbox.sbox3[row_index][col_index]
    elif which == 3:
        return sbox.sbox4[row_index][col_index]

