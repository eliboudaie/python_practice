def word_check(str1, str2):
    """ Checks if one string can be translated to another with a unique code
    :param str1: Original string
    :param str2: String to check if it can be translated
    :return: True is possible, False if not
    """
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