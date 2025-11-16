def isValid(key):
    #returns true if the key is valid
    #false otherwise
    if len(key) > 10 or len(key) == 0:#key is too long or too short
        return False
    length = len(key)
    for i in range(length):
        if str(i) not in key:
            return False
    return True
   
plain = input("Enter a message: ")

key = input("Enter a key: ")

while not isValid(key):
    key = input("Invalid key, enter another: ")
   
#key is valid, so now do the cipher!

#what if the message is too short?
while len(plain) % len(key) != 0:
    plain += " "

#the plaintext is the right length
#its length is an integer multiple of the key length

cipher = ""

l = len(plain)

for i in range(l):
    if i != 0 and i % len(key) == 0:
        plain = plain[len(key):]
        continue
    cipher += plain[int(key[i % len(key)])]
       

print(cipher)
