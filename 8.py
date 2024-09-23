# longest consequtive playlist (chef song)

nums = [1,2,1,3,2,7,4,2,3,5,6,7,8,9]
temp = set()  # This will track the unique elements in the current sequence
count = 0     # This will track the current consecutive sequence length
pos = 0       # This will store the position of the start of the longest sequence
longest = 0   # This will store the length of the longest consecutive sequence
start = 0     # This will store the starting index of the current sequence

for i in range(len(nums)):
    if nums[i] not in temp:
        temp.add(nums[i])
        count += 1
    else:
        if count > longest:
            longest = count
            pos = start 

        temp.clear()
        temp.add(nums[i])
        start = i  
        count = 1 

if count > longest:
    longest = count
    pos = start

print(nums[pos:pos+longest])








