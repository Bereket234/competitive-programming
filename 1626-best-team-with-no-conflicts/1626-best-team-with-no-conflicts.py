class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp= [0]*len(scores)
        for i in range(len(scores)):
            scores[i]= (ages[i], scores[i])
        scores.sort()
        for i in range(len(scores)):
            dp[i]= scores[i][1]
            for j in range(i):
                if scores[j][0] < scores[i][0] and scores[j][1] > scores[i][1]:
                    continue
                dp[i] = max(dp[i], scores[i][1] + dp[j])
        return max(dp)