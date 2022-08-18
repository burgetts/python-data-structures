def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    # Get sum of nums in list
    # Start at start point if it exists
    # End at end point if it exists, if greater than length, ignore
    sum = 0
    if end != None and end > len(nums):
        end = len(nums)-1
    if start != None and end != None:
        for i in range(start,end+1):
            sum += nums[i]
    elif start != None and end == None:
        for i in range(start, len(nums)):
            sum += nums[i]
    elif start == None and end != None:
        for i in range(end):
            sum += nums[i]
    return sum

