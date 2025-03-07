import re

def generate_matrix(key):
    key = key.lower().replace("j", "i") 
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix = []
    used = set()
    for char in key:
        if char in alphabet and char not in used:
            matrix.append(char)
            used.add(char)
    for char in alphabet:
        if char not in used:
            matrix.append(char)
            used.add(char)
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)] 

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def process_pairs(text):
    text = re.sub(r'[^a-z]', '', text.lower()).replace("j", "i")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'x'
        if a == b:
            pairs.append((a, 'x'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def playfair_cipher(text, matrix, encrypt=True):
    pairs = process_pairs(text)
    result = []

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # نفس الصف -> تحريك لليمين أو لليسار
            col1 = (col1 + 1) % 5 if encrypt else (col1 - 1) % 5
            col2 = (col2 + 1) % 5 if encrypt else (col2 - 1) % 5
        elif col1 == col2:  # نفس العمود -> تحريك للأسفل أو للأعلى
            row1 = (row1 + 1) % 5 if encrypt else (row1 - 1) % 5
            row2 = (row2 + 1) % 5 if encrypt else (row2 - 1) % 5
        else:  # مستطيل -> تبديل الأعمدة
            col1, col2 = col2, col1

        result.append(matrix[row1][col1] + matrix[row2][col2])

    return "".join(result)


key = input("Enter the key 🔑: ")
matrix = generate_matrix(key)

print("\n📜 matrix Playfair:")
for x in matrix:
    print(" ".join(x))

option = input("\n🔹 choose an option (e for encrypt, d for decrypt): ").strip().lower()

if option == 'e':
    text = input("\n✏️ Enter the text: ").strip().lower()
    result = playfair_cipher(text, matrix, encrypt=True)
    print("\n🔐 ciphertext:", result)
elif option == 'd':
    text = input("\n✏️ Enter the text: ").strip().lower()
    result = playfair_cipher(text, matrix, encrypt=False)
    print("\n🔓 plaintext:", result)
else:
    print("⚠️ invalid option!")