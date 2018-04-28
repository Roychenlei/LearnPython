def maxSubArray(nums):
    maxSum = currentSum = nums[0]

    for num in nums[1:]:
        if num >= currentSum:
            currentSum += num
        else:
            currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
        print maxSum
    return maxSum
a = [2,1,2,-4,45,1,3]
print maxSubArray(a)
