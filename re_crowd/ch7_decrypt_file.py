import sys

def decrypt(file_contents, key = 'intrepidmango'.encode()):
    enc_data = [ i for i in range(0x100) ]
    acc = 0
    j = 0
    while j < 0x100:
        acc += (enc_data[j] + (key[j % len(key)])) & 0xFF
        temp = enc_data[j]
        enc_data[j] = enc_data[acc % len(enc_data)]
        enc_data[acc % len(enc_data)] = temp
        j += 1
    enc_data.append(0)
    enc_data.append(0)
    enc_data = bytearray(enc_data)
    file_len = len(file_contents)
    i = 0
    while i < file_len:
        b = file_contents[i]
        x = 0
        v1 = (enc_data[0x100] + 1) & 0xFF
        v2 = (enc_data[v1 % len(enc_data)] + enc_data[0x101]) & 0xFF
        enc_data[0x100] = v1
        enc_data[0x101] = v2
        v3 = enc_data[v2]
        enc_data[v2] = enc_data[v1]
        enc_data[v1] = v3 & 0xFF
        x = enc_data[((enc_data[v2] + v3) & 0xFF)]
        file_contents[i] = b ^ x
        i += 1
    return file_contents

f_encrypted = open(sys.argv[1], "rb")
encrypted = f_encrypted.read()
f_encrypted.close()
decrypted  = decrypt(bytearray(encrypted))
f_decrypted = open("accounts.txt", "wb")
f_decrypted.write(decrypted)
f_decrypted.close()
print('DONE')