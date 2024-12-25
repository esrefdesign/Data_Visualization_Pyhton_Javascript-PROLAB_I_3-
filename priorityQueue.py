class PriorityQueue:
    def __init__(self):
        self.queue = []

    def heappush(self, item):
        """Kuyruğa eleman ekler."""
        self.queue.append(item)
        self.queue.sort(reverse=True)  # Max-heap davranışı için ters sırala

    def heappop(self):
        """Kuyruktan en yüksek öncelikli elemanı çıkarır."""
        if not self.queue:
            raise IndexError("pop from empty priority queue")
        return self.queue.pop(0)  # En yüksek öncelikli elemanı çıkarır

    def is_empty(self):
        """Kuyruğun boş olup olmadığını kontrol eder."""
        return len(self.queue) == 0

    def peek(self):
        """Kuyruğun en yüksek öncelikli elemanını döndürür, ancak çıkarmaz."""
        if not self.queue:
            raise IndexError("peek from empty priority queue")
        return self.queue[0]

    def __len__(self):
        """Kuyruğun uzunluğunu döndürür."""
        return len(self.queue)
