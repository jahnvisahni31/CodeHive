class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set()
        
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        
        return 0
