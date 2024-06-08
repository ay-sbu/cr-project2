
from hasht import hasht
import helper

def hex_test_hasht(plaintext: str, salt: str, work_factor: int, expected: str) -> bool:
    plaintext = helper.int_to_listbin(int(plaintext, 16), 64)
    salt = helper.int_to_listbin(int(salt, 16), 64)

    result = hasht(plaintext, salt, work_factor)
    
    output = hex(helper.listbin_to_int(result))

    return output, (output == expected)

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
        test_and_show(d[i][0], d[i][1], d[i][2], d[i][3])

def test_and_show(plaintext: str, salt: str, work_factor: int, expected: str) -> None:
    print('plaintext:', plaintext)
    print('salt:', salt)
    print('work_factor:', work_factor)
    print('expected:', expected)
    output, test_result = hex_test_hasht(plaintext, salt, work_factor, expected)
    print('output:', output)
    print('test_result:', test_result)
    print()

if __name__ == '__main__':
    # test_give_from_file()
    test_and_show('0xa0a35e8ca7710', '0xd62af4866aafe96e', 13, '0x6c9ecb88c7a1f4fd')
    test_and_show('0xa7710', '0x59c394c357335177', 15, '0xeb2da3ee596c65df')
    test_and_show('0x111111', '0x39c6c1e33ec00e2b', 1, '0x5038d070d6e577b0')
    test_and_show('0x000000000', '0x701309b2b76e6e2d', 1, '0x13cac2db8d45d664')
