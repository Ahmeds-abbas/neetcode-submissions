class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]* len(nums)
        fix = 1
        for i in range(len(nums)):
            res[i] = fix
            fix *= nums[i]

        fix2 = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= fix2
            fix2 *= nums[i]

        return res    
