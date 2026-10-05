class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0
        l = len(numbers)-1
        while r < l:
            value = numbers[r] + numbers[l]
            if value == target:
                return [r+1,l+1]
            elif value > target :
                l -= 1
            elif value < target :
                r += 1
               



