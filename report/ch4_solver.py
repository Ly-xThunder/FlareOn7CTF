
def canoodle(panjandrum = "", ardylo = 0, s = 0, bibble = None):
    quean = 0
    cattywampus = 0
    kerfuffle = [ 0 for _ in range(0, s) ]
    for cattywampus in range(0, len(panjandrum), 4):
        if quean == len(kerfuffle):
            print("pi = {0}, catty = {1}".format(pi, cattywampus))
            break
        pi = cattywampus + ardylo
        eb = (int(panjandrum[pi:pi+2], 16) & 0xFF)
        key = bibble[quean % len(bibble)]
        res = eb ^ key
        kerfuffle[quean] = res
        quean += 1
    return kerfuffle

buff = bytearray("FLARE-ON", "ascii")
buff.reverse()

decbytes = canoodle(F_T, 2, (0x5C21 * 14), buff)
f = open("v.png", "wb")
f.write(bytearray(decbytes))
f.close()
print("Done")