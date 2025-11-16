import random
import math

def isPrime(x):
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

minimum = int(input("Enter a large integer: "))

primes = []

for i in range(100):
    if isPrime(minimum + i):
        primes.append(minimum + i)

p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)

#print("P: ", p)
#print("Q: ", q)

n = p * q
phi = (p - 1) * (q - 1)

numKeys = int(input("How many keys do you want? "))
#Generate ONE key pair
possE = []

for i in range(2, phi):
    if math.gcd(phi, i) == 1:
        possE.append(i)

for i in range(numKeys):
    e = random.choice(possE)
    possE.remove(e)
    d = 1
   
    while e * d % phi != 1:
        d += 1
   
    print("Public Key:(" + str(e) + ", " + str(n) + ")")
    print("Private Key:(" + str(d) +", " + str(n) + ")")
    print("")

