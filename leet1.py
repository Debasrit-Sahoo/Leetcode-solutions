def twoSum(nums, target):
    hmap = {}
    for i, v in enumerate(nums):
        other_half = target - v
        if other_half in hmap:
            return [hmap[other_half], i]
        else:
            hmap[v] = i


print(twoSum([4,25,6,21,5], 10))