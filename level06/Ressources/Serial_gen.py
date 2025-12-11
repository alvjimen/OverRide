def compute_serial(s):
    #ord is used for get the value of ascii of the char.
    v4 = (ord(s[3]) ^ 0x1337) + 6221293
    for ch in s:
        c = ord(ch)
        v4 = (v4 + ((v4 ^ c) % 0x539)) & 0xffffffff
    return v4

def main():
    s = 'level06'#Bytearr
    serial = compute_serial(s)
    print "username:", s, "serial:", serial


if __name__ == '__main__':
    main()
