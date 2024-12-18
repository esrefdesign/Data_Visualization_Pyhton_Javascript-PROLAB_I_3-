class Heap:
    def __init__(self, max_heap=False):
        
        self.data = []
        self.max_heap = max_heap

    def push(self, item):
        
        if self.max_heap:
            item = (-item[0], item[1])  # Max-heap için negatif ağırlık kullan
        self.data.append(item)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        
        if not self.data:
            raise IndexError("Heap is empty")
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._heapify_down(0)
        if self.max_heap:
            item = (-item[0], item[1])  # Negatif ağırlığı tekrar pozitif yap
        return item

    def _heapify_up(self, index):
        
        parent = (index - 1) // 2
        if parent >= 0 and self._compare(self.data[index], self.data[parent]):
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
       
        left = 2 * index + 1
        right = 2 * index + 2
        smallest_or_largest = index

        if left < len(self.data) and self._compare(self.data[left], self.data[smallest_or_largest]):
            smallest_or_largest = left

        if right < len(self.data) and self._compare(self.data[right], self.data[smallest_or_largest]):
            smallest_or_largest = right

        if smallest_or_largest != index:
            self._swap(index, smallest_or_largest)
            self._heapify_down(smallest_or_largest)

    def _compare(self, child, parent):
        
        if self.max_heap:
            return child[0] > parent[0]  # Max-heap
        return child[0] < parent[0]  # Min-heap

    def _swap(self, i, j):
        
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __len__(self):
        
        return len(self.data)

    def __str__(self):
        
        return str([(-item[0], item[1]) if self.max_heap else item for item in self.data])
