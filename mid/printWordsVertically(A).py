def printVertically(s: str) -> List[str]:
    words = s.split()
    max_len = max(len(word) for word in words)
    result = []
    
    for i in range(max_len):
        vertical_word = []
        for word in words:
            if i < len(word):
                vertical_word.append(word[i])
            else:
                vertical_word.append(' ')
        result.append(''.join(vertical_word).rstrip())
    
    return result