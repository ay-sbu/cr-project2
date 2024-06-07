from random import randint
import commons
    
def list_cyclic_shift(p: list[int], count: int, dir='left'):
    if dir == 'left':
        return p[count:] + p[:count]
    else:
        return p[:count] + p[count:]
    
def module_multiply(a: int, b: int):
    return (a * b) % commons.mul_mod

def module_add(a: int, b: int):
    return (a + b) % commons.add_mod

def list_to_str(l: list[int]):
    return ''.join(map(str, l))

def list_to_num(l: list[int]):
    return int(list_to_str(l), 2)

def num_to_str(n: int, strlen: int):
    return bin(n)[2:].zfill(strlen)

def num_to_list(n: int, listlen: int):
    return list(map(int, list(num_to_str(n, listlen))))

def list_multiply(a: list[int], b: list[int]):
    a_num = list_to_num(a)
    b_num = list_to_num(b)
    
    mul = module_multiply(a_num, b_num)

    return num_to_list(mul, len(a))

def list_addition(a: list[int], b: list[int]):
    a_num = list_to_num(a)
    b_num = list_to_num(b)
    
    mul = module_add(a_num, b_num)

    return num_to_list(mul, len(a))

def list_xor(a: list[int], b: list[int]):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result