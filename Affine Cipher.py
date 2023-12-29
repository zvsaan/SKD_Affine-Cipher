#!/usr/bin/env python
# coding: utf-8

# In[6]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    result = ""
    m = 26  # Panjang alfabet

    for char in text:
        if char.isalpha():
            # Enkripsi hanya huruf alfabet
            if char.isupper():
                result += chr((a * (ord(char) - ord('A')) + b) % m + ord('A'))
            else:
                result += chr((a * (ord(char) - ord('a')) + b) % m + ord('a'))
        else:
            # Biarkan karakter selain alfabet tidak terenkripsi
            result += char

    return result

def affine_decrypt(ciphertext, a, b):
    result = ""
    m = 26  # Panjang alfabet
    a_inv = mod_inverse(a, m)

    if a_inv is not None:
        for char in ciphertext:
            if char.isalpha():
                # Dekripsi hanya huruf alfabet
                if char.isupper():
                    result += chr((a_inv * (ord(char) - ord('A') - b)) % m + ord('A'))
                else:
                    result += chr((a_inv * (ord(char) - ord('a') - b)) % m + ord('a'))
            else:
                # Biarkan karakter selain alfabet tidak terdekripsi
                result += char
    else:
        print("Kunci a tidak memiliki invers modular.")

    return result

# Contoh penggunaan
plaintext = "FAUZI IHSAN ANSHORI"
a = 9
b = 17

ciphertext = affine_encrypt(plaintext, a, b)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

decrypted_text = affine_decrypt(ciphertext, a, b)
print(f"Decrypted Text: {decrypted_text}")


# In[ ]:




