class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
        
        # Check if target is present at mid
            if nums[mid] == target:
                return mid
        
        # If target is greater, ignore left half
            elif nums[mid] < target:
                low = mid + 1
            
        # If target is smaller, ignore right half
            else:
                high = mid - 1
            
    # Element is not present in the array
        return -1