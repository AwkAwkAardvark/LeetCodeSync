class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, val in enumerate(nums):
            # print(f"idx: {idx}")
            # print(f"val: {val}")
            complement = target-val
            # print(f"complement: {complement}")
            # print(f'hmap so far... : {hmap}')
            if complement in hmap:
                # print("Done!")
                # print(f"idx: {idx}")
                # print(f"val: {val}")
                # print(f"hmap[complement]: {hmap[complement]}")
                return [idx, hmap[complement]]
            else:
                hmap[val]=idx
                # print(f"NOT done! Added {hmap[val]}")
                # print(f"{hmap[val]}: {idx}")
