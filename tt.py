"""
Introduction to Transposition Techniques
The transposition technique is a cryptographic technique that converts the plain text to cipher text by performing permutations on the plain text, i.e., changing each character of plain text for each round. It includes various techniques like the Rail Fence technique, Simple columnar transposition technique, simple columnar transposition technique with multiple rounds, Vernam cipher, and book Cipher to encrypt the plain text in a secure way.
"""
def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue
    return ciphertext
print('Encrypt Message : '+encode('3214', input('Enter Message : ')))
