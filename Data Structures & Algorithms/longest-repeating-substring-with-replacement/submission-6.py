class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, maxf, result = 0, 0 , 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            maxf = max(maxf, count[s[i]])
            while (i - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, i - l + 1) 
        return result       