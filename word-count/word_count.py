from collections import Counter
import re

def word_count(string):
    """return the words counted in the given string """
    return Counter(re.findall(r'[^\W_]+', string.lower()))
