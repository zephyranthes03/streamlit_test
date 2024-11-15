from typing import List

class solution:
    def four_sum(self, nums:List, target:int) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if i > 0 and nums[j] == nums[j-1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j],nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right +1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                    
        return result
                                      


if __name__ == "__main__":
    board = [1,0,-1,0,-2,2]
    solution = solution()
    result = solution.four_sum(board,2)
    print(f"Result:{result}")

    # for row in board:
    #     print(row)
