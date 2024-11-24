def merge(nums,start,mid,end):
    i = start
    j = mid
    temp = []
    while i<mid and j<end:
        if nums[i]<=nums[j]:
            temp.append(nums[i])
            i+=1
        else:
            temp.append(nums[j])
            j+=1
    while i<mid:
        temp.append(nums[i])
        i+=1
    while j<end:
        temp.append(nums[j])
        j+=1
    for k in range(len(temp)):
        nums[start+k] = temp[k]

def mergesort(nums,start,end):
    if start<end:
        mid = (start+end)//2
        mergesort(nums,start,mid)
        mergesort(nums,mid+1,end)
        merge(nums,start,mid,end)

nums = [2,4,5,1,3,6]
mergesort(nums,0,len(nums))
print(nums)