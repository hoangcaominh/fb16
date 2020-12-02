if __name__ == '__main__':
    print('This is a module for encoding/decoding command lines made initially for tr.')
    exit()

def fb16decode(val=0, block=4):
    if val == 0:
        return ''

    str = format(val, 'x')
    str = ('0' if len(str) % 2 != 0 else '') + str
    return ''.join([''.join([chr(127 - int(str[i:i + block * 2][::-1][j:j + 2], 16)) for j in range(0, block * 2, 2)]) for i in range(0, len(str), block * 2)]).strip('\0')

def fb16encode(str='', block=4):
    if str == '':
        return 0
        
    str += '\0' * ((block - len(str) % block) % block)
    return int(''.join([''.join([format(127 - ord(c), '02x') for c in str[i:i + block]])[::-1] for i in range(0, len(str), block)]), 16)

'''
Flipped-Block-Hexadecimal Encoder (fb16)
Algorithm:
Append null character until len(str) % block == 0
For each substr of block characters:
    The new character each in a substr is 127 - ascii code of the character in hexadecimal
    Flip and append the string result to a new string
Convert the hexadecimal string into int
'''
