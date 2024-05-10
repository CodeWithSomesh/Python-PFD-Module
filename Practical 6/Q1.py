def onlyUnicode(val):
    sumOfUnicodeVal = 0

    for i in val:
        unicodeVal = ord(i)
        sumOfUnicodeVal += unicodeVal

    return sumOfUnicodeVal

def unicode_and_position(val):
    sumOfUnicodeVal = 0

    for i in val:
        newVal = ord(i) * (val.index(i) + 1)
        sumOfUnicodeVal += newVal

    return sumOfUnicodeVal

def hornerMethod(val):
    sumOfUnicodeVal = 0
    hash = 0

    for i in val:
        newVal = 5 * hash + ord(i)
        sumOfUnicodeVal += newVal

    return sumOfUnicodeVal



if __name__ == '__main__':
    value = 'Val'

    hashCode = hornerMethod(value)
    print(hashCode)