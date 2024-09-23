# largest common element in two arrays

nums1 = [2,3,6,4,5,1,8,7]
nums2 = [2,4,3,5,9]

nums2 = set(nums2)
nums1 = set(nums1)

largest = 0
if(len(nums1) > len(nums2)):
    for i in nums1:
        if i in nums2 and i>largest:
            largest = i
else:
    for i in nums2:
        if i in nums1 and i>largest:
            largest = i
print(largest)