# Minimum operations to all array values divisible by k

n = 4
k = 4
nums = [1,2,3,4]
count1,count2 =0,0
res = 0
for i in nums:
    rem = i%k
    if rem == 0:
        continue
    else:
        temp = i
        while temp%k != 0:
            count1 += 1
            temp -= 1
        temp = i
        while temp%k != 0:
            count2 += 1
            temp += 1
        res += min(count1, count2)
        count1, count2 = 0,0
print(res)
        


