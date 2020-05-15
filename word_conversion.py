def word_check(str1, str2):
    if len(str1) != len(str2):
        return False
    matches = {}
    for x in range(len(str1)):
        if str1[x] in matches:
            if matches[str1[x]] != str2[x]:
                return False
        else:
            matches[str1[x]] = str2[x]
    return True


if __name__ == '__main__':
    print(word_check('abc', 'dbd'))