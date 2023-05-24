# import math
# msg=int(input("Enter the msg"))
#
# p=int(input("enter the value of p"))
# q=int(input("Enter the value of q"))
# n=p*q
# m=(p-1)*(q-1)
#
# for i in range(2,m):
#     if math.gcd(i,m)==1:
#         e=i
#         break
#
# for i in range(m):
#     if (e*i)%m==1:
#         d=i
#         break
#
# def encerpt(me):
#     c=pow(msg,e,n)
#     return c
#
# def decrypt(ct):
#     p=pow(ct,d,n)
#     return p
#
# print("enter the msg",msg)
# ct=encerpt(msg)
# print("enter the encrypted msg",ct)
# pt=decrypt(ct)
# print("enter the decrypted msg",pt)


import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

msg = int(input("Enter the message: "))

# Get prime values p and q
p = int(input("Enter the value of p: "))
while not is_prime(p):
    print("p is not prime. Enter a prime number.")
    p = int(input("Enter the value of p: "))

q = int(input("Enter the value of q: "))
while not is_prime(q):
    print("q is not prime. Enter a prime number.")
    q = int(input("Enter the value of q: "))

n = p * q
m = (p - 1) * (q - 1)

# Find the value of e (public key exponent)
for i in range(2, m):
    if math.gcd(i, m) == 1:
        e = i
        break

# Find the value of d (private key exponent)
for i in range(m):
    if (e * i) % m == 1:
        d = i
        break

def encrypt(message):
    c = pow(message, e, n)
    return c

def decrypt(ciphertext):
    p = pow(ciphertext, d, n)
    return p

print("Original message:", msg)
ciphertext = encrypt(msg)
print("Encrypted message:", ciphertext)
plaintext = decrypt(ciphertext)
print("Decrypted message:", plaintext)

