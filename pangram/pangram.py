def is_pangram(string):
    """Return True if the string is Pangram and False if the string is not Pangram """
    return not set('abcdefghijklmnopqrstuvwxyz') - set(string.lower())
