def is_isogram(word):
    """Return True if the given word is isogram, else return False """
    word = [char.lower() for char in word if char.isalpha()]
    for char in word:
        if word.count(char) > 1:
            return False
    return True
