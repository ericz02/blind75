def maxSubArray(nums):
    # Initialize variables to keep track of the current maximum sum and the maximum sum seen so far
    current_sum = max_sum = nums[0]

    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        # Calculate the sum of the current element and the previous subarray or start a new subarray if it's greater
        current_sum = max(nums[i], current_sum + nums[i])

        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)

    # Return the maximum sum
    return max_sum
