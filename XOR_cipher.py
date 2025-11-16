plain = input("Enter plaintext string: ")

key = input("Enter a key: ")

while key == "":
    key = input("Enter a valid key: ")

cipher = ""

for i in range(len(plain)):
    ascii_plain = bin(ord(plain[i]))[2:]
    ascii_key = bin(ord(key[i % len(key)]))[2:]
   
    new = ""
    for k in range(7):
        if(ascii_plain[k] == ascii_key[k]):
            new += "0"
        else:
            new += "1"
    cipher += str(int(new, 2)) + " "
   
   
print(cipher)

