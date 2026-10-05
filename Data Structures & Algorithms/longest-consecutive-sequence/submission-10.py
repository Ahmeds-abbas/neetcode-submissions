class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedf = list(set(nums))
        sortedf.sort()

        count = 1
        countmax = 1

        for i in range(len(sortedf) - 1):
            if sortedf[i] + 1 == sortedf[i + 1]:
                count += 1
            else:
                countmax = max(countmax, count)
                count = 1

        countmax = max(countmax, count)

        return countmax