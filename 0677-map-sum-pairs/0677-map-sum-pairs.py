class TrieNode:
    def __init__(self):
        self.children= {}
        self.value= 0
class MapSum:
    def __init__(self):
        self.root= TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr= self.root
        for c in key:
            if c not in curr.children:
                curr.children[c]= TrieNode()
            curr= curr.children[c]
        curr.value= val

    def sum(self, prefix: str) -> int:
        res= 0
        curr= self.root
        def dfs(node):
            nonlocal res
            res+= node.value
            for child in node.children.values():
                dfs(child)
        
        for c in prefix:
            if not curr.children or c not in curr.children:
                return 0
            curr= curr.children[c]
        dfs(curr)
        return res
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)