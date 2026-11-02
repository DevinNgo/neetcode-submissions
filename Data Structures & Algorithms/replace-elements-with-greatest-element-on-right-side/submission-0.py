class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        for i, num in enumerate(arr):
            new_arr.append(max(arr[i+1:])) if i < len(arr)-1 else new_arr.append(-1)
        return new_arr