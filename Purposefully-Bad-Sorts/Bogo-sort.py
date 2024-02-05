import random
class BogoSort():
    def main():
        numbers = [1,3,5,4,9,6,8,7,2,0]
        while(BogoSort.is_sorted(numbers) == False):
            for x in range(len(numbers)):
                print(numbers[x])
            random.shuffle(numbers)
        #Randomizes the list item positions until the list is sorted
        print("Sorted!")
    
    def is_sorted(nums):
        l = len(nums)
        for x in range(0, l-1):
            if nums[x] > nums[x + 1]:
                return False
        return True
        #Checks if it is sorted
    
    if __name__ == "__main__":
        main()
