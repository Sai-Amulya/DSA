# Brute Force
def slidingfixed(nums,k):
    for L in range(len(nums)):
        for R in range(L+1, min(len(nums),L+k)):
            if nums[L] == nums[R]:
                return True
    return False

# Optimal
def slidingfixedOpt(nums, k):
    window = set()
    L = 0
    for R in range(len(nums)):
        if R-L+1 > k:
            set.remove(nums[L])
            L+=1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False