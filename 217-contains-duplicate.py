# uses a hashset data structure to keep track of the elements seen 
# so far and returns True if a duplicate is found, otherwise it returns False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False