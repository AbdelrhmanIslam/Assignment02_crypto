import itertools
import string

ciphertext = input("Enter the encrypted message: ").lower()
alphabet = string.ascii_lowercase
# factorial (26!)
permutations = itertools.permutations(alphabet)

count = 0
for perm in permutations:
    #mapping table
    decryption_map = {enc: dec for enc, dec in zip(alphabet, perm)}

    # decryption
    decrypted_text = "".join(decryption_map.get(char, char) for char in ciphertext)

    print(f"Decryption Attempt {count + 1}: {decrypted_text}")

    count += 1

    # maximum 100000 attempts
    if count >= 100000:
        break