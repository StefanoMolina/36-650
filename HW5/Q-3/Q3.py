def one_away(word1, word2):
    if len(word1) < len(word2):
        temp = list(word1)
        word1 = list(word2)
        word2 = temp
    else: 
        word1 = list(word1)
        word2 = list(word2)   
    if len(word1) != len(word2):
        diff = 0
        for i in range(0,len(word1)):
                if diff ==1 and i == len(word1):
                    return 'TRUE'
                elif word1[i] != word2[i] and diff == 0:
                    diff +=1
                elif word1[i] != word2[i+diff]:
                    return 'FALSE'
                else: 
                    return 'TRUE'
    else:
        count = 0
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                count += 1
            else:
                continue
        if count > 1:
            return 'FALSE'
        else:
            return 'TRUE'
one_away('pale', 'ple')

