def search(nums, target):
    left = 0  # Initialize the left pointer
    right = len(nums) - 1  # Initialize the right pointer

    while left <= right:  # Perform binary search until left exceeds right
        mid = (left + right) // 2  # Calculate the middle index

        if nums[mid] == target:  # Check if the middle element is the target
            return mid

        if nums[left] <= nums[mid]:  # If the left half is sorted
            if nums[left] <= target < nums[mid]:  # Check if the target is within the left half
                right = mid - 1  # Update the right pointer to search in the left half
            else:
                left = mid + 1  # Update the left pointer to search in the right half
        else:  # If the right half is sorted
            if nums[mid] < target <= nums[right]:  # Check if the target is within the right half
                left = mid + 1  # Update the left pointer to search in the right half
            else:
                right = mid - 1  # Update the right pointer to search in the left half

    return -1  # Return -1 if the target element is not found
