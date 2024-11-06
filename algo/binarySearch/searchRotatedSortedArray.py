# needs to be O(log n) - binary search

def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r: # for cases where nums is 1 val
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            # then search right portion
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            # less than middle greater than left
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    
    return -1