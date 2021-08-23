""" Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target. """
# from collections import defaultdict


# def twoSum(nums, target):
#     d = defaultdict(int)
#     for i in range(len(nums)):
#         d[nums[i]] = i
#     for i in range(len(nums)):
#         if target - nums[i] in d and not i == d[target - nums[i]]:
#             return [i, d[target - nums[i]]]


# print(twoSum([3, 2, 4], 6))


def twoSum(nums, target):
    store = dict()
    for i in range(len(nums)):
        sec = target - nums[i]
        if sec not in store:
            store[nums[i]] = i
        else:
            return [store[sec], i]


print(twoSum([3, 2, 4], 6))
