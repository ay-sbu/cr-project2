import helper
import commons
import sbox
from keys import keys

def hasht(plaintext: list[int], salt: list[int], work_factor: int) -> list[int]:
    '''
    - len(plaintext) = commons.boxin_len
    - len(salt) = commons.boxin_len
    - len(output) = commons.boxin_len
    '''
    result = plaintext
    for i in range(work_factor):
        result = work_factor_func(result, keys, salt)
    return result

def box(fin: list[int], key: list[list[int]]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len
    - len(key) = commons.box_round_count
    - len(output) = commons.boxin_len
    '''
    result = fin
    for i in range(commons.box_rounds_count):
        result = round(result, key[i])
    
    result = last_round(result, key[-2], key[-1])

    return result

def work_factor_func(fin: list[int], key: list[int], salt: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len
    - len(key) = commons.boxin_len
    - len(salt) = commons.boxin_len
    - len(output) = commons.boxin_len
    '''
    result = box(fin, key)
    result = helper.listbin_xor(salt, result)
    return result

def round(fin: list[int], key: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len
    - len(key) = commons.boxin_len
    - len(output) = commons.boxin_len
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
    - len(fin) = commons.boxin_len
    - len(p_left) = len(p_right) = commons.boxin_len
    - len(output) = commons.boxin_len
    '''
    half = len(fin) // 2
    left_half = fin[:half]
    right_half = fin[half:]

    right_result = helper.listbin_xor(left_half, p_left)
    left_result = helper.listbin_xor(right_half, p_right)

    return left_result + right_result


def w(fin: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len // 2
    - len(output) = commons.boxin_len // 2
    '''
    sbox_input_len = commons.boxin_len // 8
    first_8_bit = fin[:sbox_input_len]
    second_8_bit = fin[sbox_input_len:sbox_input_len*2]
    third_8_bit = fin[sbox_input_len*2:sbox_input_len*3]
    forth_8_bit = fin[sbox_input_len*3:sbox_input_len*4]

    col_index = helper.listbin_to_int([first_8_bit[0], first_8_bit[6], first_8_bit[7]])
    first_row_index = helper.listbin_to_int(first_8_bit[1:6])
    second_row_index = helper.listbin_to_int(second_8_bit[1:6])
    third_row_index = helper.listbin_to_int(third_8_bit[1:6])
    forth_row_index = helper.listbin_to_int(forth_8_bit[1:6])

    r0 = sbox.sbox1[first_row_index][col_index]
    r1 = sbox.sbox2[second_row_index][col_index]
    r2 = sbox.sbox3[third_row_index][col_index]
    r3 = sbox.sbox4[forth_row_index][col_index]

    result = helper.listbin_add(r0, r1)
    result = helper.listbin_xor(result, r2)
    result = helper.listbin_add(result, r3)

    return result


    
