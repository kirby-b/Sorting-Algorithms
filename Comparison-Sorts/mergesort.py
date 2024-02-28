def main():
    # merge sort = recursively divide nums array in 2, sort, re-combine
    # run-time complexity = O(n Log n)
    # space complexity    = O(n)

    nums = [8, 2, 5, 3, 4, 7, 6, 1]

    merge_sort(nums)

    for x in range(len(nums)):
        print(nums[x], end=" ")


def merge_sort(nums):
    length = len(nums)
    if length <= 1: return nums  # base case

    middle = length / 2
    leftnums = []
    rightnums = []

    i = 0  # left array
    j = 0  # right array

    for i in range(length):
        if i < middle:
            leftnums.append(nums[i])
        else:
            rightnums.append(nums[i])
            j += 1

    merge_sort(leftnums)
    merge_sort(rightnums)
    merge(leftnums, rightnums, nums)


def merge(leftnums, rightnums, nums):
    left_size = len(nums) / 2
    right_size = len(nums) - left_size
    i = 0
    left = 0
    right = 0  # indices

    # check the conditions for merging
    while left < left_size and right < right_size:
        if leftnums[left] < rightnums[right]:
            nums[i] = leftnums[left]
            i += 1
            left += 1
        else:
            nums[i] = rightnums[right]
            i += 1
            right += 1

    while left < left_size:
        nums[i] = leftnums[left]
        i += 1
        left += 1

    while right < right_size:
        nums[i] = rightnums[right]
        i += 1
        right += 1


if __name__ == "__main__":
    main()
