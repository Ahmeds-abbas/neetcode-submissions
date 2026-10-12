
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxP = 0
        sset = set()

        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l += 1

            sset.add(s[r])
            maxP = max(maxP, r - l + 1)

        return maxP
