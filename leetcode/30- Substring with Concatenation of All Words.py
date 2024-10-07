class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        n = len(s)
        num_w = len(words)
        len_w = len(words[0])
        total_w_len = num_w * len_w

        if total_w_len > n:
            return []

        word_code: Dict[str, int] = dict()
        for word in words:
            word_code[word] = hash(word)

        total_w_code = sum(word_code[word] for word in words)

        s_chunk_len_w_code = []
        for i in range(n - len_w + 1):
            partial = s[i: i + len_w]
            s_chunk_len_w_code.append(hash(partial))

        
        s_chunk_full_w_code = []
        for i in range(n - total_w_len + 1):
            if i < len_w:
                acc_sum = 0
                for j in range(num_w):
                    acc_sum += s_chunk_len_w_code[i + len_w * j]
                s_chunk_full_w_code.append(acc_sum)
                continue
            previous = s_chunk_full_w_code[i - len_w]
            current = previous - s_chunk_len_w_code[i - len_w] + s_chunk_len_w_code[i + len_w * (num_w -1)]
            s_chunk_full_w_code.append(current)

        candidate_indices = [i for i in range(n - total_w_len + 1) if s_chunk_full_w_code[i] == total_w_code]

        return candidate_indices
