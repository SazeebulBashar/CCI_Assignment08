def bs2(nums):
    l,r=0,len(nums)-1
    while l<=r:
        if nums[l] < nums[r]:
            return nums[l]
        m= l+(r-l) //2
        if nums[m] >= nums[l]:
            l=m+1
        else:
            r=m-1

print(bs2([3,4,5,1,2]))
print(bs2([4,5,6,7,0,1,2]))
print(bs2([11,13,15,17]))

# time -> O(log n)
# space -> O(1)