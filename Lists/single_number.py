# https://leetcode.com/problems/single-number/

def singleNumber(self, nums: List[int]) -> int:
        
    res = 0

    for i in range(0,len(nums),1):
        res ^= nums[i]
        
    return res

# Time Complexity O(n)
# Space Complexity O(1)



