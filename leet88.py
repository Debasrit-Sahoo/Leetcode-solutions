def merge(nums1,m,nums2,n):
        i, j= m-1,n-1
        for w in range(m+n-1, -1, -1):
            if (j < 0 or nums1[i] > nums2[j]) and i >= 0:
                print(nums1)
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1                        
