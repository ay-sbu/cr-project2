
from hasht import hasht
import helper

def test_given():
    plaintext = '0x111111'
    salt = '0x39c6c1e33ec00e2b'
    work_factor = 1

    plaintext = helper.int_to_listbin(int(plaintext, 16), 64)
    salt = helper.int_to_listbin(int(salt, 16), 64)

    result = hasht(plaintext, salt, work_factor)

    print(result)
    print(hex(helper.listbin_to_int(result)))

if __name__ == '__main__':
    test_given()