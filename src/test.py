
from hasht import hasht
import helper

def hex_test_hasht(plaintext: str, salt: str, work_factor: int, expected: str) -> bool:
    plaintext = '0x111111'
    salt = '0x39c6c1e33ec00e2b'
    work_factor = 1

    plaintext = helper.int_to_listbin(int(plaintext, 16), 64)
    salt = helper.int_to_listbin(int(salt, 16), 64)

    result = hasht(plaintext, salt, work_factor)

    return hex(helper.listbin_to_int(result)) == expected

def test_give_from_file():
    f = open('../tests/testcase.txt', 'r+')
    lines = f.readlines()
    d = []
    for i in range(len(lines) // 8):
        base = i * 8
        plaintext = lines[base + 1].split("'")[-2]
        salt = lines[base + 2].split("'")[-2]
        work_factor = lines[base + 3]
        work_factor = int(work_factor[work_factor.index(':') + 1:])
        expected = lines[base + 6].split("'")[-2]
        d.append([plaintext, salt, work_factor, expected])
    
    for i in range(len(d)):
        print(d[i])
        print(hex_test_hasht(d[0], d[1], d[2], d[3]))

if __name__ == '__main__':
    test_give_from_file()