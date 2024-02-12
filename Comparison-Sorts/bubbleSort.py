class BubbleSort():
	
	# bubble sort = pairs of adjacent elements are compared, and the elements
	# 	            swapped if they are not in order.
	
	# Quadratic time O(n^2) so a small set is okay, but a big set is painful
	
	def main():
		
		nums = [9, 1, 8, 2, 7, 3, 6, 4, 5] #Nums to be passed in
		
		BubbleSort.bubble_sort(nums)
		
		for x in range(len(nums)): #Prints out the sorted string
			print(nums[x] , end="")
	
	def bubble_sort(array):
		for x in range(len(array) - 1):
			for y in range(len(array)- x - 1):
				if(array[y] > array[y+1]):
					temp = array[y]
					array[y] = array[y+1]
					array[y+1] = temp
				
			
if __name__ == "__main__":
	BubbleSort.main()
	
