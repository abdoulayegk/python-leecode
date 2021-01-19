"""Given a list of integers,write a function that returns the largest sum of
non-adjacent numbers numbers can be 0 or negative."""


def find_sum(nums):
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return max(nums[0], nums[1])
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pick = (max(nums[i], nums[j]))
        result += pick
    return result//2


print(find_sum([1, 3]))
