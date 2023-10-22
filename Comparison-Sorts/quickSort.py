def main():	
    	# quick sort = moves smaller elements to left of a pivot.
    	#			   recursively divide array in 2 partitions

    	#                       run-time complexity = Best case O(n log(n))
    	#				   		                   Average case O(n log(n))
    	#				   		                   Worst case O(n^2) if already sorted
    	
    	#                       space complexity    = O(log(n)) due to recursion
    	
        intArray = [8, 2, 5, 3, 9, 4, 7, 6, 1]
        
        quickSort(intArray, 0, len(intArray) - 1)
        
        for i in intArray:
            print(str(i) + " ")
        

def quickSort(sortingArray: list[int], start: int, end: int):
		
		if(end <= start): return
		
		pivot = partition(sortingArray, start, end)
		quickSort(sortingArray, start, pivot - 1)
		quickSort(sortingArray, pivot + 1, end)		
	
def partition(sortingArray: list[int], start: int, end: int):
		
		pivot = sortingArray[end]
		i = start - 1
		j = start
		while j <= end:
			if sortingArray[j] < pivot:
				i+= 1
				temp = sortingArray[i]
				sortingArray[i] = sortingArray[j]
				sortingArray[j] = temp
			j+= 1
		
		i+= 1
		temp = sortingArray[i]
		sortingArray[i] = sortingArray[end]
		sortingArray[end] = temp
		
		return i
	
if __name__ == "__main__":
    main()