def two_sum(nums, target):
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]


print(two_sum([3, 3, 4, 2], 6))
