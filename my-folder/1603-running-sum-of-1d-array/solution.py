class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for c in range(len(nums)-1):
            nums[c+1]+=nums[c]
        return nums
