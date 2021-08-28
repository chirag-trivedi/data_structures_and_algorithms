class Solution:
    def rob(self, nums: List[int]) -> int:
        
        length = len(nums)
        table = [0 for i in range(length+1)]

        table[length] = 0

        for i in range(length-1,-1,-1):

            first = table[i+2] if i +2 <= length -1 else 0

            table[i] = max(nums[i] + first,table[i+1])


        return table[0]
