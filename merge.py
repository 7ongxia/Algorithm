class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1)
        index = 0
        
        if length == len(nums2):
            for i in range(length):
                temp = nums2.pop(0)
                nums1.insert(i, temp)
                nums1.pop()
        
        while nums2:
            lenNums2 = len(nums2)
            i = nums2.pop(0)
            for j in range(index, length-lenNums2):
                if i < nums1[j]:
                    # shift array
                    nums1.insert(j, i)
                    nums1.pop()
                    # insert i
                    index = j + 1
                    # escape for loop
                    break
                elif j == length-lenNums2-1:
                    nums1.insert(j+1, i)
                    nums1.pop()
                    index = j + 1