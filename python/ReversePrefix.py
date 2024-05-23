class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        char_list = [x for x in word]
        first_index = word.find(ch)
        if first_index == -1:
            return word
        result = []
        for i in range(first_index, -1, -1):
            result.append(word[i])
        return "".join(x for x in result) + word[first_index + 1:]
