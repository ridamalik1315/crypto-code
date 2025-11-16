def rsa(h, k, n):
    return h ** k % n

#do we have plaintext or ciphertext?
opt = int(input("1: Coding or 2: Decoding"))


if opt == 1:
    plain = input("Enter the plaintext: ")
   
    k = int(input("Enter the key exponent: "))
   
    n = int(input("Enter the mod base: "))
   
    cipher = ""
   
    for letter in plain:
        asc = ord(letter)
        newasc = rsa(asc, k, n)
        cipher += (str(newasc) + " ")
   
    print(cipher)
else:
    cipher = input("Enter the ciphertext: ")
   
    k = int(input("Enter the key exponent: "))
   
    n = int(input("Enter the mod base: "))
   
    l = [int(i) for i in cipher.split()]
   
    plain = ""
    for num in l:
        newasc = rsa(num, k, n)
        plain += chr(newasc)
    print(plain)
