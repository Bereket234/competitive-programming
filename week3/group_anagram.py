class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        val = ''

        for string in strs:
            val = "".join(sorted(string))
            if val in counter:
                counter[val].append(string)
            else:
                counter[val] = [string]
        return counter.values()
