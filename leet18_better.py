from collections import defaultdict
def fourSum(nums, target):
        nums.sort()
        dic = defaultdict(list)
        result = set()
        l = len(nums)
        i = 0
        while i < l:
            j = i + 1
            while j < l:
                dic[nums[i] + nums[j]].append((i, j))
                j += 1
                while j < l and nums[j] == nums[j - 1]:
                    j += 1
            i += 1 
            while i < l and nums[i] == nums[i - 1]:
                i += 1

        for x in dic:
            c = target - x
            if c not in dic:
                continue

            for (i,j) in dic[x]:
                for (k,l) in dic[c]:
                    if len({i, j, k, l}) == 4:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))

        return [list(m) for m in result]