class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files= defaultdict(list)
        
        for path in paths:
            path= path.split(" ")
            folder= path[0]
            
            for s in path[1:]:
                s=s.split('.txt')
                c= s[1]
                name= s[0]
                files[c].append((folder, name))
                
        res= []
        for idx,file in files.items():
            if len(file)>1:
                temp= []
                for folder, name in file:
                    temp.append(folder+ '/' + name+ '.txt')
                res.append(temp)
        return res
            