class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king= kingName
        self.kingdom= defaultdict(list)
        self.dead= set()

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        res= []
        def dfs(name):
            if name not in self.dead:
                res.append(name)
            if name not in self.kingdom:
                return
            
            for child in self.kingdom[name]:
                dfs(child)
        dfs(self.king)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()