# Build a Caesar Cipher

# Description:
'''
Build a Caesar cipher program in Python that can encrypt and decrypt text by shifting each letter in the alphabet by a given number of positions. 
The function should support both uppercase and lowercase letters, validate the shift value, and return the transformed message based on whether encryption or decryption is selected.
'''
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# decrypt code
def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text=decrypt(encrypted_text,13)
print(decrypted_text)