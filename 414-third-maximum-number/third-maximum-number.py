class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    
        first = second = third = float('-inf')

        for num in nums:

            # Ignore duplicates
            if num == first or num == second or num == third:
                continue

            # New maximum
            if num > first:
                third = second
                second = first
                first = num

            # New second maximum
            elif num > second:
                third = second
                second = num

            # New third maximum
            elif num > third:
                third = num

        if third == float('-inf'):
            return first

        return third