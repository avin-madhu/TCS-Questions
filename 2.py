# Maximum product difference between two pairs of numbers

nums = [5,6,2,7,4,8]
nums.sort()
print((nums[-1]*nums[-2]) - (nums[0]*nums[1]))
