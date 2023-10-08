import random

def main():
    numbers = [1,3,5,4,9,6,8,7,2,0]
    while(isSorted(numbers) == False):
        for x in range(len(numbers)):
            print(numbers[x])
        random.shuffle(numbers)
    print("Sorted!")

def isSorted(nums):
    l = len(nums)
    for x in range(0, l-1):
        if nums[x] > nums[x + 1]:
            return False
    return True

if __name__ == "__main__":
    main()