class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        pairs = list(count.items())
        pairs.sort(key=lambda x: x[1], reverse=True)

        return [pairs[i][0] for i in range(k)]