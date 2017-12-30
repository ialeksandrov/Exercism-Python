from re import findall

def decode(message):
    new_message = findall(r'\d*.', message)
    return_message = []

    for char in new_message:
        char = list(char)
        new_char = char[-1]

        try:
            new_num = int(''.join(char[:-1]))
        except ValueError:
            new_num = 1

        return_message.append(new_num*new_char)
    return ''.join(return_message)

def encode(string):
    """new_message structured as list of lists [# occurence, letter]"""
    new_message = []

    for char in string:
        # if empty list or different char, add a new list
        if not new_message or new_message[-1][1] != char:
            new_message.append([0, char])
        # increase charCount by one
        new_message[-1][0] += 1

    new_message = map(encodeLst, new_message)
    return ''.join(new_message)

def encodeLst(charList):
    num, char = charList
    if num == 1:
        return char
    return str(num) + char
