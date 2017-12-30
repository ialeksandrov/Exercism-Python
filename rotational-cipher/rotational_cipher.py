import string


def rotate(text, key):
    cipher = []
    for char in text:
        if char in string.ascii_lowercase:
            cipher.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) + key) % 26])
        elif char in string.ascii_uppercase:
            cipher.append(string.ascii_uppercase[(string.ascii_uppercase.index(char) + key) % 26])
        else:
            cipher.append(char)
    return ''.join(cipher)
