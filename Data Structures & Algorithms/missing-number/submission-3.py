class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums == list(range(len(nums))):
            return (sorted_nums[-1] +1)
        for num1, num2 in zip(sorted_nums, list(range(len(nums)))):
            if num1 != num2:
                return num2
        