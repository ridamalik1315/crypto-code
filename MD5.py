"You have an MD5 hash of a string that you KNOW is 3 alphabetic characters, so it will brute-force find the three characters"
import hashlib

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for a in chars:
    for b in chars:
        for c in chars:
            h = hashlib.md5((a+b+c).encode('utf8'))
            if h.hexdigest() == "1340ec9c15a1484e054e28282f2ba8db":
                print(a + b + c)

