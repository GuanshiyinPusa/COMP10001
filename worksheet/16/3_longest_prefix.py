def longest_prefix(word1, word2):
    if not word1 or not word2:
        return ""
    
    if word1[0] != word2[0]:
        return ""
    
    return word1[0] + longest_prefix(word1[1:], word2[1:])