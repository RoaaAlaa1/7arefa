# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

        vertical_word = []
    for i in range(max_len):

def printVertically(s: str) -> List[str]:
    words = s.split()
            else:
                vertical_word.append(' ')
            if i < len(word):
                vertical_word.append(word[i])
    
    max_len = max(len(word) for word in words)
        result.append(''.join(vertical_word).rstrip())
    return result

    result = []
        for word in words: