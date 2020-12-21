def fb16decode(val=0, block=4):
    if val == 0:
        return ''
    res = format(val, 'x')
    res = ('0' if len(res) % 2 != 0 else '') + res
    return ''.join([''.join([chr(127 - int(res[i:i + block * 2][::-1][j:j + 2], 16)) for j in range(0, block * 2, 2)]) for i in range(0, len(res), block * 2)]).strip('\0')

def fb16encode(val='', block=4):
    if val == '':
        return 0
    val += '\0' * ((block - len(val) % block) % block)
    return int(''.join([''.join([format(127 - ord(c), '02x') for c in val[i:i + block]])[::-1] for i in range(0, len(val), block)]), 16)

if __name__ == '__main__':
    import sys, getopt
    argv = sys.argv[1:]
    if len(argv) == 0:
        print('This is a module for encoding/decoding command lines made initially for tr.')
        exit()
    else:
        flag = None
        val = None
        block = 4
        try:
            opts, args = getopt.getopt(argv, "d:e:b:", ['decode=', 'encode=', 'block='])
        except:
            print("Error!")
            exit()
        for opt, arg in opts:
            if opt in ['-d', '--decode']:
                if flag != None:
                    print('Invalid command')
                    exit()
                elif not arg.isdigit():
                    print('Invalid argument')
                    exit()
                else:
                    flag = 'd'
                    val = int(arg)
            elif opt in ['-e', '--encode']:
                if flag == None:
                    flag = 'e'
                    val = arg
                else:
                    print('Invalid command')
                    exit()
            elif opt in ['-b', '--block']:
                if arg.isdigit():
                    block = int(arg)
                else:
                    print('Invalid block value')
                    exit()
        if flag == 'd':
            print(fb16decode(val, block))
        elif flag == 'e':
            print(fb16encode(val, block))

'''
Flipped-Block-Hexadecimal Encoder (fb16)
Algorithm:
Append null character until len(str) % block == 0
For each substr of block characters:
    The new character each in a substr is 127 - ascii code of the character in hexadecimal
    Flip and append the string result to a new string
Convert the hexadecimal string into int
'''
