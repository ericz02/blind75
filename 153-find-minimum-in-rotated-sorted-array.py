def findMin(nums):
    # Initialize two pointers: left and right
    left, right = 0, len(nums) - 1

    while left < right:
        # Calculate the middle index
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            # If the middle element is greater than the right element,
            # the minimum element must be in the right half of the array.
            # Update the left pointer to search in the right half.
            left = mid + 1
        else:
            # If the middle element is less than or equal to the right element,
            # the minimum element is in the left half of the array or at the current index.
            # Update the right pointer to search in the left half or consider the current index as a possible minimum.
            right = mid

    # When the loop ends, the left pointer will be pointing to the minimum element.
    # Return the value at that index
    return nums[left]
