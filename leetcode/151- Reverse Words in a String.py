def find_next_word(s, start_index):
    if start_index > len(s) - 1 or start_index < 0:
        raise ValueError(f"start_index: {start_index} is out of range for s: {s}")
    
    word_start_index = -1
    word_end_index = -1

    current_index = start_index

    while current_index < len(s):
        if word_start_index != -1 and s[current_index] == " ":
            word_end_index = current_index -1
            return (word_start_index, word_end_index)
        
        if word_start_index == -1 and s[current_index] != " ":
            word_start_index = current_index

        current_index += 1

    if word_start_index == -1:
        return (len(s), len(s)) # only empty spaces. 

    return (word_start_index, len(s) - 1) # reached the end of s without another space character. 


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        start_index = 0
        while start_index < len(s):
            word_start_index, word_end_index = find_next_word(s, start_index)
            
            if word_start_index != len(s): 
                words.append(s[word_start_index: word_end_index+1])
            
            start_index = word_end_index + 1


        words.reverse()
        return " ".join(words)