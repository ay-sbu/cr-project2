
from hasht import hasht
import operators

def test_given():
    plaintext = '0x111111'
    salt = '0x39c6c1e33ec00e2b'
    work_factor = 1

    plaintext = operators.num_to_list(int(plaintext, 16), 64)
    salt = operators.num_to_list(int(salt, 16), 64)

    result = hasht(plaintext, salt, work_factor)

    print(result)
    print(hex(operators.binlist_to_int(result)))



if __name__ == '__main__':
    test_given()