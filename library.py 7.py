
V00709162 Ziya Moore

ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"


def is_alpha(word):
    for char in word:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True


def is_digit(s):
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True


def to_lower(s):
    result = ""
    for char in s:
        if char in ASCII_UPPERCASE:
            index = ASCII_UPPERCASE.index(char)
            result += ASCII_LOWERCASE[index]
        else:
            result += char
    return result


def to_upper(s):
    result = ""
    for char in s:
        if char in ASCII_LOWERCASE:
            index = ASCII_LOWERCASE.index(char)
            result += ASCII_UPPERCASE[index]
        else:
            result += char
    return result


def find_chr(s, char):
    if len(char) != 1:
        return -1
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1


def find_str(s, substr):
    if len(substr) == 0:
        return 0  # By convention, an empty substring is found at the start
    for i in range(len(s) - len(substr) + 1):
        if s[i:i + len(substr)] == substr:
            return i
    return -1


def replace_chr(s, old, new):
    if len(old) != 1 or len(new) != 1:
        return ""
    result = ""
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result


def replace_str(s, old, new):
    if old == "":
        return new.join([char for char in s]) + new  # Inserts new between each char and at the end
    result = ""
    i = 0
    while i < len(s):
        if s[i:i + len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result



