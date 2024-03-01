def trydel(nums, target, ans):
    a, b, c, = 0, 0, 0
    if len(nums) < 2:
        return ans
    if sum(nums[:2]) == target:
        a = trydel(nums[2:], target, ans + 1)
    if nums[-1] + nums[-2] == target:
        b = trydel(nums[: len(nums) - 2], target, ans + 1)
    if nums[0] + nums[-1] == target:
        c = trydel(nums[1: len(nums) - 1], target, ans + 1)
    if a > b and a > c and a != 0:
        ans = a
    elif b > a and b > c and b != 0:
        ans = b
    elif c != 0:
        ans = c
    return ans


def maxOperations(nums):
    if len(nums) < 2:
        return 0
    a = trydel(nums[2:], sum(nums[: 2]), 1)
    b = trydel(nums[: len(nums) - 2], nums[-1] + nums[-2], 1)
    c = trydel(nums[1: len(nums) - 1], nums[0] + nums[-1], 1)
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c


print(maxOperations([5, 2, 1, 6, 3, 4, 4]))
