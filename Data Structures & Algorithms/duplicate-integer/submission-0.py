class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = [int]
        for current_number in nums:
            if current_number not in contains:
                contains.append(current_number)
            else:
                return True
        return False