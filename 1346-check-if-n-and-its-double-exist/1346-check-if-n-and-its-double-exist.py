class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr[i] != 0:
                return True
            elif arr[i] == 0:
                count_z = 0
                for num in arr:
                    if num == 0: count_z += 1
                if count_z >= 2:
                    return True
                
        return False