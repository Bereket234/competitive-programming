class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        reps= [i for i in range(26)]
        
        def find_rep(node):
            while node != reps[node]:
                node= reps[node]
            return node
        
        for equation in equations:
            if equation[1] == "=":
                rep1= find_rep(ord(equation[0]) - 97)
                rep2= find_rep(ord(equation[3]) - 97)
                reps[rep1] = rep2
        
        for equation in equations:
            c1= find_rep(ord(equation[0])-97)
            c2= find_rep(ord(equation[3]) -97)
            op= equation[1]
            if op == "=" and c1 != c2:
                return False
            if op == "!" and c1 == c2:
                return False
        
        return True