def kadanesliding(nums):
    maxSum = nums[0]
    currSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if currSum < 0:
            currSum = 0
            L = R
        currSum += nums[R]
        if currSum > maxSum:
            maxSum = currSum
            maxL, maxR = L, R
    return [maxL, maxR]

            

def kadanes(nums):
    maxSum = nums[0]
    currSum = 0

    for n in nums:
        currSum = max(currSum, 0)
        currSum += n
        maxSum = max(currSum, maxSum)
    return maxSum

def maxSum(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            maxSum = max(maxSum, currSum)
    return maxSum