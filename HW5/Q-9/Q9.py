def palindrome(word):
    word = list(word)
    if len(word) == 1:
        return 'TRUE'
    elif len(word) <= 3 and word.pop(0) == word.pop(len(word)-1):
        return 'TRUE'
    elif word.pop(0) == word.pop(len(word)-1) and len(word) > 3:
        return palindrome(''.join(word))
    elif word.pop(0) != word.pop(len(word)-1):
        return 'FALSE'
    else:
        return 'TRUE'