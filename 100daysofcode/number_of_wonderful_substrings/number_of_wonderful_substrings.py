class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        count[0] = 1
        result = 0
        bitmask = 0
        
        for char in word:
            char_index = ord(char) - ord('a')
            bitmask ^= 1 << char_index
            result += count[bitmask]
            for i in range(10):
                result += count[bitmask ^ (1 << i)]
            count[bitmask] += 1
        
        return result
