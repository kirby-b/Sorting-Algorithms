class MergeSort():
    def main():  	
        # merge sort = recursively divide nums array in 2, sort, re-combine
        # run-time complexity = O(n Log n)
        # space complexity    = O(n)
        
        nums = [8, 2, 5, 3, 4, 7, 6, 1]
        
        MergeSort.mergeSort(nums)
        
        for x in range(len(nums)):
            print(nums[x], end=" ")


    def mergeSort(nums):
        
        length = len(nums)
        if (length <= 1): return nums#base case
        
        middle = length / 2
        leftnums = []
        rightnums = []
        
        i = 0 #left array
        j = 0 #right array
        
        for i in range(length): 
            if(i < middle):
                leftnums.append(nums[i])
            else:
                rightnums.append(nums[i])
                j+= 1

        MergeSort.mergeSort(leftnums)
        MergeSort.mergeSort(rightnums)
        MergeSort.merge(leftnums, rightnums, nums)

    def merge(leftnums, rightnums, nums):
        
        leftSize = len(nums) / 2
        rightSize = len(nums) - leftSize
        i = 0
        l = 0
        r = 0 #indices
        
        #check the conditions for merging
        while(l < leftSize and r < rightSize):
            if(leftnums[l] < rightnums[r]):
                nums[i] = leftnums[l]
                i+= 1
                l+= 1
            else:
                nums[i] = rightnums[r]
                i+= 1
                r+= 1

        while(l < leftSize):
            nums[i] = leftnums[l]
            i+= 1
            l+= 1

        while(r < rightSize):
            nums[i] = rightnums[r]
            i+= 1
            r+= 1

if __name__ == "__main__":
	MergeSort.main()
	