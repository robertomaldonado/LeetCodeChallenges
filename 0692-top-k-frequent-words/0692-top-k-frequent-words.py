class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 1. Count freqs
        freqs = dict()
        for word in words:
            freqs[word] = freqs.get(word,0) + 1
        # 2. Add items to a max heap
        heap = []
        for ck, v in freqs.items():
            heapq.heappush(heap, (-v, ck) )
        most_k_repeated = list()
        # 3. Return k items by poping the max heap
        while k >0:
            most_k_repeated.append(heapq.heappop(heap)[1])
            k-=1
        return most_k_repeated
