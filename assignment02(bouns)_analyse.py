import collections
import string #عشان اجيب الحروف الابجديه

def decrypt_with_frequency(ciphertext):
    english_freq = "etaoinshrdlcumwfgypbvkjxqz" # arrange of frequency letters

    # count the number of characters bears in the string
    letter_counts = collections.Counter(char for char in ciphertext if char in string.ascii_lowercase)

    decryption_map = {enc: dec for enc, dec in zip([x[0] for x in letter_counts.most_common()], english_freq)}

    # decryption function for english frequency
    return "".join(decryption_map.get(char, char) for char in ciphertext)

ciphertext = input("Enter encrypted text: ").lower()
print("\n🔓 Possible Decryption:", decrypt_with_frequency(ciphertext))