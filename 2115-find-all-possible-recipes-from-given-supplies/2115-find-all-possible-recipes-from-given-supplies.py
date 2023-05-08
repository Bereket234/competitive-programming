class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        cnt= {}
        for i, recipe in enumerate(recipes):
            cnt[recipe]= len(ingredients[i])
        
        for supply in supplies:
            cnt[supply]= 0
        
        graph= defaultdict(list)
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
        
        que= deque(supplies)
        
        while que:
            node= que.popleft()
            
            for child in graph[node]:
                if cnt[child] != 0:
                    cnt[child] -= 1
                if cnt[child] == 0:
                    que.append(child)
                
        return [recipe for recipe in recipes if cnt[recipe] == 0]
                
            