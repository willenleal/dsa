def bubble_sort(nums: list[int]) -> None:
    """
    space: O(1)
    time: O(n^2)
    """
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


def quick_sort(nums: list[int]) -> None:
    """
    space: O(1)
    time:
        best: O(nlogn)
        worst: O(n^2)
    """

    def sort(nums: list[int], left: int, right: int) -> None:
        if left < right:
            pivot = partition(nums, left, right)

            sort(nums, left, pivot - 1)
            sort(nums, pivot + 1, right)

    def partition(nums: list[int], left: int, right: int) -> int:
        i, j = left, right - 1

        while i < j:
            while i < right and nums[i] <= nums[right]:
                i += 1
            while j >= left and nums[j] > nums[right]:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        if nums[i] > nums[right]:
            nums[i], nums[right] = nums[right], nums[i]

        return i

    sort(nums, 0, len(nums) - 1)
