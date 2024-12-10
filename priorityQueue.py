class PriorityQueue:
    def __init__(self):
        self.elements = []

    def enqueue(self, priority, item):
        self.elements.append((priority, item))
        self.elements.sort(reverse=True)  # Maksimum öncelikli olan ilk çıkar

    def dequeue(self):
        return self.elements.pop(0) if self.elements else None

    def is_empty(self):
        return len(self.elements) == 0