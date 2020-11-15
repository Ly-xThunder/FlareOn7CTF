import sys

def decode(encoded_sc):
    l=len(encoded_sc)/2
    decoded_sc = b""
    for i in range(l):
        block=encoded_sc[i*2:i*2+2]
        decoded_byte_low = ord(block[1]) & 0x0F
        decoded_byte_high = ((ord(block[1]) >> 4) + (ord(block[0]) & 0x0F)) & 0x0F
        decoded_byte = chr(decoded_byte_low + (decoded_byte_high << 4))
        decoded_sc += decoded_byte
    return bytearray(decoded_sc)

fsc = open(sys.argv[1], "rb")
sc = fsc.read()
fsc.close()

dsc = decode(sc)

fdsc = open(sys.argv[1], "wb")
fdsc.write(dsc)
fdsc.close()
