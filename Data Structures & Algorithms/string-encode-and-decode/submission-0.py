class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            len_word = len(word)
            prefix = len_word + 200
            encoded_str += str(prefix) + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_res = []
        len_start_idx = 0
        while len_start_idx<len(s):
            len_end_idx = len_start_idx+2
            word_len = int(s[len_start_idx:len_end_idx+1]) - 200
            word = s[len_end_idx+1:len_end_idx+1+word_len]
            # print("word", word)
            # print(word_len, len_start_idx, len_end_idx)
            decoded_res.append(word)
            len_start_idx = len_end_idx+word_len+1
            # print("decoded_res", decoded_res)
        return decoded_res


