class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for n in nums:
            if n not in a:
                a.add(n)
            else:
                return True
        return False