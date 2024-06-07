import operators

def box(fin: list[int], key: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len
    - len(key) = commons.boxin_len
    - len(output) = commons.boxin_len
    '''
    pass

def work_factor(fin: list[int], key: list[int], salt: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len
    - len(key) = commons.boxin_len
    - len(salt) = commons.boxin_len
    - len(output) = commons.boxin_len
    '''
    result = box(fin, key)
    result = operators.list_xor(salt, result)
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
    result = operators.list_xor(left_half, key)
    result = w(result)

    # return right_half + left_half
    pass

def last_round(fin: list[int], key: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len
    - len(key) = commons.boxin_len
    - len(output) = commons.boxin_len
    '''
    pass

def w(fin: list[int]) -> list[int]:
    '''
    - len(fin) = commons.boxin_len // 2
    - len(output) = commons.boxin_len // 2
    '''
    pass