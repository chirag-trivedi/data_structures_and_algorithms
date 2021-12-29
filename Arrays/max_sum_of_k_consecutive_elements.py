def max_sum(nums,k):
    length = len(nums)
    
    if length == k:
        return sum(nums)
    
    if k == 1:
        return max(nums)
    
    final_sum = 0
    temp_sum = 0
    for i in range(0,k,1):
        temp_sum = temp_sum + nums[i]
        
    final_sum = temp_sum
    
    for i in range(k,length,1):
        temp_sum += (nums[i] - nums[i-k])
        final_sum = max(final_sum,temp_sum)
        
        
    return final_sum
        
        

nums = [1,8,30,-5,20,7]
k = int(input())
print(max_sum(nums,k))

# Time Complexity O(n)
# Space Complexity O(1)