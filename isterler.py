from queue import PriorityQueue
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Bağlantı listesi
        self.adj_list = {} 
    def add_node(self, node):
        """Yeni bir düğüm ekler."""
        if node not in self.adj_list:
            self.adj_list[node] = []
    
    def wanted_author_queue(self, author_name):
        """Yazarın işbirliği yaptığı yazarları ağırlıklarına göre sıralayan kuyruk."""
        if author_name not in self.authors:
            return f"{author_name} adlı yazar bulunamadı."

        pq = PriorityQueue()
        author_obj = self.authors[author_name]
        
        # Yazarın işbirliği yaptığı yazarları ve ağırlıkları ekleyelim
        for coauthor, weight in author_obj.collaborations.items():
            pq.put((weight, coauthor))  # Öncelikli kuyruk: ağırlığa göre sıralama
        
        # Kuyruğu ağırlıklarına göre sıralı olarak döndürelim
        result = []
        while not pq.empty():
            weight, coauthor = pq.get()
            result.append(f"Yazar: {coauthor}, Ağırlık: {weight}")
        
        return "\n".join(result)


    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start, end):
        visited = set()
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = PriorityQueue()
        pq.put((0, start))
        path = {}

        while not pq.empty():
            current_distance, current_node = pq.get()
            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == end:
                break

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_node
                    pq.put((distance, neighbor))

        # Yol geri takibi
        final_path = []
        temp = end
        while temp in path:
            final_path.append(temp)
            temp = path[temp]
        final_path.append(start)
        final_path.reverse()

        return distances[end], final_path

    def shortest_path_for_author(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        levels = {start: 0}

        while queue:
            node = queue.popleft()
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    levels[neighbor] = levels[node] + 1
        return levels

    def count_collaborators(self, author):
        return len(self.graph[author])

    def most_collaborative_author(self):
        return max(self.graph, key=lambda author: len(self.graph[author]))


class PriorityQueueWrapper:
    def __init__(self):
        self.queue = PriorityQueue()

    def add(self, item, weight):
        self.queue.put((weight, item))

    def pop(self):
        return self.queue.get()

    def is_empty(self):
        return self.queue.empty()


class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left:
                self._insert_recursive(node.left, key)
            else:
                node.left = BSTNode(key)
        else:
            if node.right:
                self._insert_recursive(node.right, key)
            else:
                node.right = BSTNode(key)

    def inorder_traversal(self, node):
        if not node:
            return []
        return self.inorder_traversal(node.left) + [node.val] + self.inorder_traversal(node.right)

    def visualize(self):
        return self.inorder_traversal(self.root)
