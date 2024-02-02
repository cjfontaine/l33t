def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        print(f'm={m-1}')
        print(f'n={n-1}')
        if nums1[m-1] >= nums2[n-1]:
            print(f'nums1[{m+n-1}]={nums1[m-1]}')
            nums1[m+n-1] = nums1[m-1]
            m=m-1
        else:
            print(f'nums1[{m+n-1}]={nums2[n-1]}')
            nums1[m+n-1] = nums2[n-1]
            n=n-1
        print('-------')
    if n > 0:
        nums1[:n] = nums2[:n]


array1=[1,2,3,0,0,0]
array2=[2,5,6]
merge(
    nums1=array1,
    m=3,
    nums2=array2,
    n=3
)

print(array1)

# nums1=[1,2,3,0,0,0]
# nums2=[2,5,6]

# m = 3
# n = 3

# nums1[2] = 3
# nums2[2] = 6
# Choose 6
# [1,2,3,0,0,6]

# nums1[2] = 3
# nums2[1] = 5
# Choose 5
# [1,2,3,0,5,6]

# nums1[2] = 3
# nums2[0] = 2
# Choose 3
# [1,2,3,3,5,6]

# nums1[1] = 2
# nums2[0] = 2
# Choose 2
# [1,2,2,3,5,6]

# nums1[0] = 1
# nums2[0] = 2
# Choose 2
# [1,2,2,3,5,6]