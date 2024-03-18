'''
NOTE
- productExceptSelf phep gan la phep toan thuc hien
- res[i] can duoc cap nhap, cap nhat theo bien prefix
- res[i] can ket qua tu vong lap truoc va res[0] can gia tri mac dinh
-> tinh toan prefix sau res[i] trong vong lap 


TWO SUM
class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        check_list = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in check_list:
                return [check_list[diff], i]
            check_list[n] = i
        return

nums = [1, 2, 3, 4 ,5]
target = 6
solution  = Solution()
print(solution.twoSum(nums, target))
'''

'''
# CONTAINS DUPLICATE
# Solution 1
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        check_list = {}
        for i, n in enumerate(nums):
            if n in check_list:
                return True
            check_list[n] = i
        return False

# Solution 2
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1
        return False

nums = [1,2,3,4]
solution  = Solution()
print(solution.containsDuplicate(nums))
'''

# Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        res = [1] * len(nums)
        # bien cap nhat cho viec gan
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        posfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= posfix
            posfix *= nums[i]
        return res
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))

'''
Làm thêm 2 solution
- Chia
- Tạo ra 2 mảng prefix và postfix
'''



