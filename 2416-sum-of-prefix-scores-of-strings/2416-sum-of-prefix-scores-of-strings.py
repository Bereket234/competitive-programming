class TrieNode:
    def __init__(self):
        self.children= {}
        self.cnt= 0
class Solution:
    def __init__(self):
        self.root= TrieNode()
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        cnt= [0]*len(words)
        def add(word):
            curr= self.root
            for i in range(len(word)):
                c= word[i]
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr= curr.children[c]
                curr.cnt += 1
        
        def count(i, word):
            curr= self.root
            for c in word:
                curr= curr.children[c]
                cnt[i] += curr.cnt
        for word in words:
            add(word)
        for i in range(len(words)):
            word= words[i]
            count(i, word)
        
        return cnt
                
            