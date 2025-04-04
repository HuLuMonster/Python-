def fun(x):
    i = 0
    num = x
    nums1 = []
    while num != 0:
        nums1.append(num % 10)
        num = num / 10
        i = i + 1
    nums2 = nums1[::-1]
    if nums1 == nums2:
        return True
    else:
        return False
