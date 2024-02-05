def main():	
    	# quick sort = moves smaller elements to left of a pivot.
    	#			   recursively divide array in 2 partitions

    	#                       run-time complexity = Best case O(n log(n))
    	#				   		                   Average case O(n log(n))
    	#				   		                   Worst case O(n^2) if already sorted
    	
    	#                       space complexity    = O(log(n)) due to recursion
    	
        int_array = [8, 2, 5, 3, 9, 4, 7, 6, 1]
        
        quick_sort(int_array, 0, len(int_array) - 1)
        
        for i in int_array:
            print(str(i) + " ")
        

def quick_sort(sorting_array: list[int], start: int, end: int):
		
		if(end <= start): return
		
		pivot = partition(sorting_array, start, end)
		quick_sort(sorting_array, start, pivot - 1)
		quick_sort(sorting_array, pivot + 1, end)		
	
def partition(sorting_array: list[int], start: int, end: int):
		
		pivot = sorting_array[end]
		i = start - 1
		j = start
		while j <= end:
			if sorting_array[j] < pivot:
				i+= 1
				temp = sorting_array[i]
				sorting_array[i] = sorting_array[j]
				sorting_array[j] = temp
			j+= 1
		
		i+= 1
		temp = sorting_array[i]
		sorting_array[i] = sorting_array[end]
		sorting_array[end] = temp
		
		return i
	
if __name__ == "__main__":
    main()