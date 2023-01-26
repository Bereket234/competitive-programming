class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l, r= 0, len(skill)-1
        res= 0
        skill.sort()
        while l < r:
            if skill[l] + skill[r] != skill[l+1] + skill[r-1]:
                return -1
            res+= skill[l] * skill[r]
            l+=1
            r-=1
        return res