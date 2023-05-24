import math

def encrypt(message, key):
    message = message.replace(" ", "")
    num_rows = key
    num_cols = math.ceil(len(message) / num_rows)

    arr = [[' ' for j in range(num_cols)] for i in range(num_rows)]
    k = 0

    for j in range(num_cols):
        for i in range(num_rows):
            if k < len(message):
                arr[i][j] = message[k]
                k += 1
            else:
                break
    ciphertext = ""

    for i in range(num_rows):
        for j in range(num_cols):
            ciphertext += arr[i][j]
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "")
    num_rows = key
    num_cols = math.ceil(len(ciphertext) / num_rows)
    arr = [[' ' for j in range(num_cols)] for i in range(num_rows)]
    k=0

    for i in range(num_rows):
        for j in range(num_cols):
            if k < len(ciphertext):
                arr[i][j] = ciphertext[k]
                k+= 1
    message = ""
    k = 0
    for j in range(num_cols):
        for i in range(num_rows):
            if k < len(ciphertext):
                if arr[i][j] != ' ':
                    message += arr[i][j]
                    k += 1
            else:
                break
    return message


# print("Enter the message :")
message = input("enter the message")
key = int(input("enter the size of key"))

ciphertext = encrypt(message, key)
print("Encrypted message:", ciphertext)

decrypted: str = decrypt(ciphertext, key)
print("Decrypted message:", decrypted)





