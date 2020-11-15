f_sprite = open("sprite.bmp", "rb")
magic_bytes = f_sprite.read()
f_sprite.close()

magic_bytes = magic_bytes[54:len(magic_bytes)]

def magic(computer_name):
    k = 0
    result = []
    txt = ""
    for i in range(len(computer_name)):
        #get a byte b
        b = computer_name[i]
        #iterate from 6 to 0
        for j in range(6, -1, -1):
            #get the current magic byte mb
            #get the LSB of mb
            #left shift it j times
            #add the result to b
            b = b + ((magic_bytes[k] & 1) << j)
            k += 1
        txt += chr(b)
        r = ((b >> 1) + ((b & 1) << 7))
        result.append(r)
    print(txt)
    return result

magic([ 0x00 for _ in range(20) ])
