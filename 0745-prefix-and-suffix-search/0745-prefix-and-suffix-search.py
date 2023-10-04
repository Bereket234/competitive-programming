class TrieNode:
    def __init__(self):
        self.children= {}
        self.loc= -1
        
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.root= TrieNode()
        for j,word in enumerate(words):
            for i in range(len(word)):
                self.add(word[i:] + '{' + word, j)
            
        
    
        
    def add(self, word, i):
        curr= self.root

        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr= curr.children[c]
            curr.loc=i
    def search(self, word):
        curr= self.root
        for c in word:
            if c not in curr.children:
                return -1
            curr= curr.children[c]
    
        return curr.loc

    def f(self, pref: str, suff: str) -> int:
        return self.search(suff+"{"+pref)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)