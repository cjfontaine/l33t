class Solution:
  def subsetSum(self, numberToFind: int, nums: list[int]):
    powerSet = self.powerSet(nums)

    for set in powerSet:
      if sum(set) == numberToFind:
        print(set)

  def powerSet(self, nums: list[int]) -> list[list[int]]:
    powerSet: list[list[int]] = []
    
    i = 0
    while i < len(nums):
      j = len(powerSet) - 1
      while j >= 0:
        set = powerSet[j]
        new_set = set.copy()
        new_set.append(nums[i])
        powerSet.append(new_set)
        j-=1
      powerSet.append([nums[i]])
      i+=1

    return powerSet


nums=[1, 2, 3, 4, 5, 9, 10, 14, 17, 19, 25]
numberToFind=32

Solution().subsetSum(
  numberToFind=numberToFind,
  nums=nums
)
