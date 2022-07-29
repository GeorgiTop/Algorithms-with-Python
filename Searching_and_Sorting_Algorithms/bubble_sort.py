nums = [int(x) for x in input().split()]

counter = 0
is_sorted = False
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(nums)- counter):
        if nums[idx] < nums[idx-1]:
            nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
            is_sorted = False
    counter += 1

# for i in range(len(nums)):
#     for j in range(1, len(nums) - i):
#         if nums[j-1] > nums[j]:
#             nums[j], nums[j-1] = nums[j-1], nums[j]


print(*nums)

