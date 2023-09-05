def numSubarrayProductLessThanK(nums, k):
        if k <= 1:
            return 0
        product = 1
        result = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            result += right - left + 1
        return result
nums = [10,5,2,6] 
k = 100
print(numSubarrayProductLessThanK(nums,k))