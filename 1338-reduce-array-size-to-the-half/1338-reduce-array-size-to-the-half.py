"""
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
dict  n=10, res_n=5
3: 4
5: 3
2: 2
7: 1
Here we first get the freq count of each item
then we sort the keys of each item as a list by the value in the dict
iterate over the key list, then retrieve the value
compare if the count of the len left if equal to the len//2 of the original 
We use reverse as we want to discard values fast
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        if len(set(arr)) == 1:
            return 1
        
        freqs = dict()
        for i in arr:
            freqs[i] = freqs.get(i,0) +1
            
        sorted_freqs = sorted(freqs, key=freqs.get, reverse=True)
        
        original_len = len(arr)
        res_len = original_len // 2
        
        removed_count = 0
        rm = []
        for k in sorted_freqs:
            v = freqs.get(k)
            if removed_count < res_len:
                removed_count += v
                rm.append(k)
        
        return len(rm)
            
        