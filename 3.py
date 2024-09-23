#  Remove Subarrays
nums = [1,2,4,3]

i, n = 0, len(nums)
flag = False
while i + 1 < n and nums[i] < nums[i + 1]:
    i += 1
if i == n - 1:
    print(n * (n + 1) // 2)
    flag = True
ans = i + 2
j = n - 1
while j:
    while i >= 0 and nums[i] >= nums[j]:
        i -= 1
    ans += i + 2
    if nums[j - 1] >= nums[j]:
        break
    j -= 1
if not flag:
    print(ans)
        