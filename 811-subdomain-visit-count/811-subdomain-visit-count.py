class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited= {}
        res=[]
        
        
        for cpdomain in cpdomains:
            cnt, domain= list(cpdomain.split(' '))
            cnt= int(cnt)
            sub_domains= domain.split('.')
            prev_sub_domain= ''
            for i in range(len(sub_domains)-1, -1, -1):
                dom= sub_domains[i] + '.' + prev_sub_domain if len(prev_sub_domain) > 0 else sub_domains[i]
                visited[dom]= cnt + visited.get(dom,0)
                prev_sub_domain= dom
        for k, v in visited.items():
            res.append(str(v)+ ' ' + k)
        return res
            