def binary_search(nums: list[int], target: int) -> bool:
    """
    space: O(1)
    time: O(logn)
    """
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        if target > nums[mid]:
            left = mid + 1
            continue

        right = mid

    return False
