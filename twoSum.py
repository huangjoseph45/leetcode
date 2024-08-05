nums = [3,2,4]
target = 6

def twoSum(nums, target):
    store = {}
    for i in range(len(nums)):
        store[nums[i]] = i
    
    for i in range(len(nums)):
        if target - nums[i] in store and store[target - nums[i]] != i:
            return [i, store[target-nums[i]]]



print(twoSum(nums, target))