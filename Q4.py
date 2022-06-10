from msvcrt import LK_LOCK


print("Input eight integers:")
nums = list(map(int, input().split()))
nums.sort()




print("After sorting the said ntegers:")
print(*nums)