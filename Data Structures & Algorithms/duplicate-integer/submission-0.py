class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        set_nums_len = len(set(nums))
        if nums_len != set_nums_len:
            return True
        return False
