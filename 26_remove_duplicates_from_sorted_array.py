class Solution:
  target = None

  def removeDuplicates(self, nums: list[int]) -> int:
    nums[:] = [num for num in nums if self.resetTarget(num) == True]

    return len(nums)
  
  def resetTarget(self, new: int) -> bool:
    if self.target is None:
      self.target = new
      return True
    elif self.target != new:
      self.target = new
      return True
    else:
      return False

def removeDuplicates(nums: list[int]) -> int:
  i = 0

  for j in range(1, len(nums)):
    if nums[i] != nums[j]:
      i+=1
      nums[i] = nums[j]

  print(nums)
  return i+1



number_of_unique_elements = removeDuplicates(
  nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
)

print(number_of_unique_elements)