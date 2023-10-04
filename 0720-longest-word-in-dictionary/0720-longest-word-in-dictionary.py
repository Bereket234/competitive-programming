class TrieNode:
    def __init__(self):
        self.children= {}
        
class Solution:
    def __init__(self):
        self.root= TrieNode()
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res= ''
        print(words)
        def add(word):
            curr= self.root
            def dfs(i, node):
                nonlocal res
                if len(word) == i or word[i] not in node.children:
                    if len(word) - 1 == i:
                        if len(word) > len(res):
                            res= word
                        node.children[word[i]]= TrieNode()
                    return
                dfs(i + 1, node.children[word[i]])
            dfs(0, curr)
        for word in words:
            add(word)
        return res
                    
                
            
            